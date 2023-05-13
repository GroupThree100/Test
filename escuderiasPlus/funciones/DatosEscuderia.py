from Escuderia import Escuderia

def DatosEscuderia():
    escuderia = Escuderia() #Instanciando el objeto Escuderia
    escuderia.nombre = input("Digite el nombre de la escudería: ")
    escuderia.casaMotor = input("Digite el nombre de la casa motor: ")
    escuderia.pilotoPrincipal.nombre = input("Digite el nombre del piloto principal: ")
    escuderia.pilotoPrincipal.fechaNacimiento = input("Digite fecha de nacimiento del piloto principal: ")
    escuderia.pilotoPrincipal.salarioAnual = float(input("Digite el salario del piloto principal: "))
    escuderia.pilotoPrincipal.Pais = input("Digite el País del piloto principal: ")
    escuderia.piloto2.nombre = input("Digite el nombre del piloto 2: ")
    escuderia.costos = float(input("Digite costos. "))
    return escuderia