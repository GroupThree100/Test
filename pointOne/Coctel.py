class Coctel:
    def __init__(self):
        self.__name = None
        self.__price = None
        self.__amountAlcohol = None
        self.__amount = None
        self.__cost = None
        self.__temperature = None
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, data):
        self.__name = data
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, data): 
        self.__price = data
    
    
    @property
    def amountAlcohol(self):
        return self.__amountAlcohol
    @amountAlcohol.setter
    def amountAlcohol(self, data):
        self.__amountAlcohol = data
    
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, data):
        self.__amount = data
        
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, data):
        self.__cost = data
    
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self,data):
        self.__temperature= data