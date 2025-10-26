import csv
import unicodedata
import funciones_auxiliares

paises = {}
with open("paises_del_mundo_español.csv", "r") as archivo:
    for fila in archivo:
        lista_completa = fila.strip().split(",")
        nombre = lista_completa.pop(0)
        paises[nombre] = lista_completa
    
n = paises.pop("nombre")

print("¡Bienvenido a la base de datos de todos los países del mundo!")
funciones_auxiliares.imprimir_menu()
eleccion = input("")
while eleccion not in ["4","3","2","1", "0"]:
    eleccion = input("Por favor, ingrese una elección válida (0, 1, 2, 3, 4): ")

if eleccion == "1":
    nombre = input("Ingrese su búsqueda: ")
    while not funciones_auxiliares.solo_letras(nombre):
        nombre = input("Por favor, ingrese un nombre válido: ")

    funciones_auxiliares.buscar_pais(nombre, paises)

elif eleccion == "2":
    pass

elif eleccion == "3":
    pass

elif eleccion == "4":
    pass

else:
    pass


