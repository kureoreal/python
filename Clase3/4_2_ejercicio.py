######################################## SLICING
frase = "Queremos hacer una prueba de slicing"
# Recotar y mostrar el valor del recorte que diga prueba
busqueda = frase.index("p")
print(busqueda)
recorte = frase[busqueda:busqueda+6]
print(recorte)