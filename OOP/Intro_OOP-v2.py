#Intro to OOP

class Car() :
    #init method or constructor
    def __init__(self, brand, model, ModelYear) :
        self.brand = brand
        self.model = model
        self.ModelYear = ModelYear
        
    def show_info(self) : # self => ต๋องใส่ไว้เสมอ
        print(self.brand + " " + self.model + " " + str(self.ModelYear))
    
    def used_price (self, year, msrp) :
        self.year = year # year of sale
        self.msrp = msrp # original prince
        factor = 1/(self.year - self.ModelYear)
        Price = factor * self.msrp
        return Price

        
myCar = Car("toyota","vios",2010)      # Object instantiation (object creation)
TomCar = Car("honda","civic", 2018)
JackCar = Car("suzuki","swift",2012)


Car.show_info(TomCar) # ไม่นิยมใช้

myCar.show_info()
TomCar.show_info()
JackCar.show_info()

myCar.show_info()
print(myCar.used_price(2022, 4000000))

Car.show_info(TomCar)
print(TomCar.used_price(2022, 500000))
# JackCar.show_info()