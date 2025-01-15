from math import degrees, acos
from package_Shape.class_shape import Shape

class Triangle(Shape):
    def __init__(self, is_regular, vertices):
        if len(vertices) != 3:
            raise ValueError("It is not a triangle.")
        super().__init__(is_regular, vertices)
    
    def compute_area(self):
        a, b, c = (edge.length for edge in self.edges)
        semiperimter = (a+b+c)/2
        return (semiperimter*(semiperimter-a)*(semiperimter-b)*
               (semiperimter-c))**0.5
    
    def compute_inner_angles(self):
        angles = []
        a,b,c = (edge.length for edge in self.edges)
        
        a_angle = degrees(acos(((b**2 + c**2) - a**2)/(2*b*c)))
        b_angle = degrees(acos(((a**2 + c**2) - b**2)/(2*a*c)))
        c_angle = degrees(acos(((a**2 + b**2)- c**2)/(2*b*a)))
        
        angles.append (a_angle) 
        angles.append (b_angle) 
        angles.append (c_angle)
        return angles
