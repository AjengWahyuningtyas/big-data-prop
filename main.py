# Mengambil fungsi dari src/func.py
from src.predict import *
from src.label import *

if __name__ == '__main__':
	# input_data = open_json('dataset/json/propertydata.json')
	output_data = 'dataset/json/labeled_testdata.json'
	# # Melakukan labeling data
	# label_data(input_data, output_data)
	# Mengubah data json menjadi dataframe
	df = convert_json_to_dataframe(output_data)
	# Melakan preprocessing
	X_train, X_test, y_train, y_test = preprocess(df)
	# Melakukan training data
	classifier = train_data(X_train, X_test, y_train, y_test)
	# Melakukan prediksi
	predict_data(classifier, X_test, y_test)
	# Melakukan evaluasi
	evaluate_data(X_test, y_test)
	# melakukan export model
	export_model(classifier, 'model/model.pkl')
