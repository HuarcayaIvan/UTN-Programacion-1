

# 1) Lista con números del 1 al 100 que sean múltiplos de 4
multiplos_de_4 = list(range(4, 101, 4))
print("1) Múltiplos de 4 del 1 al 100:", multiplos_de_4)

# 2) Lista con cinco elementos y mostrar el penúltimo
gustos = ["chocolate", "música", "viajes", "películas", "lectura"]
print("2) Penúltimo elemento:", gustos[-2])

# 3) Lista vacía, agregar tres palabras con append
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("python")
lista_vacia.append("listas")
print("3) Lista después de append:", lista_vacia)

# 4) Reemplazar segundo y último valor en la lista de animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista animales modificada:", animales)

# 5) Explicación del programa 
print("""5) numeros = [8 15 3 22 7]
   numeros. remove(max( numeros))
   print (numeros)""")

print ("El código busca el número más grande de la lista y lo elimina, dejando el resto de los elementos sin modificar.")

# 6) Lista con números del 10 al 30 de 5 en 5 y mostrar los dos primeros
numeros_saltos = list(range(10, 31, 5))
print("6) Dos primeros números con salto de 5:", numeros_saltos[:2])

# 7) Reemplazar índices 1 y 2 en la lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print("7) Lista autos modificada:", autos)

# 8) Lista vacía y agregar dobles de 5, 10 y 15 con append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista dobles:", dobles)

# 9) Modificar la lista de compras según indicaciones
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("9) Lista compras modificada:", compras)

# 10) Lista anidada con elementos específicos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("10) Lista anidada:", lista_anidada)
