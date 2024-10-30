# Primero es pedir los datos del cliente
nombre= input("Escriba su nombre: ")
apellido= input("Escriba su apellido: ")
# Pedir el número de la habitación
habitacion= input("Escriba el número de la habitación: ")
# Pedir cuantos días ha dormido el cliente en el hotel?
dias= input("Escriba el número de dias que ha estado en el hotel: ")
# Cada día vale $20000
dias= int(dias)
total= dias*20000

print("Señor(a): ",nombre," ",apellido," usted debe cancelar ",total," por los ",dias," dias" )
