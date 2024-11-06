edad = int(input("Escriba su edad: "))
dinero =int(input("Escriba cuanto dinero trae: "))
if(edad>=18 and edad < 50):
    print(f"Edad mayor a 18 años y menor a 50: {edad}")
elif(edad>50):
    print(f"Estas muy viejo")
elif(edad<18 and dinero>50000):
    print(f"El dinero te deja entrar")
elif(edad>=50 and dinero>50000):
    print(f"Que no entra por viejo")


