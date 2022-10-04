# Python ellipse clss execise
class Ellipse :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def area(self) :
        A = 3.14159*self.a*self.b
        return A

    def perimeter(self) :
        P = 2*3.14159*(((self.a**2)+(self.b**2))/2)**0.5
        return P

# main program
E1 = Ellipse(5, 8)
print("Area of E1 = " + str(E1.area()))
print("Perimter of E1 = " + str(E1.perimeter()))