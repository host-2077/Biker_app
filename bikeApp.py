# print("Bienvenido a BikerApp.")
# userName = ("Para iniciar ingresa tu nombre.")
# userBike = ("Ahora ingresa el nombre de tu motocicleta, puede ser el modelo o el nombre que tu le has puesto a tu vechicículo.")
# print random catchy phrase. 
# print("Iniciemos con los análisis.")
cilindraje = input("CC") # Cilindraje en Centímetros Cúbicos
horsePower = input("HP") # Horse Power
bikePeso = input("KG") # Peso en Kg
userPeso = input("KG") # Peso en Kg
user2Peso = input("KG") # Peso en Kg
masa = float(bikePeso) + float(userPeso) + float(user2Peso) # Peso total en Km
velocidadMaxMS = (float(horsePower) / 0.3) * 2.5 * masa # Velocidad máxima en M/s
velocidadMaxKh = velocidadMaxMS * 3.6 / 1000 # Velocidad máxima en Km/h
print("Tu motocicleta recorrerá la ruta elegida a una velocidad máxima de ", round(velocidadMaxKh, 2))

#------ PHASE 2 -----------------
recorrido = input("KM")
# convierte los datos en float aca

tiempo_estimado = recorrido / velocidadMaxKh
horas = int(tiempo_estimado)
minutos = int((tiempo_estimado - horas) * 60)
print("sha la la ", horas, minutos)
# la distancia es importante solo si quiero saber el tiempo en el que voy a recorrer tal distancia. Es decir, una pregunta que sirve para utioiar tales es: Cuanto tiempo gastare en un recorrido de 150 km. con chala chala la 
# costeCombustible = # cuanto vale la gasolina 
# velocidadEstimada = #conductorbased
# ------------------------------------
# llena el tanque hasta la maxima capacidad para iniciar el calculo. 
# cual es la capacidad de tu tanque de gasolina?
# cual es el kilometraje actual que ves en el tacometro
# cuando el tanque se encuentre en la mitad por favor responde. Cuantos kilometros ves ahora en el tacometro?
# Bonus. si estuviste recorriendo continuamente tu motocicleta. EN cuanto tiempo viste que esta a la mitad?

# litros to Gal 
# def hpFormula():
    #nrpm x Cilindraje


# Quieres conocer la potencia de tu motocicleta en W o en HP 

# cuanto le cabe a tu tanque de gasolina?
# ingresa la cantidad que contiene ahora o si no estas seguro marca X
# el indicador esta en la mitad, en 
# ingresa el kilometraje actual de tu motocicleta, el que ves en el tacometro
# ingresa la cantidad de combustible que recargaste en el motor (preferiblemente llena este dato en la estacion de servicio)
# ingresa 