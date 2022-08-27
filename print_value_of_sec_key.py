# Access the value of key2 from the following JSON
# write code to print the value of key2
# Expected Output:
# value2
import json
a= """{"key1": "value1", "key2": "value2"}"""
x=json.loads(a)
y=x["key2"]
print(y)