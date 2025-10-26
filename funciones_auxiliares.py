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
    return texto_sin_tildes.lower()

def imprimir_menu():
    print("Estas son las opciones que ofrece el menú. Seleccione una por favor: ")
    print("(1) 🔍 Buscar un país por nombre 🔍") #50
    print("(2) ⚙️       Filtrar países       ⚙️")
    print("(3) 📈      Ordenar países       📈")
    print("(4) 📊     Ver estadísticas      📊")
    print("(0) ❌           Salir           ❌")
    return None

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