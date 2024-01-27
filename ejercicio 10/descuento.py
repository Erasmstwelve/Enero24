def calcular_precio_con_descuento(precio_base, porcentaje_descuento): #Faltaba declarar el def y agregarle los :
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final #Estaba mal escrita

precio_base = float(input("Ingrese el precio base del producto: ")) #Faltaba el input
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")

