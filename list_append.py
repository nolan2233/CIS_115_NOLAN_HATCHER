#this program appends a list  with a func 

lists = [1,2,3,4,5,6,7,8,9,10]

def append_to_list(val,list):
    list.append(val)
    return list
val = input("Enter an initial value: ")

append_to_list(val,lists)

num = input("Would you like to enter another value to append to the list? ")

while num =='y': 
    value = input("Enter a value: ")
    append_to_list(value,lists)
    num = input("Would you like to enter another value to append to the list?" )

    print(lists) 
    