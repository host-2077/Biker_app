# Biker app. Ver 1.0 
# Diseñada por Ivan Robayo desde Colombia, América del Sur. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - READ.ME - - - - 
# Este es un programa que utiliza funciones básicas en Python para interactuar con el usuario y finalmente brindar información útil acerca de las especificaciones de la motocicleta que se está analizando entre ellas, su velocidad máxima teniendo en cuenta el peso real del usuario, su consumo de combustible y el gasto que puede generar. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - GitHub: ivrr207 - - - -


# Introducción al programa. 

print("Bienvenido a .")
userName = ("Para iniciar ingresa tu nombre.")
userBike = ("Ponle un nombre a tu vehículo.")
print("Hola", userName, "soy", userBike, "y voy a acompañarte en varias travesías. Entiendo que no conoces realmente de lo que soy capaz asi que este programa y el dispositivo que estás utilizando nos servirán como herramienta para comunicarnos efectivamente.") 
print("Dicho esto, iniciemos con los análisis. Ya que eres todo un maniático de la carretera vamos a empezar por la velocidad máxima que puedes alcanzar con tu actual peso, es decir, en útlima instancia soy yo", userBike, "quien está haciendo todo el trabajo, tu preocupate por hacer ejercicio a ver si podemos ir un poco más rápido.")
print("Para que todo salga bien asegurate de tener esta información: Cilindraje (CC), caballos de fuerza (HP), mi peso (" + userBike + ") (KG), tu peso (" + userName + ") (KG) y si aplica el peso de tu acompañante (KG")

# Ingreso de información a las variables requeridas. 

cilindraje = input("Ingresa el cilindraje (CC)")
horsePower = input("Ingresa los caballos de fuerza (HP)")
bikePeso = input("Ingresa el peso de la motocicleta (KG)")
userPeso = input("¿Cuánto pesas? (KG)")
user2Peso = input("¿Cuánto pesa tu acompañante? Si te gusta conducir la carretara solo como todo un vaquero renegado del oeste escribe 0")
masa = float(bikePeso) + float(userPeso) + float(user2Peso)

# Cálculo velocidad máxima de la motocicleta. 
# 1. Velocidad máxima en Metros / Segundos (M/S):

velocidadMaxMS = (float(horsePower) / 0.3) * 2.5 * masa 

# 2. Velocidad máxima en KM/H

velocidadMaxKh = velocidadMaxMS * 3.6 / 1000

# 3. Resultado. 

print(userName, "con tu peso actual y con la capacidad de ", userBike, "podrás dominar la carretera a una velocidad máxima de ", round(velocidadMaxKh, 2), "vaya! Que la pasma no se entere!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -PHASE 2 - - - -






# recorrido = input("KM")
# convierte los datos en float aca

# tiempo_estimado = recorrido / velocidadMaxKh
# horas = int(tiempo_estimado)
# minutos = int((tiempo_estimado - horas) * 60)
# print("sha la la ", horas, minutos)
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