from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
import json
import pandas as pd

# fungsi untuk conver propertydata.json menjadi dataframe
def convert_json_to_df(json_file):
	# membuka file json untuk property
	with open(json_file) as file:
		data = json.load(file)

	# mengubah file json tersebut menjadi sebuah dataframe
	df = pd.DataFrame(data)
	return df

# fungsi untuk menambahkan label pada json data dengan mengambil
# input parameter yang berupa json data yang belum dilabel 
# dengan menghasilkan output berupa json data yang sudah dilabel
def label_data(input, output):
	# Iterate over each object in the JSON data
	for obj in data:
		price = obj['price']
		property_details = obj['property_details']

		# Check the conditions for labeling as "expensive"
		if price > 1000000 and len(property_details) > 5:
			obj['label'] = 'expensive'
		else:
			obj['label'] = 'not expensive'

	# Save the updated JSON data to a new file
	with open('labeled_data.json', 'w') as file:
		json.dump(data, file, indent=4)
