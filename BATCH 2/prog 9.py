#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

for num in range(101):
    result = num % 5 != 0 
print(result)