import json

def open_json(json_file):
	with open(json_file) as file:
		data = json.load(file)

	return data