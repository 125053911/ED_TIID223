""" for i in range(5):
    print(i)
 """
""" contador = 1
while contador <= 5:
    print(contador)
    contador += 1 """


""" Ejercicio 1. Colas """
from collections import deque

cola = deque()
respuesta = "s"

while respuesta.lower() == "s":
    opcion = 0

    while opcion != 4:
        print("1. Insertar en cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")

        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            numero = int(input("Ingresa un numero: "))
            cola.append(numero)
            print("Numero agregado")
        elif opcion == 2:
            if len(cola) > 0:
                numero = cola.popleft()
                print("Numero eliminado:", numero)
            else:
                print("La cola esta vacia")

        elif opcion == 3:
            print("Contenido de la cola:", list(cola))

        elif opcion == 4:
            print("Fin del menu")

        else:
            print("Opcion incorrecta")

    respuesta = input("Deseas ejecutar nuevamente? (s/n): ")

print("Programa terminado")
            


""" Ejercicio 2. Pilas """
pila = []
seguir = "s"

while seguir.lower() == "s":
    print("1. Apilar numero")
    print("2. Desapilar numero")
    print("3. Mostrar pila")
    print("4. Salir")

    opcion = 0

    while opcion != 4:
        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            valor = int(input("Ingresa un numero: "))
            pila.append(valor)
            print("Numero agregado a la pila")

        elif opcion == 2:
            if pila:
                valor = pila.pop()
                print("Numero retirado:", valor)
            else:
                print("La pila esta vacia")

        elif opcion == 3:
            print("Pila de arriba hacia abajo:")
            for valor in reversed(pila):
                print(valor)

        elif opcion == 4:
            print("Saliendo de la pila")

        else:
            print("Opcion incorrecta")

    seguir = input("Quieres volver a ejecutar? (s/n): ")

print("Programa terminado")