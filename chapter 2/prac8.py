#Take three numbers as input and determine whether they can form a triangle. If they can, print whether the triangle is equilateral, isosceles, or scalene.
side1 = 3
side2 = 5
side3 = 5

if side1 + side2 > side3 :
    print('possibkl')
elif side1 + side3 > side2 :
    print('possible')
elif side3 + side2 > side1 :
    print('possible')
else:
    print('not possible')

if side1 == side2 == side3 :
    print(' tringal are equilateral')
elif side1 == side2 or side1 == side3 or side2 == side3 :
    print('triangle are isosceles')
elif  side1 != side2 != side3 :
    print('triangle are scalene')