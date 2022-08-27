import json
list={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

item=input("enter the item :")
quantity=int(input("how much you want to buy :"))
a=list["shopping_list"][item]
b=int(a)-quantity
list["shopping_list"][item]=b
print(list)
