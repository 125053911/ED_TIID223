""" for i in range(5):
    print(i)
 """
""" contador = 1
while contador <= 5:
    print(contador)
    contador += 1 """


""" Ejercicio 1. Colas """
cola = []
repetir = "S"

while repetir.lower() == "s":
    while True: 
        print("Menu - Colas")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            numero = input("Ingresa un numero: ")
            cola.append(numero)
            print("Numero agregado.")

        elif opcion == "2":
            if len(cola) > 0:
                print("Se elimino:", cola.pop(0))
            else: 
                print("La cola está vacía.")

        elif opcion == "3":
            print("Elementos de la cola: ", cola)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        respuesta = input("¿Quieres ejecutar otra vez? (s/n): ")

        print ("Fin del programa.")


""" Ejercicio 2. Pilas """
pila = []
seguir = "s"
while seguir.lower() == "s":
    print("\nPROGRAMA DE PILAS")

    opcion = 0

    while opcion != 4:
        print("\n1. Agregar numero")
        print("2. Quitar numero")
        print("3. Mostrar pila")
        print("4. Terminar")

        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            dato = int(input("Escribe el numero que deseas agregar: "))
            pila.append(dato)
            print("Numero guardado en la pila")

        elif opcion == 2:
            if pila:
                dato = pila.pop()
                print("Numero eliminado:", dato)
            else:
                print("No hay numeros en la pila")

        elif opcion == 3:
            if pila:
                print("Contenido de la pila:")
                for dato in reversed(pila):
                    print(dato)
            else:
                print("La pila esta vacia")

        elif opcion == 4:
            print("Has terminado de usar la pila")

        else:
            print("Selecciona una opcion valida")

    seguir = input("Deseas iniciar nuevamente? (s/n): ")

print("Programa cerrado")