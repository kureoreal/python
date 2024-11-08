# and verdadero y verdadero verdadero
# and falso y verdadero falso
# and falso y falso falso


# o verdadero y verdadero verdadero
# o falso y verdadero verdadero
# o falso y falso falso

caracter = input("Escriba un caracter: ")
match caracter:
    case "a" | "e" | "i" | "o" | "u":
        print("Es una vocal")
    case '1' | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
        print("Es un numero")
    case _:
        print("No es una vocal o un número")

