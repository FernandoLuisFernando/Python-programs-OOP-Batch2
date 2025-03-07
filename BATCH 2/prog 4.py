#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

num1 = int(input("enter divident: "))
num2 = int(input("enter divisor: "))
if num2 == 0:
    print("Error: try another number.")
result = num1 // num2 
print(f"The answer is {result}")
