from package_Shape.class_line import Point

class Line:
    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start = start_point
        self.end = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start.compute_distance(self.end)

    def compute_slope(self):
        return (self.start._y - self.end._y) / (self.start._x - self.end._x)

    def compute_horizontal_cross(self):
        if self.start._y * self.end._y > 0:
            return False
        if self.start._y == self.end._y:
            return False
        x_cross = self.start._x - (self.start._y * (
                  self.end._x - self.start._x)) / (self.end._y - self.start._y)
        return Point(x_cross, 0), True

    def compute_vertical_cross(self):
        if self.start._x * self.end._x > 0:
            return False
        if self.start._x == self.end._x:
            return False
        y_cross = self.start._y - (self.start._x * (
                  self.end._y - self.start._y)) / (self.end._x - self.start._x)
        
        return Point(0, y_cross), True
    
    def __str__(self):
        return (
        f" {self.start} {self.end} .")