# En la cadena encontrar la letra ñ
cadena = "dafhnjkdhsajkfhdaskjfhdksaññppoiid"
palabra = cadena.index("ñ")
print(palabra)
# En la frase imprimir solamente Kureo
frase = "Hola Kureo, saludos"
print(f"Lo que buscas es: {frase[5:10]}")
# Perdir un valor y convertirlo en flotante
numero = input("Escriba un número: ")
numeroflotante = float(numero)
print(type(numeroflotante))
print(numeroflotante)
# Escribir dos variables con palabras compuestas
nombreCompleto = 'Kureo Real'
edadUsuario = '50'
# Crear un texto donde el usuario diga su lenguaje de programación favorito
# y lo muestre con un mensaje
texto=input("Cúal es su lenguaje de programación favorito: ")
print(f"Su lenguaje favorito es: {texto}")
print("Su lenguaje favorito es:: ", texto)
print("Su lenguaje favorito es: "+str(texto))
print("Su lenguaje favorito es: {}".format(texto))

# Redondear a 3 decimales, 2 decimales,  1 decimal la siguiente división 153/19
division = 153/19
print(f"El resultado de 153/19 es :{round(division,3)}")
print(f"El resultado de 153/19 es :{round(division,2)}")
print(f"El resultado de 153/19 es :{round(division,1)}")
