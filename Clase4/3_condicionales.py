texto = input("Escriba un texto (Que no tenga caracteres especiales): ")
texto = texto.isalnum()
print(texto)
if(texto):
    print(f"Has escrito de forma correcta: {texto}")
else:
    print(f"Has escrito de forma incorrecta: {texto}")