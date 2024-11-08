import math
angulo = int(input("Escriba el angulo: "))
operacion = input("Escriba la operación: ")
match operacion:
    case "sin":
        print(math.sin(angulo))
    case "cos":
        print(math.cos(angulo))
    case "tan":
        print(math.tan(angulo))
    case _:
        print("La operación no está disponible")
