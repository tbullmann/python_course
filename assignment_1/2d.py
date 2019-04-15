"""
Result for 2d)
Make sure to convert degree into radians
"""
from math import sin, radians, pi


angles = [radians(45), radians(90), 2 * pi]

for angle in angles:
    print('sin(', angle, ') =', sin(angle))
