from colorama import Fore, Style, init 
init()
# Definimos colores
rojo = Fore.RED
verde = Fore.GREEN
azul = Fore.BLUE
reset = Style.RESET_ALL

# Funcion para crear conjuntos a partir de DNIs ingresados por el usuario
def crear_conjunto_dni():  # No recibe parametros
    lista_conjuntos = []  # Lista vacia para almacenar los conjuntos
    while True:
        # Pide al usuario los DNI
        x = input('Por favor, ingresá los DNI sin puntos ni espacios (o escribí "fin" para terminar): ')
        if x.lower() == 'fin':  # Convertimos el str x en minuscula
            break  # Se detiene el bucle
        elif x.isdigit():  # verifica si la cadena de texto contiene únicamente caracteres numéricos
            conjunto = {int(digito) for digito in x} # Usamos compresion de conjuntos
            lista_conjuntos.append(conjunto)  # Agregamos conjunto a la lista
        else:
            # En caso de que no contenga únicamente solo caracteres numéricos
            print('Entrada inválida. Ingresá sólo números, sin puntos ni espacios.')
    return lista_conjuntos

# Funcion para calcular y visualización de la unión de n conjuntos

# Usamos * para recibir cualquier cantidad de conjuntos.
def union_conjuntos(*conjuntos):
    resultado = set()  # Conjunto vacio para almacenar el resultado
    for conjunto in conjuntos:
        # modifica el conjunto resultado agregandole todos los elementos del conjunto
        resultado |= conjunto
    return resultado

# Funcion para calcular y visualización de la intersección de n conjuntos

# Usamos * para recibir cualquier cantidad de conjuntos.
def interseccion_conjuntos(*conjuntos):
    if not conjuntos:  # Verifica si no se pasó ningún conjunto.
        return set()  # Retornamos un conjunto vacio
    else:
        # Usamos el primer conjunto de la lista como base para la intersección.
        resultado = conjuntos[0].copy()
        # Tomamos todos los conjuntos menos el primero
        for conjunto in conjuntos[1:]:
            resultado &= conjunto  # modifica el conjunto resultado
    return resultado

# Funcion para calcular y visualización de las diferencias de n conjuntos

# Usamos * para recibir cualquier cantidad de conjuntos.
def diferencia_conjuntos(conjunto_base, *otros_conjuntos):
    # Creamos una copia del conjunto que vamos usar como base para no modificar el original
    resultado = conjunto_base.copy()
    for conjunto in otros_conjuntos:
        # Sacá del conjunto resultado todos los elementos que estén en este otro conjunto."
        resultado -= conjunto
    return resultado

# Funcion para calcular y visualización de la diferencia simétrica  de n conjuntos

# Usamos * para recibir cualquier cantidad de conjuntos.
def dif_simetrica_conjuntos(conjunto_base, *otros_conjuntos):
    # Creamos una copia del conjunto que vamos usar como base para no modificar el original
    resultado = conjunto_base.copy()
    for conjunto in otros_conjuntos:
        # modifica el conjunto resultado eliminando todos los elementos que estén en conjunto.
        resultado ^= conjunto
    return resultado

# ------------ Claudio-------------------

def evaluar_conjuntos(conjuntos):
    print("\n" + "="*10 + " Evaluación de condiciones lógicas " + "="*10)

    # 1. Ver si todos los conjuntos tienen los mismos elementos
    son_equivalentes = True
    for i in range(1, len(conjuntos)):
        if conjuntos[i] != conjuntos[0]:
            son_equivalentes = False
    if son_equivalentes:
        print(" Todos los conjuntos son equivalentes")

    # 2. Ver si todos los conjuntos tienen al menos 5 elementos
    diversidad_alta = True
    for c in conjuntos:
        if len(c) < 5:
            diversidad_alta = False
    if diversidad_alta:
        print(" Alta diversidad numérica (todos tienen al menos 5 elementos)")

    # 3. Ver si no comparten ningún dígito entre todos
    interseccion_total = conjuntos[0].copy()
    for c in conjuntos[1:]:
        interseccion_total &= c
    if len(interseccion_total) == 0:
        print(" Conjuntos totalmente independientes (sin elementos en común)")

    # 4. Ver si hay más conjuntos con cantidad impar de dígitos que pares
    cantidad_impares = 0
    cantidad_pares = 0
    for c in conjuntos:
        if len(c) % 2 == 1:
            cantidad_impares += 1
        else:
            cantidad_pares += 1
    if cantidad_impares > cantidad_pares:
        print(" Etiqueta: grupo impar (más conjuntos con cantidad impar de elementos)")

    # 5. Buscar si algún dígito aparece en todos los conjuntos
    union_total = set().union(*conjuntos)
    for digito in union_total:
        if all(digito in c for c in conjuntos):
            print(f" El dígito {digito} está en todos los conjuntos.")

    return "Evaluación de conjuntos completada."

# ----------------Fin Claudio------------------------
# ---------Comienza Diana-------------------
# Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
# Suma total de los dígitos de cada DNI.

def contar_frecuencia_y_suma(lista_conjuntos):
    for i, conjunto in enumerate(lista_conjuntos):
        dni = ''.join(map(str, conjunto))  # Convertir el conjunto a string
        print("Digitos:", dni)

        frecuencia = {str(i): 0 for i in range(10)}
        suma = 0
        for caracter in dni:
            if caracter.isdigit():
                frecuencia[caracter] += 1
                suma += int(caracter)

        for digito, cantidad in frecuencia.items():
            if cantidad > 0:
                print(" - El dígito", digito, "aparece", cantidad, "veces")

        print(" - Suma total de los dígitos:", suma)
        print()

# ---------Fin Diana-------------------
# ----- Comienza Axel-------------------

def analizar_anios_y_edades():
    anios = []  # Lista de años
    cantidad = int(input("¿Cuántos años de nacimiento desea ingresar?: "))

    for i in range(cantidad):
        anio = int(input(f"Ingrese el año de nacimiento {i + 1}: "))
        anios.append(anio)

    print("Años ingresados:", anios)

    # Contar pares e impares
    pares = contar_pares(anios)
    impares = contar_impares(anios)
    print("Cantidad de pares:", pares)
    print("Cantidad de impares:", impares)

    # Verificar si todos pertenecen al grupo Z
    if all(a > 2000 for a in anios):
        print("Todos pertenecen al grupo Z")
    else:
        print("No todos pertenecen al grupo Z")

    # Años bisiestos
    bisiestos = obtener_bisiesto(anios)
    if bisiestos:
        print("Años bisiestos ingresados:", bisiestos)
    else:
        print("Ninguno nació en un año bisiesto")

    # Calcular edades en 2025
    edades = calcular_edad_actual(anios)
    print("Edades actuales:", edades)

    # Producto cartesiano
    producto = calcular_producto_cartesiano(anios, edades)
    print("Producto cartesiano entre años y edades:")
    for par in producto:
        print(par)

def contar_pares(anios):
    return sum(1 for a in anios if a % 2 == 0)

def contar_impares(anios):
    return sum(1 for a in anios if a % 2 != 0)

def grupo_z (anios):
    if all(a > 2000 for a in anios):
        print(" Todos pertenecen al grupo Z")
    else:
        print(" No todos pertenecen al grupo Z")
#--------Fin Axel ------------------
# ------ Comienzo Yoni-------

    # Función interna para verificar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_bisiesto(anios):
    return [a for a in anios if es_bisiesto(a)]

    # Calcular edades en 2025
def calcular_edad_actual(anios):    
    return [2025 - a for a in anios]
    # print("Edades actuales:", edades)

    # Producto cartesiano
def calcular_producto_cartesiano(anios,edades):    
    return [(a, e) for a in anios for e in edades]

# ----- fin Yoni-------------------

# Funcion MENU para que el usuario seleccione la operacion a realizar
def menu():
    while True:
        print(f"\n{verde}Menú de Opciones{reset}")
        print("1. Unión de conjuntos")
        print("2. Intersección de conjuntos")
        print("3. Diferencia de conjuntos")
        print("4. Diferencia simétrica de conjuntos")
        print("5. Contar frecuencia y suma de dígitos")
        print("6. Evaluar condiciones lógicas de conjuntos")
        print("7. Analizar años de nacimiento")
        print("8. Salir")

        opcion = input(f"{verde}Ingrese la opción deseada: {reset}")

        if opcion == "1" or opcion == "2":
            lista_conjuntos = crear_conjunto_dni()
            print(f"{azul}Conjuntos creados:{reset}", lista_conjuntos)

            if opcion == "1":
                resultado = union_conjuntos(*lista_conjuntos)
                print("Unión de conjuntos:", resultado)
            else:
                resultado = interseccion_conjuntos(*lista_conjuntos)
                print("Intersección de conjuntos:", resultado)
            
        elif opcion == "3" or opcion == "4":
            print('Ingrese el DNI base primero. Los DNI que ingrese luego se restarán de este.')
            conjuntos = crear_conjunto_dni()
            conjunto_base = conjuntos[0] # Tomamos el primer conjunto como conjunto base para la operación
            otros_conjuntos = conjuntos[1:] #Los conjuntos restantes serán los que restaremos o con los que haremos la diferencia simétrica
            if opcion == "3":
                resultado = diferencia_conjuntos(conjunto_base, *otros_conjuntos)
                print(f"Diferencia de conjuntos: {resultado}")
            else:
                resultado = dif_simetrica_conjuntos(conjunto_base, *otros_conjuntos)
                print(f"Diferencia simetrica de conjuntos: {resultado}")

        elif opcion == "5":
            lista_conjuntos = crear_conjunto_dni()
            contar_frecuencia_y_suma(lista_conjuntos)

        elif opcion == "6":
            lista_conjuntos = crear_conjunto_dni()
            print(f"{azul}Conjuntos creados:{reset}", lista_conjuntos)

            resultado4 = evaluar_conjuntos(lista_conjuntos)
            print("Evaluacion Conjuntos:", resultado4)

        elif opcion == "7":
            analizar_anios_y_edades()

        elif opcion == "8":
            print(f"{rojo}Saliendo del programa...{reset}")
            break
        else:
            print(f"{rojo}Opción inválida. Por favor, intente nuevamente.{reset}")

#programa principal 
print(f"{azul}Bienvenido{reset}")
# print(f"{verde}Primero crearemos el conjunto de DNIs{reset}")
menu()
