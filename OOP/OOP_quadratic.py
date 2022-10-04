#OOP demo - quadratic solver
class quadratic:
    def __init__(self, a, b, c):
        self.a = a      # attribute (variable used in class)
        self.b = b      # attribute
        self.c = c      # attribute
    def is_realroot(self):  # method (function inside class)
        d = (self.b)**2 - 4*self.a*self.c
        if d < 0 :
            return False
        else :
            return True
    def root(self):     #method
        d = (self.b)**2 - 4*self.a*self.c
        x1 = ((-self.b)+(d)**0.5)/(2*self.a)
        x2 = ((-self.b)-(d)**0.5)/(2*self.a)
        print(x1)
        print(x2)

# main body
P1 = quadratic(4,7,5)
print(P1.is_realroot())
P1.root()