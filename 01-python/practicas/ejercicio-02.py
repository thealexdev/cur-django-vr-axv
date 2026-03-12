"""
Ejercicio #2:

 - Escribir un script que nos muestre en pantalla
   todos los numeros pares del 1 al 120

"""


for contador in range(0, 121):
    if contador % 2 == 0:
        print(f"{contador} es par")
    elif contador % 2 != 0:
        print(f"{contador} no es par")
  