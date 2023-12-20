class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        radius = self.radius
        height = self.height
        return 3.14 * radius**2 * height
    
    def surface_area(self):
        radius = self.radius
        height = self.height
        return 2 * 3.14 * radius**2 + 2 * 3.14 * radius * height

# EXAMPLE OUTPUT
c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())