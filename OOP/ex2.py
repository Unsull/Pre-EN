class Triangle :
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c
        self.s = (self.a + self.b + self.c)/2

    def area(self) :
        # A = (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5
        # return A
        return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5

    def perimeter(self) :
        # P = self.a + self.b + self.c
        # return P
        return self.s * 2

# main program
T1 = Triangle(3, 4, 5)
print("Perimeter of T1 = " + str(T1.perimeter()))
print("Area of T1 = " + str(T1.area()))
