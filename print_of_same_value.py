# Parse the following JSON to get all the values of a key ‘name’ within an array
# Expected Output:

# ["name1", "name2"]
import json
a="""[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""
b=[]
x=json.loads(a)
for i in x:
    for j in i:
        if j=="name":
            b.append(i[j])
print(b)
