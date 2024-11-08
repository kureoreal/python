# Es saber cual es el menor entre tres números
numeroUno = input("Escriba un número: ")
numeroDos = input("Escriba un número: ")
numeroTres = input("Escriba un número: ")
if(numeroUno<numeroDos):
    if(numeroUno<numeroTres):
        print(f"El número menor es numeroUno: {numeroUno}")
    else:
        print(f"El número menor es numeroTres: {numeroTres}")
else:
    if(numeroDos<numeroTres):
        print(f"El número menor es numeroDos: {numeroDos}")
    else:
        print(f"El número menor es numeroTres: {numeroTres}")