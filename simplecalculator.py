#Simple calculator using python program
print("Welcome to the python calculator!")
num1 = int(input("Enter the frist number:\n"))
num2 = int(input("Enter the second number:\n"))
print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n")
choice = int(input("Enter your choice:\n"))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)   
print("Hope this is helpful.")     