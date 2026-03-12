"""
Ejercicio 4:

 - Pedir dos numeros al usuario y hacer todas
 - las operaciones matematicas

"""

numeroUno = int(input("Ingresa el primer numero: "))
numeroDos = int(input("Ingresa el segundo numero: "))

print("-------------------------------------------")

print("Suma = 1")
print("Resta = 2")
print("Multiplicacion = 3")
print("Division = 4")

print("-------------------------------------------")

operacion = int(input("Selecciona la operacion: "))


if operacion == 1:
    print(f"El resultado de la suma es: {numeroUno + numeroDos}")
if operacion == 2:
    print(f"El resultado de la resta es: {numeroUno - numeroDos}")
if operacion == 3:
    print(f"El resultado de la multiplicacion es: {numeroUno * numeroDos}")
if operacion == 4:
    print(f"El resultado de la division es: {numeroUno / numeroDos}")
