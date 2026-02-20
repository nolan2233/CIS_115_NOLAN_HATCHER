#this program calculates the energy in joules produced

mass = float(input("Enter an Integer Value for Mass: "))
c = 2.99 * 10**8

def energy(mass):
    en = mass * (c * c)
    return en

result = energy(mass) 

print(f'The energy produced is {result:,.2f} Joules')

