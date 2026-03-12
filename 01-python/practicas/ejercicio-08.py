"""

Ejercicio 8:

 - Cuanto es el X % de X numero?
 - ej: 20% de 150

"""

numero = int(input("De que numero deseas obtener el porcentaje?: "))
porcentaje = int(input("De cuanto es el porcentaje?: "))

resultado = porcentaje / 100 * numero

print(f"El porcentaje de {numero} es {resultado}")
