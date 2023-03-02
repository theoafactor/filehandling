fullname = input("Enter full name: ")
email = input("Enter email: ")
password = input('Enter password: ')

file_object = open("users.csv", "a")

file_object.write("\n"+fullname + "," + email + ","+password)

file_object.close()
