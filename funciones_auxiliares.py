import unicodedata

# Funciones de validación

def solo_letras(texto):
    return (not texto == "") and (texto.isalpha())

def solo_numeros(texto):
    return (not texto == "") and (texto.isdigit())

def es_float(texto):
    if texto == "":
        return False
    else:
        try:
            float(texto)
        except:
            return False
        return True

# Funciones generales

def normalizar(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = "".join([c for c in texto_normalizado if unicodedata.category(c) != 'Mn'])
    return texto_sin_tildes.strip().lower()

def imprimir_menu():
    print("\nEstas son las opciones que ofrece el menú. Seleccione una por favor: ")
    print("(1) 🔍 Buscar un país por nombre 🔍") 
    print("(2) ⚙️       Filtrar países       ⚙️")
    print("(3) 📈      Ordenar países       📈")
    print("(4) 📊     Ver estadísticas      📊")
    print("(0) ❌           Salir           ❌")
    return None

def submenu_filtrar():
    print("\n¿Según qué desea filtrar su búsqueda?")
    print("(1) 🌍       Por continente      🌍")
    print("(2) 👤  Por rango de habitantes  👤")
    print("(3) 🏝️   Por rango de superficie  🏝️")
    print("(0) 🔙           Atrás           🔙")

def submenu_ordenar():
    print("\n¿Como quiere ordenar los países?")
    print("(1) 🅰️         Por nombre        🅱️")
    print("(2) 👤       Por población       👤")
    print("(3) 🏝️        Por superficie      🏝️")
    print("(0) 🔙           Atrás           🔙")

def submenu_ordenar_por_asc_o_desc():
    print("\n¿De qué forma?")
    print("(1) ⬆️         Ascendente         ⬆️")
    print("(2) ⬇️         Descendente        ⬇️")
    print("(0) 🔙           Atrás           🔙")

from collections import Counter

def submenu_estadisticas():
    print("\n¿Qué estadística desea mostrar? ")
    print("(1) 📊 País con mayor y menor población")
    print("(2) 📊 Promedio de población y superficie")
    print("(3) 📊 Cantidad de países por continente")
    print("(0) 🔙           Atrás           🔙")

def estadisticas_por_opcion(opcion, paises):
    poblaciones = [(pais, int(datos[0])) for pais, datos in paises.items() if datos[0].isdigit()]
    superficies = [(pais, int(datos[1])) for pais, datos in paises.items() if datos[1].isdigit()]
    continentes = [datos[2].lower() for datos in paises.values()]
    
    if opcion == "1":
        if poblaciones:
            pais_mayor_pob = max(poblaciones, key=lambda x: x[1])
            pais_menor_pob = min(poblaciones, key=lambda x: x[1])
            print(f"País con mayor población: {pais_mayor_pob[0]} ({pais_mayor_pob[1]:,} habitantes)")
            print(f"País con menor población: {pais_menor_pob[0]} ({pais_menor_pob[1]:,} habitantes)")
        else:
            print("No hay datos de población disponibles.")
            
    elif opcion == "2":
        if poblaciones and superficies:
            promedio_poblacion = sum(p[1] for p in poblaciones) / len(poblaciones)
            promedio_superficie = sum(s[1] for s in superficies) / len(superficies)
            print(f"Promedio de población: {promedio_poblacion:,.0f} habitantes")
            print(f"Promedio de superficie: {promedio_superficie:,.0f} km²")
        else:
            print("No hay datos suficientes para calcular promedios.")
    
    elif opcion == "3":
        conteo_continentes = Counter(continentes)
        print("Cantidad de países por continente:")
        for continente, cantidad in conteo_continentes.items():
            print(f"{continente.capitalize()}: {cantidad}")


def buscar_pais(nombre, diccionario):
    lista = []
    nombre = normalizar(nombre)
    for clave in diccionario:
        if nombre in normalizar(clave):
            lista.append(clave)
    if lista == []:
        print("No se encontraron países.")
    else:
        print("Esta es la lista de países encontrada: ")
        for elemento in lista:
            print(elemento)

def por_continente(nombre, diccionario):
    lista = []
    nombre = normalizar(nombre)
    for clave in diccionario:
        if nombre in normalizar(diccionario[clave][2]):
            lista.append(clave)
    print(f"Esta es la lista de países de {nombre}: ")
    for elemento in lista:
        print(elemento)

def por_habitantes(min, max, diccionario):
    lista = []
    for clave in diccionario:
        if min <= int(diccionario[clave][0]) and max >= int(diccionario[clave][0]):
            lista.append(clave)
    if lista == []:
        print("No se encontraron países.")
    else:
        print(f"Esta es la lista de países que tienen menos de {max} habitantes y más de {min} habitantes:")
        for elemento in lista:
            print(elemento)
        
def por_superficie(min, max, diccionario):
    lista = []
    for clave in diccionario:
        if min <= int(diccionario[clave][1]) and max >= int(diccionario[clave][1]):
            lista.append(clave)
    if lista == []:
        print("No se encontraron países.")
    else:
        print(f"Esta es la lista de países que tienen una superficie menor a {max} km² y mayor a {min} km²:")
        for elemento in lista:
            print(elemento)


