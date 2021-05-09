# Reto 1: Los cinco doses
#¿Sabrías obtener los números del 5 al 10 utilizando cinco 2's y los signos suma 
#(+), resta (-),  multiplicación (x) y división (/)?
#Te regalamos el ejemplo para el 5 y el resto deberás calcularlos y programarlos tú mismo. ¡Ánimo!

#Solucion
print("Ejercicio 1")
x  = int(2+2+2/2)     #5
x1 = int(2+2+2)       #6
x2 = int(2*2+2+2/2)   #7
x3 = int(2*2+2*2)     #8
x4 = int(2*2+2*2+2/2) #9
x5 = int(2+2+2+2+2)   #10
print(x,"-",x1,"-",x2,"-",x3,"-",x4,"-",x5)

## Reto 2: ¿Cuánto costará el teléfono?
'''
El IVA es un Impuesto sobre el Valor Añadido de un servicio o producto.
En España disponemos de varios tipos de IVA (21%, 10% y 4%).
Este impuesto grava sobre el precio neto del producto, es decir, el precio total o bruto corresponde 
al precio neto del producto más el impuesto que se le aplica.

Estamos interesados en comprar un nuevo teléfono móvil y en el escaparate de una tienda aparece que el móvil 
cuesta 420€. El problema es que si nos esperamos a comprarlo al día siguiente sufrirá un 
incremento porcentual del 20%. 
¿Cuánto costará entonces el teléfono si nos esperamos?
'''
#Solucion
print()
print("Ejercicio 2")
Costo_Movil = float(input("Cual es el Valor del Movil? "))
Incremento_Next_Day = float(input("Cual es el porcentaje de incremento? "))
Porcentaje_Incremento = (Incremento_Next_Day/100)
Valor_Aumento_Next_Day = Porcentaje_Incremento * Costo_Movil

Costo_Movil_Next_Day = Costo_Movil + Valor_Aumento_Next_Day

print("El valor del Movil al Siguiente dia es de =", Costo_Movil_Next_Day,"Euros")

## Reto 3: ¿Cuántas vueltas dará un Fidget Spinner?
'''
El spinner es un juguete que cabe en la palma de la mano y consiste en tres aros unidos entre sí. 
En el centro hay un círculo que hace las veces de eje giratorio y permite que los aros 
de vueltas y más vueltas, como las hélices de un helicóptero.

Sabemos que un Fidget Spinner da 147 vueltas por minuto ¿Cuántas vueltas dará en 640 segundos? 
Para este ejercicio se desprecia el rozamiento con el aire.
'''
#Solucion
print()
print("Ejercicio 3")
VPM = int(input("Ingrese la cantidad de Vueltas Por Minuto "))
Tiempo_Segundos = int(input("Ingrese el tiempo en Segundos "))
Minute_to_Second = 60
Tiempo_Minutos = Tiempo_Segundos/Minute_to_Second
Numero_Vueltas = Tiempo_Minutos * VPM
print("El numero de Vueltas en ",Tiempo_Segundos,"Segundos es de =", Numero_Vueltas,"Vueltas")

## Reto 4: ¿Cuántas latas de refresco sobran?
'''
Un acto de graduación es la ceremonia oficial que 
clausura el curso escolar y sirve de reconocimiento a los estudiantes que han completado los 
requisitos académicos de un plan de estudios y, por lo tanto, se han hecho merecedores del título académico.

Para organizar una fiesta de graduación del instituto se compran 9 
cajas de refrescos, donde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas 
y queremos que todas y cada una de ellas consuman la misma cantidad de refrescos 
¿Cuántas latas de refresco sobrarán?
'''
#Solucion
print()
print("Ejercicio 4")
Cantidad_Cajas = int(input("Ingrese la cantidad de cajas compradas = "))
Numero_Refrescos_caja = int(input("Ingrese la cantidad de botellas por caja = "))
Cantidad_Personas = int(input("Ingrese la cantidad de asistentes = "))
Total_Refrescos = Numero_Refrescos_caja*Cantidad_Cajas
Total_Refrescos_Por_Persona = (Total_Refrescos // Cantidad_Personas)
Total_Refrescos_Sobrantes = (Total_Refrescos % Cantidad_Personas)
print("La Cantidad de botellas sobrantes es de = ", Total_Refrescos_Sobrantes )