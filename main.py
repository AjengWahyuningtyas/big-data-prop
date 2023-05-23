# import file from folder src
from src.func import convert_json_to_df, label_data, add_label

data = 'dataset/json/propertydata.json'
df = convert_json_to_df(data)
label_data(df)

# Separate features and target variable
# X = df.drop('label', axis=1)  # Features
# y = df['label']  # Target variable

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Instantiate and train the Naive Bayes classifier
# clf = GaussianNB()
# clf.fit(X_train, y_train)

# # Label the example data
# example_data = df.head()

# # Preprocess the example data to match the format of the training data
# # Extract relevant features and transform them as needed

# # Predict the label for the example data
# example_features = preprocess_example_data(example_data)  # Custom function to preprocess example data
# predicted_label = clf.predict([example_features])

# print("Predicted label:", predicted_label) 

