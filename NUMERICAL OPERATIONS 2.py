import math
a = float(input("Please insert the first coefficient: "))
b = float(input("Please insert the second coefficient: "))
c = float(input("Please insert the third coefficient: "))
determinants = math.sqrt(b*b - 4*a*c)
x1 = (-b + determinants)/(2*a)
x2 = (-b - determinants)/(2*a)
print("The first root is ", x1)
print("The second root is ", x2) 


