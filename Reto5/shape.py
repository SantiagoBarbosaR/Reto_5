from math import degrees, acos, isclose, sqrt


# Clase Point
class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def compute_distance(self, other: "Point") -> float:
        return sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

    def __str__(self):
        return f"Point({self._x}, {self._y})"


# Clase Line
class Line:
    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start = start_point
        self.end = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start.compute_distance(self.end)

    def compute_slope(self):
        return (self.start._y - self.end._y) / (self.start._x - self.end._x)

    def __str__(self):
        return f"Line between {self.start} and {self.end}"


# Clase Shape
class Shape:
    def __init__(self, is_regular: bool, vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges()

    def calculate_edges(self) -> "list[Line]":
        shape_edges = []
        for i in range(len(self.vertices)):
            start = self.vertices[i]
            end = self.vertices[(i + 1) % len(self.vertices)]
            shape_edges.append(Line(start, end))

        if self.is_regular:
            lengths = [edge.length for edge in shape_edges]
            if not all(isclose(lengths[0], length) for length in lengths):
                raise ValueError("Shape must be regular.")
        return shape_edges

    def compute_perimeter(self) -> float:
        return sum(edge.length for edge in self.edges)


# Clase Rectangle
class Rectangle(Shape):
    def __init__(self, is_regular, vertices):
        if len(vertices) != 4:
            raise ValueError("A rectangle must have exactly 4 vertices.")
        super().__init__(is_regular, vertices)

    def compute_area(self):
        return self.edges[0].length * self.edges[1].length


# Clase Square
class Square(Rectangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if not all(isclose(self.edges[0].length, edge.length) for edge in self.edges):
            raise ValueError("All edges of a square must have the same length.")


# Clase Triangle
class Triangle(Shape):
    def __init__(self, is_regular, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")
        super().__init__(is_regular, vertices)

    def compute_area(self):
        a, b, c = (edge.length for edge in self.edges)
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))


# Clase Equilateral
class Equilateral(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if not all(isclose(self.edges[0].length, edge.length) for edge in self.edges):
            raise ValueError("An equilateral triangle must have all equal sides.")


# Clase Isosceles
class Isosceles(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        a, b, c = (edge.length for edge in self.edges)
        if not (isclose(a, b) or isclose(b, c) or isclose(a, c)):
            raise ValueError("An isosceles triangle must have at least two equal sides.")


# Clase Scalene
class Scalene(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        a, b, c = (edge.length for edge in self.edges)
        if isclose(a, b) or isclose(b, c) or isclose(a, c):
            raise ValueError("A scalene triangle must have all sides of different lengths.")


# Clase Trirectangle
class Trirectangle(Triangle):
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        a, b, c = sorted(edge.length for edge in self.edges)
        if not isclose(c**2, a**2 + b**2):
            raise ValueError("A trirectangle triangle must satisfy the Pythagorean theorem.")
