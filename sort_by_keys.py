# Sort JSON keys in and write them into a file
# Sort following JSON data alphabetical order of keys
# Expected Output:
# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# }
import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
x=sorted(sampleJson.items())
y=dict(x)
with open("sort.json","w") as f:
    json.dump(y,f,indent=4)
# print(json.dumps(y))

