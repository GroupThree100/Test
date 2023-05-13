class Piloto:
    def __init__(self):
        self.__nombre=None
        self.__fechaNacimiento=None
        self.__salarioAnual=None
        self.__Pais=None
        
    @property
    def nombre(self):
        return self.__nombre   
    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @property
    def salarioAnual(self):
        return self.__salarioAnual
    @property
    def Pais(self):
        return self.__Pais


    @nombre.setter
    def nombre(self, dato):
        self.__nombre=dato
    @fechaNacimiento.setter
    def fechaNacimiento(self, dato):
        self.__fechaNacimiento=dato
    @salarioAnual.setter
    def salarioAnual(self, dato):
        self.__salarioAnual=dato
    @Pais.setter
    def Pais(self, dato):
        self.__Pais=dato
    
