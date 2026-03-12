"""

Ejercicio 9:

 - Hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111

"""

numeroUsuario = 0

while numeroUsuario != 111:
    numeroUsuario = int(input("Adivina el numero: "))
    if numeroUsuario == 111:
        print("Lo adivinaste!!")
        break
    else:
        print("Sigue intentando")
