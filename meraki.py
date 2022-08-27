import json

a={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
x=json.dumps(a)
# with open("meraki.json","w")as f:
#     json.dump(a,f,indent=3)
print(x)
