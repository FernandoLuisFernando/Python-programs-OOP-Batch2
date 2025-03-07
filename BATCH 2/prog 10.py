#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

value1 = int(input("input the first number: "))
value2 = int(input("input the second number: "))
if value1 > value2:
    value1, value2 = value2, value1
print("Numbers between the two numbers: ")
for num in range(value1 + 1, value2):
    print (num)
    