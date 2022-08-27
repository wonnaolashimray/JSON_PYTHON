# Exercise 5: Access the nested key ‘salary’ from the following JSON
# write code to print the value of salary
# Expected Output:
# 7000
import json

k= """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
x=json.loads(k)
y=x["company"]["employee"]["payble"]["salary"]
print(y)