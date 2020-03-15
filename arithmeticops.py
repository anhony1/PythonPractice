# create a program to calculate the area and circumference of a circle. Ask the user for the radius!

import math

radius = float(input("Please Enter the Radius"))

area = math.pi * (radius ** 2)
circum = 2 * math.pi * radius
print("The area is: ", round(area,2))
print("The circumference is: ", round(circum,2))

