""" 1. Crear una pila vacia """
historial = []

""" 2. Apilar/ Push (Agregar elementos) """
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("Historial: ", historial)

""" 3. Ver el elemento superior (Peek/ Cima) """
pagina_actual = historial[2]
print("Pagina actual: ", pagina_actual)

""" 4. Desapilar/ Pop (Eliminar el ultimo elemento ingresado) """
pagina_salida = historial.pop()
print("Saliendo de: ", pagina_salida)

print("Historial actualizado: ", historial)