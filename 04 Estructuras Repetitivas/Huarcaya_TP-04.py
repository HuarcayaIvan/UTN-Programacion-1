# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#definicion de variables
numero = 0
#Inicio de ciclo
while numero <= 100:
    print(numero)
    numero += 1

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

#Definicion de variables
numero = int(input("Ingrese un número entero: "))
contador = 0

#Inicio de ciclo
if numero == 0:
    contador = 1
else:
    if numero < 0:
        numero = -numero
    while numero > 0:
        numero = numero // 10
        contador += 1
print("Cantidad de dígitos:", contador)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#Definicion de variables
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0
i = inicio + 1

#Inicio de ciclo

while i < fin:
    suma += i
    i += 1
print("La suma es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

total = 0
numero = int(input("Ingrese un número (0 para terminar): "))
while numero != 0:
    total += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))
print("La suma total es:", total)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True

print("Felicidades! Adivinaste el numero en", intentos, "intento(s).")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

i = 100
while i >= 0:
    if i % 2 == 0:
        print(i)
    i -= 1

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
i = 0
while i <= numero:
    suma += i
    i += 1
print("La suma es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)

cantidad = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0

i = 0
while i < cantidad:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    i += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad = 100 
suma = 0
i = 0

while i < cantidad:
    numero = int(input("Ingrese un número: "))
    suma += numero
    i += 1

media = suma / cantidad
print("La media es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número entero: "))
invertido = 0

while numero != 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)

