"""
Area of Triangle when all sides of the triangle is known - a,b,c
Semi perimeter = (a+b+c)/2
Area = Square root of (s*(s-a)*(s-b)*(s-c))
"""

a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 # Squareroot is 1/2 power of the number

print(f"The area of triangle where side are {a}, {b}, {c} is {round(area,2)}")