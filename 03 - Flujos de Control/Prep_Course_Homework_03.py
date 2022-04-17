## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

from math import factorial


a = 5 
if a > 0:
    print("La variable", a, "es mayor a 0")
else:
    print("La variable ", a, " es menor a 0")

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

b = 90
c = 100
if type(b) == type(c):
    print("Las varibles son del mismo tipo")
else:
    print("las varibles son de diferente tipo")

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range (1,21):
    if n % 2 == 0:
        print(n, "Es un numero par")
    else:
        print(n, "Es un numero impar")

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for n in range (6):
    print(n,"Elevado a 3 es igual a:", n**3)

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

d = 3
for n in range (d):
    print (n+1, "Hola mundo")

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

f = 5
e = f
facto = 1
if f > 0:
    while e > 0:
        facto = facto * e
        e -= 1
    print("El factorial de", f, "es igual a", facto)
else:
    print(f, "No es un numero mayor a 0")

# 7) Crear un ciclo for dentro de un ciclo while

g = 1
while g < 4:
    for n in range (1, 4):
        print("Pista", g, "vuelta", n)
    g += 1

# 8) Crear un ciclo while dentro de un ciclo for


for n in range (3):
    h = 2
    while h > 0:
        print(h," mayor a cero")
        h -= 1
    print("Vuelta", n + 1)

# 9) Imprimir los números primos existentes entre 0 y 30


for n in range (1, 31):
    divisor = n
    contador = 0
    while divisor > 0:
        if n % divisor == 0:
            contador += 1
        else:
            pass
        divisor -= 1
    if contador == 2:
        print(n, "Es un numero primo")
    else:
        pass

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

print("Shi se puede")

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

cantidad_ciclos = 0
for n in range (1, 31):
    divisor = n
    contador = 0
    while divisor > 0:
        cantidad_ciclos += 1
        if n % divisor == 0:
            contador += 1
        else:
            pass
        divisor -= 1
    if contador == 2:
        print(n, "Es un numero primo")
    else:
        pass
    cantidad_ciclos += 1
print(cantidad_ciclos)

#----------------------------------------------------------------------------

cantidad_ciclos = 0
for n in range (1, 31):
    divisor = n
    contador = 0
    while (divisor > 0 and contador <= 2):
        cantidad_ciclos += 1
        if n % divisor == 0:
            contador += 1
        divisor -= 1
    if contador == 2:
        print(n, "Es un numero primo")
    else:
        pass
    cantidad_ciclos += 1
print(cantidad_ciclos)



# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n = 99
while(n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n, ' es divisible por 12')
# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

z = 100
while (z <= 300):
    if (z % 6 == 0):
        print ("El numero es:", z)
        break
    z += 1
