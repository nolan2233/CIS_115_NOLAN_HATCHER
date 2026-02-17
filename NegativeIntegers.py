#This program
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

result = num1 - num2

print(result)

if result >0:
    print("""
############################
Invalid! The Value is less than zero
   ############################
 """)
else:
    print("The values entered were valid integers") 