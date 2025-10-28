import csv
import unicodedata
import funciones_auxiliares

continentes = ["antartida", "america del sur", "america del norte", "africa", "asia", "oceania", "europa"]
paises = {}
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
eleccion = "-1"

while eleccion != "0":    
    print("\n¡Bienvenido a la base de datos de todos los países del mundo!")
    funciones_auxiliares.imprimir_menu()
    eleccion = input("> ")
    while eleccion not in ["4", "3", "2", "1", "0"]:
        eleccion = input("Por favor, ingrese una elección válida (0, 1, 2, 3, 4): ")

    if eleccion == "1":
        nombre = input("Ingrese su búsqueda: ")
        while not funciones_auxiliares.solo_letras(nombre):
            nombre = input("Por favor, ingrese un nombre válido: ")

        funciones_auxiliares.buscar_pais(nombre, paises)

    elif eleccion == "2":
        funciones_auxiliares.submenu_filtrar()
        subeleccion = input("> ")
        while subeleccion not in ["3", "2", "1", "0"]:
            subeleccion = input("Por favor, ingrese una elección válida (0, 1, 2, 3): ")

        if subeleccion == "1":
            continente = input("Ingrese el continente por el cual desea filtrar los países: ")
            while funciones_auxiliares.normalizar(continente) not in continentes:
                continente = input("Ingrese un continente válido (Antártida, América del Norte, América del Sur, Asia, África, Oceanía, Europa): ")
            funciones_auxiliares.por_continente(continente, paises)

        elif subeleccion == "2":
            min = input("Ingrese la cota inferior para la cantidad de habitantes: ")
            while not funciones_auxiliares.solo_numeros(min):
                min = input("Por favor, ingrese un valor válido: ")
            max = input("Ingrese la cota superior para la cantidad de habitantes: ")
            while not funciones_auxiliares.solo_numeros(max):
                max = input("Por favor, ingrese un valor válido: ")
            funciones_auxiliares.por_habitantes(int(min), int(max), paises)
            
        elif subeleccion == "3":
            min = input("Ingrese la cota inferior para la extensión de superficie en km²: ")
            while not funciones_auxiliares.solo_numeros(min):
                min = input("Por favor, ingrese un valor válido: ")
            max = input("Ingrese la cota superior para la extensión de superficie en km²: ")
            while not funciones_auxiliares.solo_numeros(max):
                max = input("Por favor, ingrese un valor válido: ")
            funciones_auxiliares.por_superficie(int(min), int(max), paises)

        else:
            print("Volviendo al menú principal...")

    elif eleccion == "3":
        funciones_auxiliares.submenu_ordenar()
        subeleccion = input("> ")
        lista_nombres_paises = list(paises.keys())
        
        while subeleccion not in ["3", "2", "1", "0"]:
            subeleccion = input("Por favor, ingrese una elección válida (0, 1, 2, 3): ")
        if subeleccion != "0":
            funciones_auxiliares.submenu_ordenar_por_opcion(subeleccion, lista_nombres_paises, paises)
        else:
            print("Volviendo al menú principal...")
        

    elif eleccion == "4":
        funciones_auxiliares.submenu_estadisticas()
        subseleccion3 = input("> ")
        while subseleccion3 not in ["1","2","3","0"]:
            subseleccion3 = input("Por favor, ingrese una elección válida (0,1,2,3): ")
        if subseleccion3 != "0":
            funciones_auxiliares.estadisticas_por_opcion(subseleccion3, paises)
        else:
            print("Volviendo al menú principal...")

    elif eleccion == "0":
        print("Gracias por utilizar este servicio. Hasta pronto!")
    
    print("--------------------------------------------------------------------")

