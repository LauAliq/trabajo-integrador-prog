import csv
import unicodedata
import os
import funciones_api
import funciones_auxiliares
from InquirerPy import inquirer

if not os.path.exists("paises_del_mundo_español.csv"):
    datos = funciones_api.obtener_datos_paises()
    if datos:
        funciones_api.generar_csv(datos)
else:
    pass

continentes = ["antartida", "america del sur", "america del norte", "africa", "asia", "oceania", "europa"]
paises = {}

# Apertura del archivo .csv
with open("paises_del_mundo_español.csv", "r", encoding="utf-8") as archivo:
    for fila in archivo:
        if "Tristán de Acuña" not in fila:
            lista_completa = fila.strip().split(",")
            nombre = lista_completa.pop(0)
            paises[nombre] = lista_completa
        else:
            lista_provisoria = fila.strip().split(",")
            lista_completa = []
            nombre = lista_provisoria[0].strip('"') + "," + lista_provisoria[1].strip('"')
            for i in range(2, 5):
                lista_completa.append(lista_provisoria[i])
            paises[nombre] = lista_completa
    
n = paises.pop("nombre")

# Eleccion Asc/Desc Opción 3 
def menu_asc_desc_1():
    ad_opciones = {
        "⬆️         Ascendente         ⬆️": lambda: funciones_auxiliares.ordenar_pais_por_poblacion(paises),
        "⬇️         Descendente        ⬇️": lambda: funciones_auxiliares.ordenar_pais_por_poblacion_op(paises),
        "🔙           Atrás           🔙" : None
    }
    
    sub_seleccion = inquirer.select(
            message="¿De qué manera quieres que se muestren?:",
            choices=list(ad_opciones.keys())
        ).execute()

    if ad_opciones[sub_seleccion] is None:
        print("Volviendo al menú principal...\n")
    else:
        ad_opciones[sub_seleccion]()

# Eleccion Asc/Desc Opción 4 
def menu_asc_desc_2():
    ad_opciones = {
        "⬆️         Ascendente         ⬆️": lambda: funciones_auxiliares.ordenar_pais_por_superficie(paises),
        "⬇️         Descendente        ⬇️": lambda: funciones_auxiliares.ordenar_pais_por_superficie_op(paises),
        "🔙           Atrás           🔙" : None
    }

    sub_seleccion = inquirer.select(
            message="¿De qué manera quieres que se muestren?:",
            choices=list(ad_opciones.keys())
        ).execute()

    if ad_opciones[sub_seleccion] is None:
        print("Volviendo al menú principal...\n")
    else:
        ad_opciones[sub_seleccion]()


# Submenú de la opción 2
def menu_filtrar_paises():
    sub_opciones = {
        "🌍       Por continente      🌍" : lambda: funciones_auxiliares.buscar_pais_por_continente(paises, continentes),
        "👤  Por rango de habitantes  👤" : lambda: funciones_auxiliares.buscar_pais_por_habs(paises),
        "🏝️   Por rango de superficie  🏝️" : lambda: funciones_auxiliares.buscar_pais_por_sup(paises),
        "🔙           Atrás           🔙" : None
    }

    while True:
        sub_seleccion = inquirer.select(
            message="¿Cómo quieres filtrar los países?:",
            choices=list(sub_opciones.keys())
        ).execute()

        if sub_opciones[sub_seleccion] is None:
            print("Volviendo al menú principal...\n")
            break
        else:
            sub_opciones[sub_seleccion]()

# Submenú de la opción 3
def menu_ordenar_paises():
    sub_opciones = {
        "🅰️         Por nombre        🅱️" : lambda: funciones_auxiliares.ordenar_pais_por_nombre(paises),
        "👤       Por población       👤" : menu_asc_desc_1,
        "🏝️        Por superficie      🏝️" : menu_asc_desc_2,
        "🔙           Atrás           🔙" : None
    }

    while True:
        sub_seleccion = inquirer.select(
            message="¿Cómo quieres ordenar los países?:",
            choices=list(sub_opciones.keys())
        ).execute()

        if sub_opciones[sub_seleccion] is None:
            print("Volviendo al menú principal...\n")
            break
        else:
            sub_opciones[sub_seleccion]()

# Submenú de la opción 4
def menu_estadisticas_paises():
    sub_opciones = {
        "📊  País con mayor y menor población  📊" : lambda: funciones_auxiliares.estadistica_1(paises),
        "📊 Promedio de población y superficie 📊" : lambda: funciones_auxiliares.estadistica_2(paises),
        "📊 Cantidad de países por continente  📊" : lambda: funciones_auxiliares.estadistica_3(paises),
        "🔙               Atrás                🔙" : None
    }

    while True:
        sub_seleccion = inquirer.select(
            message="¿Qué estadística desea mostrar?:",
            choices=list(sub_opciones.keys())
        ).execute()

        if sub_opciones[sub_seleccion] is None:
            print("Volviendo al menú principal...\n")
            break
        else:
            sub_opciones[sub_seleccion]()

# Menú principal
opciones = {
    "🔍   Buscar un país por nombre   🔍" : lambda: funciones_auxiliares.buscar_pais(paises),
    "⚙️         Filtrar países         ⚙️" : menu_filtrar_paises,
    "📈        Ordenar países         📈" : menu_ordenar_paises,
    "📊       Ver estadísticas        📊" : menu_estadisticas_paises,
    "❌             Salir             ❌" : None
}

bandera_menu_principal : bool = True
while bandera_menu_principal:
    seleccion = inquirer.select(
        message="Elige una opción:",
        choices=list(opciones.keys())
    ).execute()

    if opciones[seleccion] is None:
        print("Gracias por utilizar nuestro sistema. ¡Hasta luego!")
        bandera_menu_principal = False
    else:
        opciones[seleccion]()
