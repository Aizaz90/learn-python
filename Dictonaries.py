# customer={
#     "name": "John",
#     "age": 30,
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("name"))
# print(customer.get("Fake"))

# customer["name"]="Jack"
# print(customer.get("name"))

# customer["BirthDate"]=1980
# print(customer.get("BirthDate"))

phone = input("Phone : ")
digit_mapping={

"1":"one",
"2":"Two",
"3":"Three"

}

output=""
for i in phone:
    output+=digit_mapping.get(i, "!")+" "

print(output)