frase1 = "Hola"
frase2= "Kureo"
frase3= "Real"
resultado = " ".join([frase1, frase2, frase3])
print(resultado)
resultado = "-".join([frase1, frase2, frase3])
print(resultado)
resultado = resultado.replace('Hola','Adios')
print(resultado)
frase = "Anita lava la tina"
cambio = frase.replace("a", "e")
print(cambio)
frase = "La idea de hacer algo es siempre hacerlo con amor"
print("amor" in frase)
print("Kureo" in frase)
