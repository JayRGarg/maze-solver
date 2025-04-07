class Point:

    def __init__(self, x:int, y:int):
        self.x:int = x
        self.y:int = y

class Line:

    def __init__(self, point_1:Point, point_2:Point):
        self.p1:Point = point_1
        self.p2:Point = point_2

    def draw(self, canvas, fill_color):
        x1:int = self.p1.x
        y1:int = self.p1.y
        x2:int = self.p2.x
        y2:int = self.p2.y
        print(f"Drawing {x1},{y2} to {x2},{y2}")
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

