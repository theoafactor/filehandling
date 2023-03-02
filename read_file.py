file_object = open("users.txt", "r")

data = file_object.readline()

print(data)

file_object.close()