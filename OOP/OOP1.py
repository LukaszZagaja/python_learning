class Line:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
    
    def distance(self):
        x1,y1 = self.coordinate1
        x2,y2 = self.coordinate2

        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coordinate1
        x2,y2 = self.coordinate2

        return (y2 - y1) / (x2 - x1)


li = Line((3, 2), (8, 10))

print(li.distance())
print(li.slope())