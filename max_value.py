#this program uses the max func to accept 2 int and returns the greater value 

num1 = int(input('Enter first value: '))
num2 = int(input('Enter second value:'))

def max(num1, num2):
    if num1 > num2: 
        print(num1)
    else:
        print(num2)

max(num1,num2)