#this program calculates the theta angle 

from math import atan2, pi

x = float(input("Enter an integer value "))
y = float(input("Enter an integer value "))


def ThetaTriangle(x,y ):
   angle = atan2(y, x) * (180 / pi)
   return angle 

result = ThetaTriangle(x,y)
print(f"The theta angle is: {result: .2f}")
