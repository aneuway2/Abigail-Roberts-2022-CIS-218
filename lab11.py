"""
Abigail Roberts
Week 8-11 Lab
"""

class Car:
    def __init__(self, year, price):
        """year and price are variables"""
        self.__year= 2005 
        self.__price= 4010
    def ppy(self):
        #calculates price per year
        return self.__price / self.__year
    def __repr__(self):
        """__representation function"""
        return "Car (" +str(self.__year) + "," + str(self.__price) + ")"
    def set_year(self,sy):
        if sy >= 2012:
            print ("That is old.")
        if sy <= 2013:
            print ("That is new.")
        self.__year = sy
    def get_year(self):
        return self.__year
    def set_price(self, sp):
        if sp >= 10000:
            print ("That is cheap.")
        if sp <= 10001:
            print ("That is expensive.")
            self.__price = sp

    def __str__(self):
        """
        This returns a string of car information
        """
        return ( "Car year=" + str (self.year) + " price="+str(self.__price))

    def __eq__(self,other):
        """compares two years and prices"""
        if self is other:
            return True
        if type(self) != type (other):
            return False
        else:
            return self.__year == other.__price and \
                   self.price == other.__year

class Sedan(Car):
    """Sedan is a subclass of Cars"""
    def __init__(self, model, make):
        self.model= model
        self._make = make
        super().__init__()
        
    def __lt__(self,other):
        """lt function"""
        if type(Self) != type(other):
            return False
            return self.__Sedan() < other.__Sedan

    def __ge__(self,other):
        """ge function"""
        if type(self) != type(other):
            return False
        return self.__Sedan() >= other.__Sedan()

def __str__(self):
    return "Sedan type is "+str(self._model)+ "The make is = "+str(self.get_make())
           
class test_Car():
    """test class"""
    honda= Car()
    assert honda.get_year() == 2005
    assert honda.get_price == 4010
    '''assert str(honda) == '(2)'''
    honda.set_year(2005)
    honda.set_price(4010)
    assert honda.get_year() == 4010
    assert honda.ppy() == 2
    honda=Car()
    assert honda != sedan
    assert sedan != honda
    assert honda.ppy != sedan.ppy
    assert eval(repr(honda)) != sedan
    print ("Car class checks out fine!!")


  

    
    
