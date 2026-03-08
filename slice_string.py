#this program uses a func that returns a sliced string from position 0-3

stringVal = input("Enter the string value ")

def slice_my_string(stringVal):

    return stringVal[0:4]

print(slice_my_string(stringVal)) 