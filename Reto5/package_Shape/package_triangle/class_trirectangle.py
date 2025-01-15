import package_Shape.package_triangle.class_triangle as Triangle

class Trirectangle(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("Trirectangle cannot be regular")
        
        a, b, c = sorted(edge.length for edge in self.edges)
        if not (c**2 - (10**-9)) < (a**2 + b**2) <= c**2:
            raise ValueError(
            "You cannot create an Trirectangle triangle with the vertices")
