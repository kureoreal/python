######################################## INDEX

# Pida al usuario que escriba su nombre
nombre = input("Escriba su nombre completo (nombres y apellidos): ")
print(f"El nombre ingresado es: {nombre}")
# Pida al usuario que letra quiere buscar dentro de su nombre
letra = input("Qué letra desea buscar?: ")
busqueda = nombre.index(letra)
print(f"Su letra está en la posición: {busqueda}")
# Pida al usuario desde que espacio (posición) debe comenzar
posicionInicial=input("Desde que espacio (posición) debe comenzar a buscar?: ")
posicionInicial= int(posicionInicial)
busqueda = nombre.index(letra,posicionInicial)
print(f"Su letra está en la posición: {busqueda}")
# Pida al usuario en que espacio (posición) debe terminar
posicionFinal=input("En que espacio (posición) debe terminar de buscar?: ")
posicionFinal= int(posicionFinal)
busqueda = nombre.index(letra,posicionInicial,posicionFinal)
print(f"Su letra está en la posición: {busqueda}")


