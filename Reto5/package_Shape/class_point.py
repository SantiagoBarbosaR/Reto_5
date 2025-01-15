class Point:

    def __init__(self, x: float=0, y: float=0):     
        self._x = x
        self._y = y

    def point_setter(self, new_x: float, new_y: float):
        self._x = new_x
        self._y = new_y

    def point_getter(self):
        return self._x, self._y

    def reset(self):
        self._x = 0
        self._y = 0

    def compute_distance(self, point: "Point") -> float:
        distance = ((self._x - point._x)**2+(self._y - point._y)**2)**(0.5)
        return distance

    def __str__ (self):
        return f"({self._x},{self._y})"
