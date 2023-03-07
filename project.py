"""Accept fullnames, emails and passwords from users 
using input() function and save them to a list of dictionaries. 
"""

fullname = input("Enter full name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

user = {
    "fullname": fullname,
    "email": email,
    "password": password
}
datastore = "userlist2.py"

try:
    #open the file for reading
    fobject = open(datastore, "r")

    #if the file exists, import it
    import userlist2

    # check if this email has been used already

    for stored_user in userlist2.users:
        if stored_user["email"] == email:
            ##the email has been used already
            print("This email has been used already")
            break 
    else:
        # open datastore for writing
        fobject2 = open(datastore, "w")

        fobject.close()
        
        # add the user dictionary to the list
        userlist2.users.append(user)
        #write to the datastore
        fobject2.write("users=" + str(userlist2.users))
        print("User saved")
        fobject2.close()

except:
    # print("File does not exist")
    # create the file
    fobject = open(datastore, "w")
    fobject.write("users=" + str([user]))
    fobject.close()







