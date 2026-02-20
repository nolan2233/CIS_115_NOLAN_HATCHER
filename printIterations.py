#this program uses a user defined func 

val = int(input("Enter an integer: "))
loopCounter = 0 

def print_iterations(Val):
    loopCounter = 0 

    for i in range(Val):
        loopCounter += 1

    return loopCounter

result = print_iterations(val)

print(f'The function call looped {result} times.')
