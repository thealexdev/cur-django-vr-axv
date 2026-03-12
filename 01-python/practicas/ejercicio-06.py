"""

Ejercicio 6:

- Mostrar todas las tablas de multiplicar del 1 al 10
- Mostrando el titulo de la tabla y luego las multiplicaciones

"""

numTabla = 0
tabla = 1

for tablas in range(0, 9):
    numTabla = numTabla + 1
    print(f"Tabla del {numTabla}: ")
    for tabla in range(1, 11):
        print(f"{numTabla} X {tabla} = {numTabla * tabla}")
