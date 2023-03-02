# -> open("name_of_file", "mode")
# modes:
# 1. w -> write
# 2. r -> read
# 3. a -> append
# file_object = open("users.txt", "w")

# file_object.write("Everybody is present\n")
# file_object.write("This is Python class\n")
# file_object.write("End of write-up")
# file_object.close()

## accept 'username' and 'password' from input and add them to a txt file.
username = input("Enter username: ")
password = input('Enter password: ')

# user = {
#     "username": username,
#     "password": password
# }


f_object = open("user_data.txt", "w")

f_object.write(username + "\n")
f_object.write(str(password) + "\n")

f_object.close()