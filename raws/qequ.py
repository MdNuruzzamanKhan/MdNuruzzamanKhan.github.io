# Solve the quadratic equation(দ্বিঘাত সমীকরণ)
# Author: Md. Nuruzzaman Khan

# import complex math module
import cmath

print("ax^2+bx+c=0")
print("a=",end="")
a = int(input())
print("b=",end="")
b = int(input())
print("c=",end="")
c = int(input())

# calculate the discriminant(নিশ্চায়ক)
d = (b**2) - (4*a*c)

# find two solutions
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are :\n{0:.4} and {1:.4}'.format(s1,s2))
# a+bj equals to a+bi

# OUTPUT:

# ax^2+bx+c=0
# a=1
# b=-2
# c=1
# The solutions are :
# (1+0j) and (1+0j)  