"""
Ejercicio 3:

 - Programa que muestre los cuadrados (num*num) de los 60 primeros numeros naturales.
 - Reslverlo con el bucle for y con while

"""

numero = 0

while numero <= 60:
    numero = numero + 1
    print(numero * numero)

for numero2 in range(1, 62):
    print(f"for: {numero2 * numero2}")
