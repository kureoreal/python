# Pedir el nombre de la persona
# Pedir que letra desea cambiar
# Pedir la letra por la que lo desea remplazar
# Mostrar el nombre con el cambio de letra
nombre= input("Escriba su nombre completo: ")
letraBuscada = input("Escriba la letra a buscar: ")
letraReplazada = input("Escriba la letra por la que desea remplazar: ")
nombreRemplazado = nombre.replace(letraBuscada,letraReplazada)
print(f"Su nuevo nombre es: {nombreRemplazado}")