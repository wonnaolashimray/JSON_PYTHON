import json

sample_json={
    "name": "David", 
    "class": "I", 
    "age": 6
}
x=json.dumps(sample_json)
# y=type(x)
print(x)