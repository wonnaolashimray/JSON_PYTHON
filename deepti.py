import json
x=open("deepti.txt","r")
a=x.read().split()
d={}
i=0
while i<len(a)-1: 
    d[a[i]]={a[i+1]}
    i+=2
print(d)
with open("deepti.json","w+")as f:
    json.dump(d,f,indent=4)
x.close()