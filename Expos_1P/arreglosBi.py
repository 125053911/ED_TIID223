matriz = [
    [1,2,3],
    [4,5,6]
]

print("Mostrar la matriz.")
for fila in matriz:
    print(fila)
print("")

""" Mostrar un valor en especifico """
print("Mostrar el 6.")
print(matriz[1][2])  
print("")  

""" Mostrar fila """
print("Mostrar la fila.")
print(matriz[0])
print("")

""" Modificar un valor en especifico """
print("Modificar el valor 5 por 8.")
matriz[1][1]=8
for fila in matriz:
    print(fila)
print("")

""" Agregar una fila """
print("Agregar una fila.")
matriz.append([7,8,9])
for fila in matriz:
    print(fila)
print("")

matriz[0].pop(2)
print("Eliminar el último elemento de la primera fila.")
for fila in matriz:
    print(fila)