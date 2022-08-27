# PrettyPrint following JSON data

# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
# Expected Output:
# {
#   "key1" = "value2",
#   "key2" = "value2",
#   "key3" = "value3"
# }
import json
var= {"key1": "value1", "key2": "value2","key":"value3"}
x=json.dumps(var,indent=2,separators=(","," = "))
print(x)
