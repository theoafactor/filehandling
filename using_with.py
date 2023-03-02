# file_object = open("users.csv", "r")

# data = file_object.read()

# file_object.close()

with open("users.csv", "r") as file_object:
    data = file_object.read()
    print(data)
