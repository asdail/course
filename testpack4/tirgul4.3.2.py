pw=input("Enter Password: ")
pw2=input("Confirm Password: ")
if pw2!=pw:
    for i in range(4):
        print("Passwords don't match!")
        pw2 = input("Confirm Password: ")
    print("Too many attempts.")
if pw2==pw:
    print("Congrats!")
