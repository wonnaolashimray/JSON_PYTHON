# Convert the following dictionary into JSON format
# Expected Output:
# data = {"key1" : "value1", "key2" : "value2"}
import json
data = {"key1" : "value1", "key2" : "value2"}
x= json.dumps(data)
# y=type(x)
print(x)