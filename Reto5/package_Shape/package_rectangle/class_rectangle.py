import package_Shape.class_shape as Shape

class Rectangle(Shape):
    def __init__(self, is_regular, vertices):
        if len(vertices) != 4: 
            raise ValueError("It is not a rectangle.")
        super().__init__(is_regular, vertices)

    def compute_area(self):
        width = self.edges[0].length
        length = self.edges[1].length
        return width * length

    def compute_inner_angles(self):
        return [90, 90, 90, 90]
