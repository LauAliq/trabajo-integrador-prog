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
    print("Estas son las opciones que ofrece el menú. Seleccione una por favor: ")
    print("(1) 🔍 Buscar un país por nombre 🔍") #50
    print("(2) ⚙️       Filtrar países       ⚙️")
    print("(3) 📈      Ordenar países       📈")
    print("(4) 📊     Ver estadísticas      📊")
    print("(0) ❌           Salir           ❌")
    return None

def submenu_filtrar():
    print("¿Según qué desea filtrar su búsqueda?")
    print("(1) 🌍       Por continente      🌍")
    print("(2) 👤  Por rango de habitantes  👤")
    print("(3) 🏝️   Por rango de superficie  🏝️")
    print("(0) 🔙           Atrás           🔙")

#def submenu_ordenar():


#def submenu_estadisticas()

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


