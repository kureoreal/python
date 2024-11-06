edad = int(input("Escriba su edad: "))
dinero =int(input("Escriba cuanto dinero trae: "))
if(edad>=18):
    if(dinero>=50000):
        print(f"Puedes ingresar recuerda que el cover vale: {dinero} y te quedan {dinero-50000}")
    else:
        print(f"No puedes ingresar recuerda que el cover vale: 50000")
else:
    print(f"No puedes ingresar recuerda que la edad mínima es 18 años")