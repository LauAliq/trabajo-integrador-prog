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
