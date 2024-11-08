mascota = "loro"
match mascota:
    case "lagarto":
        print("La mascota es un lagarto")
    case "gato":
        print("La mascota es un gato")
    case "perro":
        print("La mascota es un perro")
    case "loro":
        print("La mascota es un loro")
    case _:
        print("No tiene mascota")