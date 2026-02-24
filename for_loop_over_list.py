#this program uses list and for loops over the list and print it out

def getMyList():
    list = [10,20,30,40,50,60]

    length = len(list) 

    for item in list:
     
        print(item)

    return length

total = getMyList()
print(f'The total count is: {total}') 