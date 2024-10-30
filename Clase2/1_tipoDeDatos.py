####################################### Textos
# Strings (Cadena de caracteres)
cadenadecaracteres = "324$%#$&jkldjs()[]"
print("El tipo de variable es: ",type(cadenadecaracteres))
print("El númnero de caracteres es : ",len(cadenadecaracteres))
# [Posición]
print(cadenadecaracteres[2])
print(cadenadecaracteres[9])
# [Inicio: Fin]
print(cadenadecaracteres[2:9])
print(cadenadecaracteres[2:10])
# [Inicio: Fin: Salto]
print(cadenadecaracteres[0:10:2])
print(cadenadecaracteres[0:10:4])
nombre = "    kureo real     "
print(nombre)
# Quitar los espacios
print(nombre.strip())
print(nombre.rstrip())
print(nombre.lstrip())
# Poner primer letra en mayúscula
print(nombre.strip().capitalize())
# Poner todo en mayúsculas
print(nombre.strip().upper())
# Poner todo en minúsculas
print(nombre.strip().lower())
# Buscar dentro del texto una palabra
texto = "Hola, bienvenidos a esta clase"
palabra = texto.index("esta")
print(palabra)
# Buscar números dentro de un texto
textoNumero="Carlos45%&"
numero = textoNumero.isalnum()
print(numero)
# Inicia en mayúscula
textoEnMayuscula = "Kureo"
mayus = textoEnMayuscula.isalpha()
print(mayus)
# Solo hay números
numeros = "12345678"
soloNumero = numeros.isalnum()
print(soloNumero)
# Char (Character)

######################################## Números

# int (Enteros)
# Positivos
numeroEntero = 5
print("El tipo de variable es: ",type(numeroEntero))
# Negativos
numeroEntero = -10
print("El tipo de variable es: ",type(numeroEntero))
# float (Decimáles)
# Positivos
numeroDecimal = 5.5
print("El tipo de variable es: ",type(numeroDecimal))
# Negativos
numeroDecimal = -5.5
print("El tipo de variable es: ",type(numeroDecimal))
######################################### Booleanos
# true - false
booleanTrue = True
print("El tipo de variable es: ",type(booleanTrue))
booleanFalse = False
print("El tipo de variable es: ",type(booleanFalse))
