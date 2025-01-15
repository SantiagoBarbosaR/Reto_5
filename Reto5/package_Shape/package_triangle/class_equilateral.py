import package_Shape.package_triangle.class_triangle as Triangle

class Equilateral(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == False:
            raise ValueError("The instance is not regular.")
        
        a, b, c = (edge.length for edge in self.edges)
        
        if not (a == b and b == c):
            raise ValueError (
                "all sides must be equal.")