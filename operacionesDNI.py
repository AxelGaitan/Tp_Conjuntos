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
