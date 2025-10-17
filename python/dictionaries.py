# dict = {"name": "Rahul", "age": 20}
# for x in dict.keys():
#     print(x)
# for x in dict.values():
#     print(x)
# for x, y in dict.items():
#     print(x, y)



# nested dictionary
person = {
    "person_1": {
        "name": "Rahul",
        "age": 20
    },
    "person_2": {
        "name": "Manish",
        "age": 21
    },
    "person_3": {
        "name": "Yashvi",
        "age": 21
    }
}

for x, obj in person.items():
    print(x)

    for a, b in obj.items():
        print(a, b)