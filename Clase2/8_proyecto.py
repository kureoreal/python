# 1. Pida los datos del vendedor
# - Nombre
# - Apellido
# - Dirección
# - Teléfono
# 2. Pase los datos a mayúsculas
# - Nombre
# - Apellido
# 3. Verifique que solo tenga números el teléfono
# 4. Pida el total de ventas
# 5. Calcule una comisión del 8% y dejela con un solo decimal
# 6. Sume el smlv mas la comisión
# 7. Diga el nombre completo del vendedor, su número de celular y lo que ganó ese mes
nombre=input("Escriba su nombre: ")
apellido=input("Escriba su apellido: ")
direccion=input("Escriba su dirección: ")
telefono=input("Escriba su telefono: ")
nombre= nombre.upper()
apellido= apellido.upper()
telefono=int(telefono)
print(type(telefono))
totalDeVentas = input("Escriba el valor total de las ventas: ")
totalDeVentas = int(totalDeVentas)
comision = totalDeVentas*0.08
comision = round(comision,1)
total = 1300000+ comision
print(f'Vendedor: {nombre} {apellido}, celular: {telefono} y lo que ganó este mes es: {total}')
