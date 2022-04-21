# reuse the code: composition vs inheritance
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class LabeledPoint(Point):
    def __init__(self, initX, initY, label):
        super().__init__(initX, initY)
        self.label = label 

    def __str__(self):
        return super().__str__() + " (" + self.label + ")"

class LabelPoint2:
    def __init__(self, initX, initY, label):
        self.point = Point(initX, initY)
        self.label = label 

    def distanceFromOrigin(self):
        return self.point.distanceFromOrigin() 

    def __str__(self):
        return str(self.point) + " (" + self.label + ")" 

p = LabeledPoint(3, 4, "Here")
print(p)
print(p.distanceFromOrigin())

p2 = LabelPoint2(3, 4, "There")
print(p2)
print(p2.distanceFromOrigin())