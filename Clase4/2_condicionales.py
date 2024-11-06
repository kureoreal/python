numeroUno = input("Escriba un número: ")
numeroDos = input("Escriba un número: ")
numeroTres = input("Escriba un número: ")
if(numeroUno>numeroDos):
    if(numeroUno>numeroTres):
        print(f"El número mayor es numeroUno: {numeroUno}")
    else:
        print(f"El número mayor es numeroTres: {numeroTres}")
else:
    if(numeroDos>numeroTres):
        print(f"El número mayor es numeroDos: {numeroDos}")
    else:
        print(f"El número mayor es numeroTres: {numeroTres}")