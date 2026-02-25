#this program 

mass = int(input("Enter the value for mass: "))
velocity = int(input("Enter the value for velocity: "))

def kinetic_energy(mass,velocity):
    KE = .5 * (mass * (velocity ** 2))
    print(f'The amount of kinetic energy the ogject has is: {KE}kgs/mps2')

kinetic_energy(mass,velocity)