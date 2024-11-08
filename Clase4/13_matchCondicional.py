# fruta = "pera"
# Si es mayor a 400 no se compra
# fruta = "manzana"
# Si es mayor a 300 no se compra
# fruta = "banano"
# Si es mayor a 500 no se compra

fruta = int(input("Escriba un número para seleccionar la fruta: \n 1. pera \n 2. manzana \n 3. banano \n\t:"))
match fruta:
    case 1:
        print("Ha elegido una pera")
        dinero = int(input("Escriba cuanto dinero trae: "))
        valorFruta = 300
        print("La fruta vale 300")
        if(dinero>400 & valorFruta<500):
            dinero = dinero-valorFruta
            print(f"Ha comprado una pera, le quedan ${dinero}")
        else:
            print("Esta muy cara no comprar")
    case 2:
        print("Ha elegido una manzana")
        dinero = int(input("Escriba cuanto dinero trae: "))
        valorFruta = 200
        print("La fruta vale 200")
        if(dinero>300 & valorFruta<300):
            dinero = dinero-valorFruta
            print(f"Ha comprado una manzana, le quedan ${dinero}")
        else:
            print("Esta muy cara no comprar")
    case 3:
        print("Ha elegido una banano")
        dinero = int(input("Escriba cuanto dinero trae: "))
        valorFruta = 499
        print("La fruta vale 499")
        if(dinero>500 & valorFruta<500):
            dinero = dinero-valorFruta
            print(f"Ha comprado una banano, le quedan ${dinero}")
        else:
            print("Esta muy cara no comprar")
    case _:
        print("No tenemos esa fruta")