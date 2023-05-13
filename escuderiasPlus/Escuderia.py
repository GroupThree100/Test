from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__nombre=None
        self.__casaMotor=None
        self.__pilotoPrincipal=Piloto()
        self.__piloto2=Piloto()
        self.__costos=None


    @property
    def nombre(self):
        return self.__nombre
    @property
    def casaMotor(self):
        return self.__casaMotor
    @property
    def pilotoPrincipal(self):
        return self.__pilotoPrincipal
    @property
    def piloto2(self):
        return self.__piloto2
    @property
    def costos(self):
        return self.__costos


    @nombre.setter
    def nombre(self, dato):
        self.__nombre=dato
    @casaMotor.setter
    def casaMotor(self, dato):
        self.__casaMotor=dato
    @pilotoPrincipal.setter
    def pilotoPrincipal(self, dato):
        self.__pilotoPrincipal=dato
    @piloto2.setter
    def piloto2(self, dato):
        self.__piloto2=dato
    @costos.setter
    def costos(self, dato):
        self.__costos=dato
