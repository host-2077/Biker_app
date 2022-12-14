# Biker app. Ver 1.0 
# Diseñada por Ivan Robayo desde Colombia, América del Sur. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - READ.ME - - - - 
# Este es un programa que utiliza funciones básicas en Python para interactuar con el usuario y finalmente brindar información útil acerca de las especificaciones de la motocicleta que se está analizando entre ellas, su velocidad máxima teniendo en cuenta el peso real del usuario, su consumo de combustible y el gasto que puede generar. 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - GitHub: ivrr207 - - - - 
import time
# Introducción al programa.
print("Bienvenido a IN PROCESS.")
userName = input("Para iniciar ingresa tu nombre.")
userBike = input("Pónle un nombre a tu vehículo.")
message1 = "Hola ", userName, " soy ", userBike, " y voy a acompañarte en varias travesías. \nEntiendo que no conoces realmente de lo que soy capaz asi que este programa y tu teclado servirán como herramientas para comunicarnos efectivamente.\n> > > > > >\n"
for i in message1:
    print(i, end="", flush=True)
    time.sleep(0.1)
message2 = "Dicho esto, iniciemos con los análisis. \nYa que eres todo un maniático de la carretera vamos a empezar por la velocidad máxima que puedes alcanzar con tu peso actual.\n"
for i in message2:
    print(i, end="", flush=True)
    time.sleep(0.1)
message3 = "Necesitarás: \n- Cilindraje (CC) \n- Caballos de fuerza (HP) \n- Mi peso (" + userBike + ") (KG), \n- Tu peso (" + userName + ") (KG) \n- El peso de tu acompañante si es que existe. (KG)\n> > > > > >"
for i in message3:
    print(i, end="", flush=True)
    time.sleep(0.1)
# Ingreso de información a las variables requeridas.
cilindraje = input("Ingresa el cilindraje (CC)")
horsePower = input("Ingresa los caballos de fuerza (HP)")
bikePeso = input("Ingresa el peso de la motocicleta (KG)")
userPeso = input("¿Cuánto pesas? (KG)")
user2Peso = input("¿Cuánto pesa tu acompañante? (KG) > > > Si no tienes acompañante escribe '0'")
masa = float(bikePeso) + float(userPeso) + float(user2Peso)
# Notificación de análisis.
loading = "A N A L I S A N D O D A T O S / "
loadingprompt = loading * 3
for i in loadingprompt:
    print(i, end="", flush=True)
    time.sleep(0.1)
# Cálculo velocidad máxima de la motocicleta. 
# Velocidad máxima en Metros / Segundos (M/S):
velocidadMaxMS = (float(horsePower) / 0.3) * 2.5 * masa
# Velocidad máxima en KM/H
velocidadMaxKh = velocidadMaxMS * 3.6 / 1000
# 3. Resultado.
print("\n")
resultado = userName, " con tu peso actual y con la capacidad de ", userBike, " podrás dominar la carretera a una velocidad máxima de ", round(velocidadMaxKh, 2), " KM/H", "\n¡vaya! ¡Que la pasma no se entere!"
for i in resultado:
    print(i, end="", flush=True)
    time.sleep(0.1)
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