import package_Shape.package_rectangle.class_rectangle as Rectangle

class Square(Rectangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        
        a, b, c, d = (edge.length for edge in self.edges)

        if self.is_regular == True:
            if not (a == b and b == c and c == d and d == a):
                raise ValueError(
                    "all sides must be equal.")
        else:
            raise ValueError("The instance is not regular.")