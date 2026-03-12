"""
Ejercicio 7:

- Programa que muestre todos los numeros impares
  entre dos numeros que elija un usuario.

"""

numeroUno = int(input("Ingresa el primer numero: "))
numeroDos = int(input("Ingresa el segundo numero: "))

if numeroUno < numeroDos:
    for numeros in range(numeroUno, numeroDos + 1):
        if numeros % 2 != 0:
            print(f"{numeros} es impar")
else:
    print(
        f"El numero {numeroUno} es mayor al numero {numeroDos}, ingresa un numero valido."
    )
