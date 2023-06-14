import json
import csv
from transformers import pipeline
from util import open_json 

task = "zero-shot-classification"
zero_shot_model = "facebook/bart-large-mnli"

# 1: Load the zero-shot classification model
classifier = pipeline(task, zero_shot_model)

# 2: Melakukan definisi label
labels = ["expensive", "not expensive"]

# 3: membuat prompt
prompt_template = "This is the property of {title} with {property_details} and it values {price}."

# 4-6: melakukan klasifikasi property
def classify_property(title, price, property_details):
    prompt = prompt_template.format(title=title, property_details=property_details, price=price)
    result = classifier(prompt, labels)
    return result

# Step 7: Interpret the results and label the testing dataset
def label_dataset(testing_dataset):
    labeled_dataset = []
    for data_point in testing_dataset:
        title = data_point["title"]
        price = data_point["price"]
        property_details = data_point["property_details"]
        
        result = classify_property(title, price, property_details)
        predicted_label = result["labels"][0]
        predicted_score = result["scores"][0]
        
        data_point["predicted_label"] = predicted_label
        data_point["predicted_score"] = predicted_score
        
        labeled_dataset.append(data_point)
    
    return labeled_dataset

# Step 8: Testing dataset
testing_dataset = []
data = open_json('dataset/json/propertydata.json')
# mengambil beberapa the title, price, and property_details dari data
for obj in data:
	title = obj['title']
	price = obj['price']
	property_details = obj['property_details']
	testing_dataset.append({"title": title, "price": price, "property_details": property_details})
	
# Step 9: Label the testing dataset
labeled_testing_dataset = label_dataset(testing_dataset)

# Write the dataset 
for data_point in labeled_testing_dataset:
	print("====================================")
	print("Title:", data_point["title"])
	print("Price:", data_point["price"])
	print("Property Details:", data_point["property_details"])
	print("Predicted Label:", data_point["predicted_label"])
	print("Predicted Score:", data_point["predicted_score"])
	print("====================================")
	# simpan dengan json
	with open('dataset/json/labeled_testdata.json', 'w') as file:
		json.dump(labeled_testing_dataset, file, indent=4)

	# simpan dengan csv
	with open('dataset/csv/labeled_testdata.csv', 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Title", "Price", "Property Details", "Predicted Label", "Predicted Score"])
		for data_point in labeled_testing_dataset:
			writer.writerow([data_point["title"], data_point["price"], data_point["property_details"], data_point["predicted_label"], data_point["predicted_score"]])

# count the labeled_testing_dataset
print("Jumlah data yang sudah dilabel:", len(labeled_testing_dataset))
