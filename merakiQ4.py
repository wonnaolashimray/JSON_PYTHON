import json

a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
b=json.dumps(a,indent=5,sort_keys=True)
print(b)