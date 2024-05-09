import math
x = float(input("Please insert the value of x: "))
y = float(input("Please insert the value of y: "))
z = math.log10(abs(x)) + math.log10(abs(y))
sum_xy = x + y
difference_xy = x - y
product_xy = x*y
quotient_xy = x/y
remainder_xy = x%y
exponential_xy = x**y
absolute_x = abs(x)
absolute_y = abs(y)
absolute_z = abs(z)
square_root_x = math.sqrt(abs(x))
square_root_y = math.sqrt(abs(y))
square_root_z = math.sqrt(abs(z))
log_xyz = math.log(abs(x)) + math.log(abs(y)) + math.log(abs(z))
maximum_xyz = max(x, y, z)
minimum_xyz = min(x, y, z)
print("The sum of x and y is", sum_xy)
print("The difference between x and y is", difference_xy)
print("The product of x and y is", product_xy)
print("The quotient of x and y is", quotient_xy)
print("The remainder of x and y is", remainder_xy)
print("x to the power of y is", exponential_xy)
print("The absolute value of x is", absolute_x)
print("The absolute value of y is", absolute_y)
print("The absolute value of z is", absolute_z)
print("The sqaure root of x is", square_root_x)
print("The square root of y is", square_root_y)
print("The sqaure root of z is", square_root_z)
print("The value of log xyz base 10 is", log_xyz)
print("The maximum value from the list of x,y, and z is", maximum_xyz)
print("The minimum value from the list of x, y, and z is", minimum_xyz)
