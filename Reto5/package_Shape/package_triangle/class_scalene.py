from math import isclose
import package_Shape.package_triangle.class_triangle as Triangle

class Scalene(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Scalene cannot be regular.")
        
        a, b, c = (edge.length for edge in self.edges)

        scalene_condition = (
            not isclose (a,b) and 
            not isclose (b,c) and 
            not isclose (a,c)
        )

        if not scalene_condition:
            raise ValueError(
        "You cannot create an Scalene triangle with the vertices.")