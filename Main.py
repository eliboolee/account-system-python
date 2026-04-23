userList = {}

boole = True
while boole == True:
    print("Choose an option")
    print("1 - Login")
    print("2 - Register")
    print("E - Exit")
    choice = input("")

    if choice == "1":
        print("\n[Login]")
        username = input("Username: ")
        password = input("\nPassword: ")

        if username in userList and userList[username] == password:
            print("\nSuccess!\n")

            while True:
                print("Choose an option")
                print("3 - Change Password")
                print("4 - Logout")
                print("E - Exit")
                choice1 = input("")

                if choice1 == "3":
                    print("\n[Changing password]")
                    changePass = input("Password: ")
                    print("\n")
                    userList[username] = changePass
                elif choice1 == "4":
                    print("\nLogging Out...\n")
                    break
                elif choice1 == "E":
                    print("\nTerminating...")
                    boole = False
                    break
        else:
            print("\nIncorrect username/password!\n")
        
    elif choice == "2":
        print("\n[Register]")
        username = input("Username: ")
        password = input("\nPassword: ")
        userList[username] = password
        print("\nUser successfully added!\n")

    elif choice == "E":
        print("\nTerminating...")
        break
