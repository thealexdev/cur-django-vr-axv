"""

Ejercicio 10:

 - El programa tiene que pedir la nota de 15 alumnos y imprimir en pantalla
   cuantos han aprobado y cuantos han reprobado.

"""

# ingresando = True
# notasAlumnos = []

# while ingresando == True:
#     nota = int(input("Ingresa la nota de un alumno: "))
#     notasAlumnos.append(nota)
#     terminar = int(input("Son todos los alumnos? 5 - si 0 - no: "))
#     print(notasAlumnos)
#     if terminar == 5:
#         ingresando = False
#         break


# for resultado in notasAlumnos:
#     if resultado <= 6:
#         print(f"{resultado} Reprobo")
#     else:
#         print(f"{resultado} Aprobo")

# ingresando = True
# notasAlumnos = {}

# while ingresando == True:
#     nombre = input("Ingresa el nombre del alumno: ")
#     nota = int(input("Ingresa la nota de un alumno: "))

#     notasAlumnos[nombre] = nota

#     terminar = int(input("Son todos los alumnos? 5 - si 0 - no: "))
#     print(notasAlumnos)

#     if terminar == 5:
#         ingresando = False
#         break


# for alumno, nota in notasAlumnos.items():
#     if nota <= 6:
#         print(f"{alumno} Reprobo")
#     else:
#         print(f"{alumno} Aprobo")

ingresando = True
notasAlumnos = []

while ingresando == True:
    nota = int(input("Ingresa la nota de un alumno: "))
    notasAlumnos.append(nota)
    terminar = int(input("Son todos los alumnos? 5 - si 0 - no: "))
    print(notasAlumnos)
    if terminar == 5:
        ingresando = False
        break

sumaReprobados = 0
sumaAprobados = 0

for resultado in notasAlumnos:
    if resultado <= 6:
        sumaReprobados = sumaReprobados + 1
    else:
        sumaAprobados = sumaAprobados + 1

print(f"El total de aprobados es: {sumaAprobados}")
print(f"El total de reprobados es: {sumaReprobados}")
