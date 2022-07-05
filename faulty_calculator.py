# This is a faulty calculator where all results are correct except
# 1) 56+9  2) 45*3  3)56/6

print("Welcome to the Calculator")
num1 = int(input("Enter 1st number\n"))
num2 = int(input("Enter 2nd number\n"))
print("Input the corresponding operator you wish to perform ?")
print("1)Add\n2)Subtract\n3)Multiply\n4)Divide")
choice = input("Enter the operator\n")

if choice == "+":
    if num1 == 56 and num2 ==9:
        print("Sum is 77")
    else:
        print("Sum is",(num1 + num2))
elif choice == "*":
    if num1 == 45 and num2 == 3:
        print("Product is 555")
    else:
        print("Product is",(num1*num2))
elif choice== "/":
    if num1 == 56 and num2 == 6:
        print("Quotient is 4")
    else:
        print("Quotient is",(num1/num2))
else:
    print("Difference is",(num1-num2))


