import requests
import csv
import sys

API_URL = "https://restcountries.com/v3.1/all"
NOMBRE_ARCHIVO_CSV = "paises_del_mundo_español.csv"

ENCABEZADOS = ['nombre', 'poblacion', 'superficie', 'continente']

TRADUCCION_CONTINENTES = {"Africa": "África", "Americas": "América", "South America": "América del Sur", "North America": "América del Norte", "Asia": "Asia", "Europe": "Europa", "Oceania": "Oceanía", "Antarctica": "Antártida", "Antarctic": "Antártida", "N/A": "N/A"}

def obtener_datos_paises():
    
    parametros = {'fields': 'name,population,area,continents,translations'}
    
    print(f"-> Conectando con la API: {API_URL}. Por favor, espere un momento.")
    
    try:
        respuesta = requests.get(API_URL, params=parametros, timeout=10)
        respuesta.raise_for_status()
        
        datos_json = respuesta.json()
        print("-> Datos recibidos con éxito.")
        return datos_json
    
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}", file=sys.stderr)
        return None

def generar_csv(datos_paises):
    
    datos_estructurados = []
    
    for pais in datos_paises:

        nombre_comun = pais.get('name', {}).get('common', 'N/A')
        try:

            nombre = pais['translations']['spa']['common']
        except (TypeError, KeyError):

            nombre = nombre_comun
        
        continentes_en = pais.get('continents', [])
        
        continente_en = continentes_en[0] if continentes_en else 'N/A'
        
        continente = TRADUCCION_CONTINENTES.get(continente_en, continente_en)
        
        poblacion = pais.get('population', 0)
        superficie = pais.get('area', 0)
        
        datos_estructurados.append({'nombre': nombre, 'poblacion': int(poblacion), 'superficie': int(superficie), 'continente': continente})

    try:
        with open(NOMBRE_ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=ENCABEZADOS)
            escritor.writeheader()
            escritor.writerows(datos_estructurados)
            
        print(f"-> Archivo CSV '{NOMBRE_ARCHIVO_CSV}' generado exitosamente con {len(datos_estructurados)} países.")
        
    except IOError as e:
        print(f"Error al escribir el archivo CSV: {e}", file=sys.stderr)