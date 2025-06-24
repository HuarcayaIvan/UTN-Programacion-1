

# 1) Factorial de un número y mostrar todos los factoriales desde 1 hasta n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Serie de Fibonacci hasta una posición dada
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("\nIngrese la cantidad de términos de Fibonacci a mostrar: "))
for i in range(posicion):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# 3) Potencia base^exponente con recursividad
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# 4) Conversión decimal a binario (cadena de texto)
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

decimal = int(input("\nIngrese un número decimal positivo para convertir a binario: "))
binario = decimal_a_binario(decimal)
print(f"El número binario es: {binario if binario else '0'}")

# 5) Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("\nIngrese una palabra para verificar si es un palíndromo: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("\nIngrese un número entero positivo para sumar sus dígitos: "))
print("Suma de los dígitos:", suma_digitos(numero))

# 7) Total de bloques para formar una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("\nIngrese la cantidad de bloques en el nivel inferior de la pirámide: "))
print("Bloques totales necesarios:", contar_bloques(nivel))

# 8) Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("\nIngrese un número: "))
digito = int(input("Ingrese un dígito (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
