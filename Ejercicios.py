'''
## Ejercicio 1
Escribir una función a la que se le pase una cadena
 `<nombre>` y muestre por pantalla el saludo `¡hola <nombre>!`.

def saludo(nombre,apellido):
   
   return nombre+" "+apellido

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
print("¡Hola",saludo(nombre,apellido),"!")


## Ejercicio 2
Escribir una función que reciba un número entero 
positivo y devuelva su **factorial**.


def N_factorial(Numero_factorial):
   import math
   Numero_factorial= math.factorial(numero)
   return Numero_factorial

numero = int(input("Ingrese un numero entero positivo: "))
print("El numero factorial de ", numero , "es", N_factorial(numero))

'''
'''
## Ejercicio 3
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.


def IVA(Valor_Base,Porcentaje_Iva=19):
   Total = (Valor_Base*(Porcentaje_Iva/100))+Valor_Base
   return(Total)

#Valor_Base = float(input("Ingrese el valor del producto"))
#Porcentaje_Iva = int(input("Ingrese el valor del IVA"))

print("El valor total de la factura es de: ", IVA(5000,20), "COP")
'''
'''
## Ejercicio 4
Escribir una función que calcule el área de un círculo y otra que 
calcule el volumen de un cilindro usando la primera función.


from math import pi


def Area_Circulo(Radio):
   Area=pi*(Radio**2)
   return round(Area,3)

def Volumen_Cilindro(Altura):
  Area = Area_Circulo(Radio)
  #print(Area)
  Volumen = Area * Altura
  return round(Volumen,3)

Radio = float(input("Ingrese el valor del radio en CM "))
Altura = float(input("Ingrese el valor de la altura del cilindro en CM "))

print("El valor del area es de =", Area_Circulo(Radio),"Cm^2")
print("El valor del volumen del cilindro es de = ", Volumen_Cilindro(Altura)," cm^3")

'''
'''
Escribir un programa que lea un entero positivo *n*, introducido por el usuario y después 
muestre en pantalla la suma de todos los enteros desde 1 hasta *n*. La suma de los primeros
enteros positivos puede ser calculada de la siguiente forma:

![suma = \frac{n(n+1)}{2}](https://latex.codecogs.com/svg.latex?\Large&space;suma=\frac{n(n+1)}{2})


def Serie_Suma(Num):
   from fractions import Fraction
   suma = Fraction ((Num*(Num+1)),2)
   return suma

Num = int (input("Ingrese un numero entero positivo "))
print("LA sumatoria respectiva es de =", Serie_Suma(Num))

'''

'''
## Ejercicio 6
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
  `Tu índice de masa corporal es <imc>` donde `<imc>`
 es el índice de masa corporal calculado redondeado con dos decimales.
 '''
def IMC (Peso,Estatura):
   from fractions import Fraction
   Indice_Masa_Corporal = Fraction(Peso,(Estatura*Estatura))
   return round(Indice_Masa_Corporal,6)

#Peso = float(input("Ingrese su peso en Kg ="))
#Estatura = float(input("Ingrese su altura en metros ="))
Indice=IMC(150,1.5)
print ("Su IMC es de =", Indice)
if Indice<=18.5 :
   print ("Esta usted en Bajo Peso")
elif Indice>18.5 and Indice <= 24.9:
   print ("Esta usted Normal")
elif Indice>24.9 and Indice <= 29.9:
   print ("Esta usted en sobrepeso")
elif Indice>29.9 and Indice <= 34.9:
   print ("Esta usted Obeso")
else:
   print ("Error")
