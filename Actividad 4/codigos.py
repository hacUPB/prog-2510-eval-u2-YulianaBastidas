
1 # Código ejercicios 1

import math  # Importamos el módulo math para usar funciones matemáticas como sqrt()

# Pedir al usuario las coordenadas del primer punto
x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))

# Pedir al usuario las coordenadas del segundo punto
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2: "))

# Calcular la distancia entre los puntos usando la fórmula de la distancia euclidiana
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mostrar el resultado
print("La distancia entre los puntos es:", d)


2 #Código ejercicio 2

# Pedir al usuario la cantidad de tela en metros
medidas = float(input("Ingrese la cantidad de tela en metros: "))

# Convertir metros a pulgadas (1 pulgada = 0.0254 metros)
m = medidas / 0.0254  # Dividimos entre 0.0254 para obtener el equivalente en pulgadas

# Mostrar el resultado
print("La cantidad de tela en pulgadas es:", m)


3 # Código ejercicio 3

import math  # Importamos la librería math para usar la función sqrt()

# Pedir al usuario los valores de los catetos
A = float(input("Ingrese el valor del cateto A: "))
B = float(input("Ingrese el valor del cateto B: "))

# Calcular la hipotenusa usando el Teorema de Pitágoras
C = math.sqrt(A**2 + B**2)  # sqrt() calcula la raíz cuadrada

# Mostrar el resultado
print("La hipotenusa del triángulo es:", C)


4 # Código ejercicio 4

# Pedir al usuario la fecha de nacimiento
dia_nac = int(input("Ingrese el día de nacimiento: "))
mes_nac = int(input("Ingrese el mes de nacimiento: "))
anio_nac = int(input("Ingrese el año de nacimiento: "))

# Pedir al usuario la fecha actual
dia_actual = int(input("Ingrese el día actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
anio_actual = int(input("Ingrese el año actual: "))

# Calcular la edad inicial
edad = anio_actual - anio_nac

# Verificar si la persona aún no ha cumplido años este año
if mes_actual < mes_nac or (mes_actual == mes_nac and dia_actual < dia_nac):
    edad -= 1  # Se resta 1 a la edad porque aún no ha cumplido años

# Verificar si hoy es su cumpleaños
if dia_actual == dia_nac and mes_actual == mes_nac:
    print("¡Feliz Cumpleaños! 🎉")

# Mostrar la edad calculada
print("Tu edad actual es:", edad)


5 # Código ejercicio 5


# Pedir al usuario las horas trabajadas y el pago por hora
horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))

# Verificar si las horas exceden el límite permitido
if horas_trabajadas > 50:
    print("No se permite trabajar más de 50 horas.")
else:
    sueldo = 0  # Se inicia el sueldo en 0

    # Cálculo del sueldo según las condiciones establecidas
    if horas_trabajadas <= 40:
        sueldo = horas_trabajadas * pago_por_hora
    elif horas_trabajadas <= 45:
        sueldo = (40 * pago_por_hora) + ((horas_trabajadas - 40) * pago_por_hora * 2)
    else:
        sueldo = (40 * pago_por_hora) + (5 * pago_por_hora * 2) + ((horas_trabajadas - 45) * pago_por_hora * 3)

    # Mostrar el sueldo calculado
    print("El sueldo semanal es:", sueldo)
