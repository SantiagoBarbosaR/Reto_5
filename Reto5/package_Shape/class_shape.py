from math import isclose
from package_Shape.class_line import Line
from package_Shape.class_point import Point

class Shape:
    def __init__(self, is_regular: "bool", vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges()
        self.inner_angles = self.compute_inner_angles()

    def calculate_edges(self) -> "list[Line]":
        shape_edges = [] 
        for index in range(len(self.vertices)):
            start_point = self.vertices[index]
            end_point = self.vertices[(index + 1) % len(self.vertices)]
            shape_edges.append(Line(start_point, end_point))
        
        if self.is_regular:
            comparison_length = shape_edges[0].length
            for edge_length in shape_edges:
                if not (isclose(comparison_length, edge_length.length)):
                    raise ValueError("The instance is not regular.")
        
        return shape_edges
    
    def compute_area(self) -> "float":
        pass

    def compute_perimeter(self) -> "float":
        shape_perimeter = 0
        for edges in self.edges:
            shape_perimeter += edges.length
        return shape_perimeter
    
    def compute_inner_angles(self) -> "list":
        pass

    def __str__(self):
        vertices = []
        for point in self.vertices:
            vertices.append(point.__str__())
        return (f" {vertices}.")
