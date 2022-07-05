# email :- abc@gmail.com
# password :- 123456


email = input("Apna email bata")
if '@' in email:
    password = input("Apna passowrd bhi bata")

    if email == "campusx@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "campusx@gmail.com" and password != "1234":
        print("Password Incorrect")
        password = input("Password fir se bol")
        if password == "1234":
            print("Finally correct")
        else:
            print("Still incorrect")
    else:
        print("Incorrect credentials")
else:
    print("Email galat hai sahi likho")