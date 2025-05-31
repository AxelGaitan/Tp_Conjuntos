from colorama import Fore,Style,init

#Definimos colores
rojo=Fore.RED
verde=Fore.GREEN
azul=Fore.BLUE
reset=Style.RESET_ALL


#Funcion para crear conjuntos a partir de DNIs ingresados por el usuario
def crear_conjunto_dni (): #No recibe parametros
    lista_conjuntos = [] #Lista vacia para almacenar los conjuntos
    while True:
        x = input ('Por favor, ingresá los DNI sin puntos ni espacios (o escribí "fin" para terminar): ') #Pide al usuario los DNI
        if x.lower() == 'fin': #Convertimos el str x en minuscula
            break #Se detiene el bucle
        elif x.isdigit():  #verifica si la cadena de texto contiene únicamente caracteres numéricos
            conjunto = {int(digito) for digito in x}
            lista_conjuntos.append(conjunto) #Agregamos conjunto a la lista
        else:
            print('Entrada inválida. Ingresá sólo números, sin puntos ni espacios.') #En caso de que no contenga únicamente solo caracteres numéricos
    return lista_conjuntos        

#Funcion para calcular y visualización de la unión de n conjuntos 
def union_conjuntos(*conjuntos): # Usamos * para recibir cualquier cantidad de conjuntos.
    resultado = set() #Conjunto vacio para almacenar el resultado
    for conjunto in conjuntos:
        resultado |= conjunto #modifica el conjunto resultado agregandole todos los elementos del conjunto
    return resultado 

#Funcion para calcular y visualización de la intersección de n conjuntos 
def interseccion_conjuntos_1(*conjuntos): # Usamos * para recibir cualquier cantidad de conjuntos.
    resultado = set() #Conjunto vacio para almacenar el resultado
    for conjunto in conjuntos:
        resultado &= conjunto #modifica el conjunto resultado conservando solo los elementos en común entre los conjuntos
    return resultado 

#Funcion para calcular y visualización de la intersección de n conjuntos 
def interseccion_conjuntos(*conjuntos): # Usamos * para recibir cualquier cantidad de conjuntos.
    if not conjuntos: #Verifica si no se pasó ningún conjunto.
        return set () #Retornamos un conjunto vacio 
    else:
        resultado = conjuntos[0].copy() #Usamos el primer conjunto de la lista como base para la intersección.
        for conjunto in conjuntos[1:]: #Tomamos todos los conjuntos menos el primero
            resultado &= conjunto #modifica el conjunto resultado 
    return resultado

#Funcion para calcular y visualización de las diferencias de n conjuntos 
def diferencia_conjuntos(conjunto_base, *otros_conjuntos): # Usamos * para recibir cualquier cantidad de conjuntos.
    resultado = conjunto_base.copy() #Creamos una copia del conjunto que vamos usar como base para no modificar el original
    for conjunto in otros_conjuntos:
        resultado -= conjunto #modifica el conjunto resultado eliminando todos los elementos que estén en conjunto.
    return resultado

#Funcion para calcular y visualización de la diferencia simétrica  de n conjuntos 
def dif_simetrica_conjuntos(conjunto_base, *otros_conjuntos): # Usamos * para recibir cualquier cantidad de conjuntos.
    resultado = conjunto_base.copy() #Creamos una copia del conjunto que vamos usar como base para no modificar el original
    for conjunto in otros_conjuntos:
        resultado ^= conjunto #modifica el conjunto resultado eliminando todos los elementos que estén en conjunto.
    return resultado


#Prueba de las funciones (ESTA PARTE SE DESCARTA)

# conjunto_dni = crear_conjunto_dni()
# print(conjunto_dni)    


# a = {1,2,3}
# b= {3,1,5,6,7}

# c = union_conjuntos(a,b)
# d = interseccion_conjuntos(a,b)
# e = diferencia_conjuntos(a,b)
# f = dif_simetrica_conjuntos(a,b)

# print (c)
# print(d)
# print(e)
# print(f)

# -----------------------------------------------------------------------------------------------

# DIANA 
#
# Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
# Suma total de los dígitos de cada DNI.

def contar_frecuencia_y_suma(lista_conjuntos):
    for i, conjunto in enumerate(lista_conjuntos):
        dni = ''.join(map(str, conjunto))  # Convertir el conjunto a string
        print("DNI:", dni)
        
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

# Llamar a las funciones
# lista_conjuntos = crear_conjunto_dni()
# contar_frecuencia_y_suma(lista_conjuntos)


############################################
#####  MENU - DIANA

print(f"{azul}Bienvenido{reset}")
print(f"{verde}Primero crearemos el conjunto de DNIs{reset}")
lista_conjuntos=crear_conjunto_dni()
print(f"{azul}Conjuntos creados:{reset}", lista_conjuntos)

def menu():
    while True:
        print(f"\n{verde}Menú de Opciones{reset}")
        print("1. Unión de conjuntos")
        print("2. Intersección de conjuntos")
        print("3. Diferencia de conjuntos")
        print("4. Diferencia simétrica de conjuntos")
        print("5. Contar frecuencia y suma de dígitos")
        print("6. Salir")
        
        opcion = input(f"{verde}Ingrese la opción deseada: {reset}")
        
        if opcion == "1":
            num_conjuntos = int(input("Ingrese el número de conjuntos a unir: "))
            conjuntos = []
            for i in range(num_conjuntos):
                conjunto = input(f"Ingrese el conjunto {i+1} (separado por comas): ")
                conjunto = {int(x) for x in conjunto.split(',')}
                conjuntos.append(conjunto)
            print("Unión de conjuntos:", union_conjuntos(*conjuntos))
        elif opcion == "2":
            num_conjuntos = int(input("Ingrese el número de conjuntos a intersectar: "))
            conjuntos = []
            for i in range(num_conjuntos):
                conjunto = input(f"Ingrese el conjunto {i+1} (separado por comas): ")
                conjunto = {int(x) for x in conjunto.split(',')}
                conjuntos.append(conjunto)
            print("Intersección de conjuntos:", interseccion_conjuntos(*conjuntos))
        elif opcion == "3":
            conjunto_base = input("Ingrese el conjunto base (separado por comas): ")
            conjunto_base = {int(x) for x in conjunto_base.split(',')}
            num_otros_conjuntos = int(input("Ingrese el número de otros conjuntos: "))
            otros_conjuntos = []
            for i in range(num_otros_conjuntos):
                conjunto = input(f"Ingrese el conjunto {i+1} (separado por comas): ")
                conjunto = {int(x) for x in conjunto.split(',')}
                otros_conjuntos.append(conjunto)
            print("Diferencia de conjuntos:", diferencia_conjuntos(conjunto_base, *otros_conjuntos))
        elif opcion == "4":
            conjunto_base = input("Ingrese el conjunto base (separado por comas): ")
            conjunto_base = {int(x) for x in conjunto_base.split(',')}
            num_otros_conjuntos = int(input("Ingrese el número de otros conjuntos: "))
            otros_conjuntos = []
            for i in range(num_otros_conjuntos):
                conjunto = input(f"Ingrese el conjunto {i+1} (separado por comas): ")
                conjunto = {int(x) for x in conjunto.split(',')}
                otros_conjuntos.append(conjunto)
            print("Diferencia simétrica de conjuntos:", dif_simetrica_conjuntos(conjunto_base, *otros_conjuntos))
        elif opcion == "5":
            lista_conjuntos = crear_conjunto_dni()
            contar_frecuencia_y_suma(lista_conjuntos)
        elif opcion == "6":
            print(f"{rojo}Saliendo del programa...{reset}")
            break
        else:
            print(f"{rojo}Opción inválida. Por favor, intente nuevamente.{reset}")

menu()