# Alumno: Huarcaya Figueroa, Raul Ivan.
# Práctico 1: Estructuras secuenciales

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("hola mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Bienvenido, por favor ingrese un usuario")

print("Hola",nombre)

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

print ("Bienvenido, a continuacion debera ingresar sus datos personales")
nombre = input ("Ingrese su nombre")
apellido = input ("Ingrese su apellido")
edad = input("Ingrese su edad")
nacionalidad = input ("ingrese su nacionalidad")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {nacionalidad}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

print ("Calculadora de area y perímetro de un circulo")
print ("---------------------------------------------")

import math

radio = float(input ("Ingrese el radio"))

Area = round (math.pi * radio ** 2,2)
Perimetro = round(2 * math.pi * radio,2)

print ("El perimetro del circulo es de ",Perimetro)
print ("El area del circulo es de ",Area)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

print ("Conversor de segundos a horas")

Segundos = int(input ("Ingrese un valor en segundos"))
Horas = Segundos / 3600
print ("El resultado es de: ",round(Horas,1))

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número

print("Bienvenido a la tabla de multiplicar")

Numero = int(input ("Ingrese un numero por favor"))

for i in range(1, 11):
    print(f"{Numero} x {i} = {Numero * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

print("Operadores aritmeticos")
print("Ingrese 2 numeros enteros distintos del 0")

Numero1 = int(input("Ingrese el primer numero"))
Numero2 = int(input("ingrese el segundo numero"))

Suma = Numero1 + Numero2
Resta = Numero1 - Numero2
Multiplicacion = Numero1 * Numero2
Division = Numero1 / Numero2

print(f"Suma:{Suma}, Resta:{Resta}, Multiplicacion:{Multiplicacion}, Division:{Division}.")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que  el índice de masa corporal se calcula del siguiente modo: IMC = (peso en Kg / (altura en m)²)

print ("Calculadora de IMC")

Peso = float(input("Ingrese su peso en kilogramos"))
Altura = float(input("Ingrese su altura en metros"))
IMC = round(Peso / (Altura ** 2),1)

print ("Su IMC es de:", IMC)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print ("Conversor de Celsius a Fahrenheit")
print ("---------------------------------")
TempC = round(float(input("Ingrese un valor de temperatura en °C ")),2)
TempF = 9/5 * TempC + 32

print(f"La tempertura {TempC}°C equivale a {TempF} °F.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("Calculadora de promedio")

Num1 = int(input("Ingrese el primer valor numerico"))
Num2 = int(input("Ingrese el segundo valor numerico"))
Num3 = int(input("Ingrese el tercer valor numerico"))
Promedio = round(float((Num1 + Num2 + Num3) / 3),2)

print("El promedio es de: ",Promedio)

