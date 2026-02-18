#this program uses functions to calculate hypoteneuse of a right triangle

def triangle():

    side1 = int(input("Enter first number:"))
    side2 = int(input("Enter second number:"))
    product = (side1 * side2) + (side2 * side2) 
    side3 = product ** .5

    print(f"The missing side is: {side3}")

triangle()
