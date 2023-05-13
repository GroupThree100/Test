from funciones.DatosEscuderia import DatosEscuderia

escuderias = []
contador = 0

numeroEscuderias = int(input("¿Cuántas escuderías hay esta temporada? "))

while contador < numeroEscuderias:
    escuderia = DatosEscuderia()
    contador += 1

    escuderias.append(escuderia)

#Recorriendo la lista de escuderias
for escuderia in escuderias:
    print(escuderia.nombre, escuderia.costos)

costoMayor = 0
nombreEscuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaMasCara = escuderia.nombre
        
print(f"La escudería más costosa es la escudería {nombreEscuderiaMasCara} con un valor de {costoMayor}")
