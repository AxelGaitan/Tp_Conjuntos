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
def interseccion_conjuntos(*conjuntos): # Usamos * para recibir cualquier cantidad de conjuntos.
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

def contar_frecuencia_y_suma():
    dnis = []
    cantidad_dnis = int(input("Ingrese la cantidad de DNIs a procesar: "))
    res_dig = ""
    res_suma = "" 
    
    for i in range(cantidad_dnis):
        dni = input("Ingresá el DNI número " + str(i+1) + ": ")
        dnis.append(dni)
    
    for dni in dnis:
        suma = 0  # Acumulador para sumar los dígitos
        print("DNI:", dni)
        
        frecuencia = {str(i): 0 for i in range(10)}
        
        for caracter in dni:
            if caracter.isdigit():  
                frecuencia[caracter] += 1  
                suma += int(caracter)  
        
        for digito, cantidad in frecuencia.items():
            if cantidad > 0:
                res_dig=print(" - El dígito", digito, "aparece", cantidad, "veces")
        
        res_suma=print(" - Suma total de los dígitos:", suma)
        
    
    return res_dig,res_suma

#contar_frecuencia_y_suma()

############################################
#####  MENU - DIANA

def menu_operaciones():
    while True:
        print("\nMenú de Operaciones")
        print("1. Crear conjunto de DNIs")
        print("2. Unión de conjuntos")
        print("3. Intersección de conjuntos")
        print("4. Diferencia de conjuntos")
        print("5. Diferencia simétrica de conjuntos")
        print("6. Contar frecuencia y suma de dígitos")
        print("7. Salir")
        
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "1":
            crear_conjunto_dni()
        elif opcion == "2":
            conjuntos = pedir_conjuntos()
            union_conjuntos(*conjuntos)
        elif opcion == "3":
            conjuntos = pedir_conjuntos()
            interseccion_conjuntos(*conjuntos)
        elif opcion == "4":
            conjunto_base = pedir_conjunto_base()
            otros_conjuntos = pedir_otros_conjuntos()
            diferencia_conjuntos(conjunto_base, *otros_conjuntos)
        elif opcion == "5":
            conjunto_base = pedir_conjunto_base()
            otros_conjuntos = pedir_otros_conjuntos()
            dif_simetrica_conjuntos(conjunto_base, *otros_conjuntos)
        elif opcion == "6":
            contar_frecuencia_y_suma()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

def pedir_conjuntos():
    # Función para pedir conjuntos al usuario
    pass

def pedir_conjunto_base():
    # Función para pedir el conjunto base al usuario
    pass

def pedir_otros_conjuntos():
    # Función para pedir otros conjuntos al usuario
    pass

menu_operaciones()