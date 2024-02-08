class StarCookie:
    milk = 0.5

    def __init__(self, colour, weight):
        self.colour = colour
        self.weight = weight

star_cookie1 = StarCookie("Red", 15)
star_cookie2 = StarCookie("Blue", 50)
#star_cookie1.weight = 15
#star_cookie1.colour = "Red"
print("\nCOOKIE 1:")
print(star_cookie1.weight)
print(star_cookie1.colour)

#print(star_cookie1.milk) # instance 1
#print(star_cookie2.milk) # instance 2
#print(StarCookie.milk) # class
star_cookie2.milk = 0.2
print(star_cookie1.__dict__) # instance 1
print(star_cookie2.__dict__) # instance 2
print(StarCookie.__dict__) # class
