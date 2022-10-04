#Object-oriented programming demo
class circle:
    def __init__(self, r):
        self.r = r          #attribute
    def area(self):         #method
        return 3.14159*(self.r)**2  
    def circumf(self):      #method
        return 3.14159*2*self.r
    def sector(self, deg):
        return (3.14159*(self.r)**2)*(deg/360)
#main body
C = circle(7)   #create object C as a circle
Diameter = 2*C.r    #access attribute r of the object
Area = C.area()
Circumference = C.circumf()
angle = 90
Sarea = C.sector(angle)
print("A circle with diameter " + str(Diameter))
print("Area = " + str(Area))
print("Circumference = " + str(Circumference))
print(str(angle) + " degree sector has area " + str(Sarea))