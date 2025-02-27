import json
 
python_dict = {"name": "afiq", "age":30, "gender": "male"}
json_string = json.dumps(python_dict)
print(json_string)

python_dict = json.loads(json_string)
print(python_dict)

with open('data.json', 'w') as file:
    json.dump(python_dict, file)