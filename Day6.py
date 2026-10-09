contacts = {
    "Tom": "111",
    "Jack": "222",
    "Lucy": "333"
}
print(contacts["Jack"])
contacts["Bob"]="444"
contacts["Tom"]="999"
del contacts["Lucy"]
for item,value in contacts.items():
    print(f"{item}={value}")