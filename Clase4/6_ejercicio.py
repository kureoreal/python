dinero = int(input("Cantidad de dinero: "))
manzanas = 500
peras = 200

if(dinero>=200):
    compra = input("Qué quiere comprar?: ")
    print(f"Compra: {compra}")
    if(compra =="manzana"):
        dinero = dinero-500
        print(dinero)
        if(dinero>200):
            compra = input("Qué quiere comprar?: ")
            if(compra =="peras"):
                dinero = dinero-200
                print(dinero)
        else:
            print("No te alcanza")
    elif(compra=="peras"):
        dinero=dinero-200
        print(dinero)
