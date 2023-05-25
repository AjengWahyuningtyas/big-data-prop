from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
import json
import pandas as pd
import os

# fungsi untuk conver propertydata.json menjadi dataframe
def convert_json_to_dataframe(json_file):
	# membuka file json untuk property
	with open(json_file) as file:
		data = json.load(file)

	# mengubah file json tersebut menjadi sebuah dataframe
	df = pd.DataFrame(data)
	return df

# fungsi untuk membuka file json
def open_json(json_file):
	with open(json_file) as file:
		data = json.load(file)

	return data

# fungsi untuk menambahkan label pada json data dengan mengambil
# input parameter yang berupa json data yang belum dilabel 
# dengan menghasilkan output berupa json data yang sudah dilabel
def label_data(input, output):
	# cek apakah file output sudah ada atau belum
	if os.path.exists(output):
		print('Data sudah dilabel')
		return None
	# loop data dan menambahkan label dengan mengecek harga dan banyaknya detail pada property
	for obj in input:
		price = obj['price']
		property_details = obj['property_details']

		# Check the conditions for labeling as "expensive"
		if price > 1000000 and len(property_details) > 5:
			obj['label'] = 'expensive'
		else:
			obj['label'] = 'not expensive'

	# simpan data yang sudah dilabel ke dalam file json sesuai dengan parameter output
	with open(output, 'w') as file:
		json.dump(input, file, indent=4)
		print("Data berhasil dilabel")
		return output

# Data preprocess
# fungsi untuk memproses data yang akan digunakan untuk trainin
def preprocess(df):
	# mengambil kolom yang akan digunakan untuk training
	df = df[['title', 'description', 'price', 'property_details', 'label']]

	# menghitung panjang property_details, karena dalam datanya tersebut adalah sebuah array
	# maka panjangnya adalah banyaknya elemen dalam array tersebut dapat menentukan banyaknya detail
	# yang ada pada property sehingga dapat digunakan sebagai fitur untuk melihat kelayakannya
	df['property_details_length'] = df['property_details'].apply(lambda x: len(x))

	# Preprocess fiturnya
	X = df[['price', 'property_details_length']]

	# preprocess labelnya
	y = df['label']

	# memisahkan dataset untuk training dan testing
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
	return X_train, X_test, y_train, y_test

# Fungsi untuk melakukan training data
def train_data(X_train, X_test, y_train, y_test): 
	# lakukan training data naive bayes
	clf = GaussianNB()
	# fit data training ke dalam classifier
	clf.fit(X_train, y_train)

	# prediksikan label untuk test
	y_pred = clf.predict(X_test)
	
	# Evaluasi akurasi dari classifier
	accuracy = accuracy_score(y_test, y_pred)
	print("Accuracy:", accuracy)

	# return classifier
	return clf