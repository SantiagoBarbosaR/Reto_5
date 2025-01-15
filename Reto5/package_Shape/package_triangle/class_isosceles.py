from math import isclose
import package_Shape.package_triangle.class_triangle as Triangle

class Isosceles(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Isosceles cannot be regular.")
        
        a, b, c = (edge.length for edge in self.edges)
        
        isosceles_condition = (
            isclose(a, b) and not isclose(b, c) or
            isclose(b, c) and not isclose(c, a) or
            isclose(a, c) and not isclose(a, b)
        )

        if not isosceles_condition:
            raise ValueError(
        "You cannot create an isosceles triangle with the vertices.")