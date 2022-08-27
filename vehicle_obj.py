# Convert the following JSON into Vehicle Object
# For example, we should be able to access Vehicle Object using the dot operator like this.
# vehicleObj.name, vehicleObj.engine, vehicleObj.price
import json
a="""{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }"""
x=json.loads(a)
s=""
v="vehicleObj."
for i in x:
    y=s+v
    z=y+i
    print(z,end=",")


