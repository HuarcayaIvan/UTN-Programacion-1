
# 1) Añadir frutas al diccionario

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print("1) Diccionario actualizado con nuevas frutas:")
print(precios_frutas)

# 2) Actualizar precios de frutas existentes

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("\n2) Diccionario con precios actualizados:")
print(precios_frutas)

# 3) Lista de frutas sin precios

frutas = list(precios_frutas.keys())
print("\n3) Lista de frutas:")
print(frutas)

# 4) Agenda telefónica con 5 contactos

agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre del contacto que desea consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5) Análisis de una frase

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("\nPalabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo_palabras)

# 6) Notas de 3 alumnos y promedio

notas_alumnos = {}
for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {alumno}: ")) for j in range(3))
    promedio = sum(notas) / 3
    notas_alumnos[alumno] = promedio

print("\nPromedios:")
for alumno, promedio in notas_alumnos.items():
    print(f"{alumno}: {promedio:.2f}")

# 7) Sets de estudiantes que aprobaron Parcial 1 y Parcial 2

parcial1 = set(input("Ingrese nombres de aprobados en Parcial 1 (separados por coma): ").split(","))
parcial2 = set(input("Ingrese nombres de aprobados en Parcial 2 (separados por coma): ").split(","))

print("\nAprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno de los dos:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8) Stock de productos

stock = {}
continuar = True

while continuar:
    producto = input("Ingrese nombre del producto (o 'salir' para terminar): ")
    if producto.lower() == 'salir':
        continuar = False
    elif producto in stock:
        cantidad = int(input("Producto existente. Ingrese cantidad a sumar: "))
        stock[producto] += cantidad
    else:
        cantidad = int(input("Nuevo producto. Ingrese cantidad inicial: "))
        stock[producto] = cantidad

consulta = input("Ingrese producto para consultar stock: ")
print(f"Stock de {consulta}: {stock.get(consulta, 'Producto no registrado')}")

# 9) Agenda de eventos

agenda_eventos = {}
activo = True

while activo:
    dia = input("Ingrese el día del evento (o 'salir' para terminar): ")
    if dia.lower() == 'salir':
        activo = False
    else:
        hora = input("Ingrese la hora del evento: ")
        evento = input("Ingrese el evento: ")
        agenda_eventos[(dia, hora)] = evento

consulta_dia = input("Consultar evento - Ingrese día: ")
consulta_hora = input("Consultar evento - Ingrese hora: ")
evento = agenda_eventos.get((consulta_dia, consulta_hora))
if evento:
    print(f"Evento: {evento}")
else:
    print("No hay evento registrado para ese día y hora.")

# 10) Invertir diccionario país-capital

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("\nDiccionario invertido (Capital -> País):")
print(capitales_paises)
