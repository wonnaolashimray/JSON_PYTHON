import json
a=open("textfile.txt","r")
b=a.read().split()
# print(b)
d={}
i=0
while i<len(b)-1:
    d[b[i]]=b[i+1]
    i+=2
print(d)
with open("textfile.json","w")as f:
    json.dump(d,f,indent=4)
a.close()  