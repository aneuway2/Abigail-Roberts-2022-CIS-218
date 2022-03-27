"""Abigail Roberts"""

class Car(object):
    def __init__(self, make, model):
        print ("A new car")
        self.__make = make
        self.__model = model
    
    def main():
        make = ( input ("Enter make"))
        model = ( input ("Enter model"))
        print ("The make is a", "and the model is", model)
    if __name__ == '__main__':
        main()
        

