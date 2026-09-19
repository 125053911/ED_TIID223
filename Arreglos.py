# declarando un arreglo de enteros
numeros = [10, 20, 30 , 40, 50]

print(numeros[2]) # Imprime el tercer elemento del arreglo, que es 30

numeros[2] = 15 # Cambiando el valor del tercer elemento a 15
print(numeros[2]) # Imprime el nuevo valor del tercer elemento, que es 15

numeros.append(60) # Agregando un nuevo elemento al final del arreglo
print(numeros) # Imprime el arreglo completo, que ahora es [10, 20, 15, 40, 50, 60]

numeros.pop(1) # Eliminando el segundo elemento del arreglo
print(numeros) # Imprime el arreglo completo después de eliminar el segundo elemento, que ahora es [10, 15, 40, 50, 60]

numeros.remove(40) # Eliminando el elemento con valor 40 del arreglo
print(numeros) # Imprime el arreglo completo después de eliminar el elemento con valor

frutas=["Manzana", "Mango", "Uva", "Pera", "Maracuya"]
frutas.remove("Uva") # Eliminando el elemento con valor "Uva" del arreglo
print(frutas) # Imprime el arreglo completo después de eliminar el elemento con valor "Uva"

frutas.pop(3) # Eliminando el elemento en la posición 4 del arreglo, que es "Maracuya"
print(frutas) # Imprime el arreglo completo después de eliminar el elemento en la posición 4, que ahora es ["Manzana", "Mango", "Pera"]

frutas.append("Kiwi") # Agregando un nuevo elemento al final del arreglo
print(frutas) # Imprime el arreglo completo después de agregar "Kiwi"

frutas[2] = "Fresa" # Cambiando el valor del tercer elemento a "Fresa"
print(frutas) # Imprime el arreglo completo después de cambiar el valor del tercer elemento

vacio=[]
n = int(input("Ingrese el tamaño del arreglo: ")) #Input = imprimir en pantalla y esperar a que el usuario ingrese un valor
vacio.append(int(input("Ingresa el valor 0: ")))
print(vacio)


