"""

Ejercicio 5:

 - Hacer un programa que muestre todos los numeros entre dos numeros que elija un usuario


"""

numeroUno = int(input("Ingresa el primer numero: "))
numeroDos = int(input("Ingresa el segundo numero: "))
numeroDos = numeroDos + 1

if numeroUno < numeroDos:
    for numeros in range(numeroUno, numeroDos):
        print(numeros)
else:
    print("El primer numero tiene que ser menor al numero dos")
