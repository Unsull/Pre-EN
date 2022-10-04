class Triangle :
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c
        self.s = (self.a + self.b + self.c)/2

    def area(self) :
        return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5

    def perimeter(self) :
        return self.s * 2

# main program
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

d1 = ((x2-x1)**2 + (y2-y1)**2)**0.5 # a
d2 = ((x3-x2)**2 + (y3-y2)**2)**0.5 # b
d3 = ((x3-x1)**2 + (y3-y1)**2)**0.5 # c

print("d1 = " + str(d1) + "d2 = " + str(d2) + "d3 = " + str(d3))

T1 = Triangle(d1, d2, d3)
print("Perimeter of T1 = " + str(T1.perimeter()))
print("Area of T1 = " + str(T1.area()))
