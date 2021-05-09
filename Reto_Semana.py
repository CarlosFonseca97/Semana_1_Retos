'''
Descripción del problema:
El gobierno Colombiano tiene la necesidad de recaudar $23,4 billones de pesos por medio de impuestos
en la nueva reforma tributaria. Una de las propuestas que impacta el bolsillo de todos los colombianos,
es gravar con impuesto de IVA del 19% a varios de los productos que actualmente son exentos, y subir
del 5% a 19% a otro grupo de productos.
Para poder estimar qué productos son los indicados para ser grabados con el 19% de IVA, se te ha
pedido que crees una función que permita simular (calcular) cuanto se podrá recaudar de impuestos
para un producto que se esté evaluando si se entrega: precio base (antes de IVA) del producto, cantidad
que se espera vender en el siguiente año, porcentaje de IVA tiene actualmente el producto. Por defecto,
el IVA actual del producto se tomará como 0%. Como resultado, se espera que se devuelva el valor del
recaudo adicional que se recaudaría después de un año de aplicar el nuevo porcentaje de IVA sobre el
producto. Este resultado debe ser aproximado a máximo 2 decimales.

Entradas:
Nombre Tipo Descripción
precio_base float     "Valor del producto sin incluir impuestos"
cantidad int          "Cantidad de productos que se esperan vender en el próximo año"
porcentaje_actual int "Porcentaje de IVA que tiene el producto (por defecto es 0)"
Salida:
Tipo de retorno Descripción
float Valor que se recaudaría para el producto simulado
Ejemplos:
precio_base cantidad porcentaje_actual Valor de retorno
100 1000000 19000000.0
1000 1000000 5 140000000.0
158.53 2354837 5 52263723.35
'''
#Solucion
def Valor_Iva(precio_base, cantidad, porcentaje_actual):
    Valor_Retorno = ((porcentaje_actual*precio_base)+precio_base)*cantidad
    return round (Valor_Retorno,2)



#Entradas
precio_base = float(input("Ingrese el valor del producto sin incluir impuestos "))
cantidad    = int(input("Ingrese la cantidad de productos que se esperan vender en el proximo año "))
porcentaje_actual = int(input("Ingrese el porcentaje de iva que tiene el producto "))
Total_mas_iva = Valor_Iva(precio_base, cantidad, porcentaje_actual)

print("El valor esperado es de ", Valor_Iva(precio_base, cantidad, porcentaje_actual), "COP")