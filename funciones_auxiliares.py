import unicodedata
from collections import Counter

# Funciones de validación

def solo_letras(texto):
    sin_espacios = texto.replace(" ", "")
    return (not sin_espacios == "") and (sin_espacios.isalpha())

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

def buscar_pais(diccionario):
    nombre = input("Ingrese su búsqueda: ")
    while not solo_letras(nombre):
        nombre = input("Por favor, ingrese un nombre válido: ")
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

# Definimos funciones principales

def buscar_pais_por_continente(diccionario, continentes):
    continente = input("Ingrese el continente por el cuál desea filtrar los países: ")
    while normalizar(continente) not in continentes:
        continente = input("Ingrese un continente válido (Antártida, América del Norte, América del Sur, Asia, África, Oceanía, Europa): ")
    continente = normalizar(continente)
    lista = []
    for clave in diccionario:
        if continente in normalizar(diccionario[clave][2]):
            lista.append(clave)
    print(f"Esta es la lista de países de {continente}: ")
    for elemento in lista:
        print(elemento)

def buscar_pais_por_habs(diccionario):
    min = input("Ingrese la cota inferior para la cantidad de habitantes: ")
    while not solo_numeros(min):
        min = input("Por favor, ingrese un valor válido: ")
    min = int(min)
    max = input("Ingrese la cota superior para la cantidad de habitantes: ")
    while not solo_numeros(max):
        max = input("Por favor, ingrese un valor válido: ")
    max = int(max)
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

def buscar_pais_por_sup(diccionario):
    min = input("Ingrese la cota inferior para la extensión de superficie en km²: ")
    while not solo_numeros(min):
        min = input("Por favor, ingrese un valor válido: ")
    min = int(min)
    max = input("Ingrese la cota superior para la extensión de superficie en km²: ")
    while not solo_numeros(max):
        max = input("Por favor, ingrese un valor válido: ")
    max = int(max)
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

def ordenar_pais_por_nombre(paises):
    lista_nombres_paises = list(paises.keys())
    lista_nombres_paises.sort()
    for i in lista_nombres_paises:
        print(i)

def ordenar_pais_por_poblacion(paises):
    poblacion_paises = [(pais, int(datos[0])) for pais, datos in paises.items()]
    paises_por_poblacion = sorted(poblacion_paises, key=lambda x: x[1])
    for nombre, poblacion in paises_por_poblacion: 
        print(f"{nombre}: {poblacion:,} habitantes")

def ordenar_pais_por_poblacion_op(paises):
    poblacion_paises = [(pais, int(datos[0])) for pais, datos in paises.items()]
    paises_por_poblacion = sorted(poblacion_paises, key=lambda x: x[1], reverse=True)
    for nombre, poblacion in paises_por_poblacion: 
        print(f"{nombre}: {poblacion:,} habitantes")

def ordenar_pais_por_superficie(paises):
    poblacion_paises = [(pais, int(datos[0])) for pais, datos in paises.items()]
    paises_por_poblacion = sorted(poblacion_paises, key=lambda x: x[1])
    for nombre, superficie in paises_por_poblacion:
        print(f"{nombre}: {superficie:,} km²")

def ordenar_pais_por_superficie_op(paises):
    poblacion_paises = [(pais, int(datos[0])) for pais, datos in paises.items()]
    paises_por_poblacion = sorted(poblacion_paises, key=lambda x: x[1], reverse=True)
    for nombre, superficie in paises_por_poblacion:
        print(f"{nombre}: {superficie:,} km²")

def estadistica_1(paises):
    poblaciones = [(pais, int(datos[0])) for pais, datos in paises.items()]
    pais_mayor_pob = max(poblaciones, key=lambda x: x[1])
    pais_menor_pob = min(poblaciones, key=lambda x: x[1])
    print(f"País con mayor población: {pais_mayor_pob[0]} ({pais_mayor_pob[1]:,} habitantes)")
    print(f"País con menor población: {pais_menor_pob[0]} ({pais_menor_pob[1]:,} habitantes)")

def estadistica_2(paises):
    superficies = [(pais, int(datos[1])) for pais, datos in paises.items()]
    poblaciones = [(pais, int(datos[0])) for pais, datos in paises.items()]
    promedio_poblacion = sum(p[1] for p in poblaciones) // len(poblaciones)
    promedio_superficie = sum(s[1] for s in superficies) / len(superficies)
    print(f"Promedio de población: {promedio_poblacion:,} habitantes")
    print(f"Promedio de superficie: {promedio_superficie:,.1f} km²")

def estadistica_3(paises):
    continentes = [datos[2] for datos in paises.values()]
    conteo_continentes = Counter(continentes)
    print("Cantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"{continente}: {cantidad}")