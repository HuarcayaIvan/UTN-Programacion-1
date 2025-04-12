#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

from colorama import Fore, Style #Se importa de la libreria Colorama formato de texto para resaltar los resultados de los siguientes ejercicios.

Edad = int(input("Ingrese la edad el usuario "))

if Edad >= 18:
    print(Fore.GREEN, "El usuario es MAYOR de edad", Style.RESET_ALL)
else:
    print(Fore.RED, "El usuario es MENOR de edad", Style.RESET_ALL)

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

Nota = int(input("Ingrese la nota el usuario "))

if Nota >= 6:
    print(Fore.GREEN, "Aprobado", Style.RESET_ALL)
else:
    print(Fore.RED, "Desaprobado", Style.RESET_ALL)

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";  en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

Numero = int(input("Ingrese un numero "))

if Numero % 2 == 0 :
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

Edad = int(input("Ingrese su edad "))

if Edad < 12 :
    print("Usted pertenece a la categoria niño/a")
elif Edad >= 12 and Edad < 18 :
    print("Usted pertenece a la categoria adolecente")
elif Edad >= 18 and Edad < 30 :
    print("Usted pertenece a la categoria adulto/a joven")
else: 
    print("Usted pertenece a la categoria Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

Contraseña = int(len(input("Ingrese contraseña ")))

if (Contraseña >= 8) and (Contraseña <= 14) :
    print(Fore.GREEN,"Ha ingresado una contraseña correcta", Style.RESET_ALL)
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres", Style.RESET_ALL)

#6)  Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint (1,100) for i in range (50)]

print(mode(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mean(numeros_aleatorios))

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase o palabra por favor ")

if frase and frase [-1] in 'aeiou':
    print(frase,"!")
else:
    print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el  número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por  pantalla.
# Nota: investigue uso de las funciones upper(),lower() y title() de Python para convertir entre mayúsculas y minúsculas.

Nombre = input("Ingrese su nombre")

print("Selecciones una de las siguientes opciones:")
print("-------------------------------------------")
print("1. Nombre en mayúsculas.")
print("2. Nombre en minúsculas.")
Opcion = input(print("3. Nombre con la primera letra mayúscula."))

if Opcion == '1' :
    print(Nombre.upper())
elif Opcion == '2' :
    print(Nombre.lower())
elif Opcion == '3' :
    print(Nombre.title())
else:
    print("Reinicie el programa e ingrese una opcion valida")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima  el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

EscalaTerremoto = float(input("Ingrese la maginitud del terremoto segun la escala de Richter."))

if EscalaTerremoto <= 3 and EscalaTerremoto >= 0:
    print("Muy leve (imperceptible)")
elif EscalaTerremoto >= 3 and EscalaTerremoto < 4:
    print("Leve (ligeramente perceptible).")
elif EscalaTerremoto >= 4 and EscalaTerremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif EscalaTerremoto >= 5 and EscalaTerremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif EscalaTerremoto >= 6 and EscalaTerremoto < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else :
    print("Extremo (puede causar graves daños a gran escala).")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
#Periodo del año Estación en el:
#Desde el 21 de diciembre hasta el 20 de marzo (incluidos) - Estación en el hemisferio norte (Invierno) -  Estación en el hemisferio sur (Verano)
#Desde el 21 de marzo hasta el 20 de junio (incluidos) - Estación en el hemisferio norte (Primavera) -  Estación en el hemisferio sur (Otoño)
#Desde el 21 de junio hasta el 20 de septiembre (incluidos) - Estación en el hemisferio norte (Verano) -  Estación en el hemisferio sur (Invierno)
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) - Estación en el hemisferio norte (Otoño) -  Estación en el hemisferio sur (Primavera)

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla asi el usuario se encuentra en otoño, invierno, primavera o verano.

Estacion = input("Ingrese en qué hemisferio se encuentra Norte (N) o Sur (S): ").upper()
Mes = int(input("Ingrese el mes vigente (1 a 12): "))
Dia = int(input("Ingrese el día actual (1 a 31): "))


if Estacion == "N":
    if (Mes == 12 and Dia >= 21) or (Mes == 1) or (Mes == 2) or (Mes == 3 and Dia <= 20):
        print("Estás en Invierno")
    elif (Mes == 3 and Dia >= 21) or (Mes == 4) or (Mes == 5) or (Mes == 6 and Dia <= 20):
        print("Estás en Primavera")
    elif (Mes == 6 and Dia >= 21) or (Mes == 7) or (Mes == 8) or (Mes == 9 and Dia <= 20):
        print("Estás en Verano")
    elif (Mes == 9 and Dia >= 21) or (Mes == 10) or (Mes == 11) or (Mes == 12 and Dia <= 20):
        print("Estás en Otoño")
elif Estacion == "S":
    if (Mes == 12 and Dia >= 21) or (Mes == 1) or (Mes == 2) or (Mes == 3 and Dia <= 20):
        print("Estás en Verano")
    elif (Mes == 3 and Dia >= 21) or (Mes == 4) or (Mes == 5) or (Mes == 6 and Dia <= 20):
        print("Estás en Otoño")
    elif (Mes == 6 and Dia >= 21) or (Mes == 7) or (Mes == 8) or (Mes == 9 and Dia <= 20):
        print("Estás en Invierno")
    elif (Mes == 9 and Dia >= 21) or (Mes == 10) or (Mes == 11) or (Mes == 12 and Dia <= 20):
        print("Estás en Primavera")
else:
    print("Hemisferio no válido")
