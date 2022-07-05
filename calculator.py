print("Enter 2 nos to perform operations on")
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

print("Which operation do you wish to perfom? Enter the corresponding option")
print("1)Add\n2)Subtract\n 3)Divide\n4)Multiply")

choice = int(input("Enter your choice"))

#while choice <4:
if choice == 1:
        res = a+b
        print(res)
elif choice ==2:
        res = a-b
        print(res)
elif choice ==3:
        res  = a/b
        print(res)
else:
        res = a*b  
        print(res)        