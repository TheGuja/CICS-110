# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

def legal_triangle_angles(angle_A, angle_B, angle_C):

    if angle_A + angle_B + angle_C == 180:
        return "triangle"
    
    return "not a triangle"

def legal_triangle_sides(side_a, side_b, side_c):

    if (side_a < (side_b + side_c)) and (side_b < (side_a + side_c)) and (side_c < (side_a + side_b)):
        return "triangle"
    
    return "not a triangle"
    
def triangle_angle_type(angle_A, angle_B, angle_C):

    if angle_A == 90 or angle_B == 90 or angle_C == 90:
        return "right"
    elif angle_A > 90 or angle_B > 90 or angle_C > 90:
        return "obtuse"
    elif angle_A < 90 and angle_B < 90 and angle_C < 90:
        return "acute"
    
def triangle_side_type(side_a, side_b, side_c):
    
    if side_a == side_b == side_c:
        return "equilateral"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "isosceles"
    elif side_a != side_b != side_c:
        return "scalene"
    

print(legal_triangle_sides(8,1,1))