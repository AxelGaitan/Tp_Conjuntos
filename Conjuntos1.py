# Paso 1: Ingreso de DNI
# Solicitamos al usuario que ingrese 3 DNI
dnis = []
for i in range(3):  # Se puede cambiar el número 3 para pedir más o menos DNI
    dni = input("Ingresá el DNI número " + str(i+1) + ": ")
    dnis.append(dni)  # Guardamos cada DNI en la lista 'dnis'

# Paso 2: Crear conjuntos con los dígitos únicos de cada DNI
# si el DNI es "123123", el conjunto será {'1', '2', '3'}
conjuntos = []
for dni in dnis:
    conjunto = set()  # Se creea un conjunto vacío
    for digito in dni:
        # Agregamos cada dígito solo una vez por ser conjunto
        conjunto.add(digito)
    # Guardamos el conjunto en la lista de conjuntos
    conjuntos.append(conjunto)

# Mostramos los conjuntos generados
print(" Conjuntos generados ")
for i in range(len(conjuntos)):
    print("Conjunto", i+1, ":", conjuntos[i])

# Paso 3: Operaciones básicas entre conjuntos entre el primero y el segundo
# Unión: todos los dígitos que están en A o B
# Intersección: los que están en A y también en B
# Diferencia: los que están en A pero no en B, y viceversa
union = conjuntos[0] | conjuntos[1]
interseccion = conjuntos[0] & conjuntos[1]
diferencia_ab = conjuntos[0] - conjuntos[1]
diferencia_ba = conjuntos[1] - conjuntos[0]

print(" Operaciones entre A y B ")
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia A - B:", diferencia_ab)
print("Diferencia B - A:", diferencia_ba)

# Paso 4: Contar cuántas veces aparece cada dígito en cada DNI
# También sumamos todos los dígitos de cada DNI
print(" Frecuencia y suma de dígitos ")
for dni in dnis:
    suma = 0  # Acumulador para sumar los dígitos
    print("DNI:", dni)
    for digito in "0123456789":  # Recorremos todos los dígitos posibles
        cantidad = 0  # Contador para el dígito actual
        for caracter in dni:
            if caracter == digito:
                cantidad += 1  # Si el dígito aparece, aumentamos el contador
                # También lo sumamos (de texto a número con int)
                suma += int(digito)
        if cantidad > 0:
            print(" - El dígito", digito, "aparece", cantidad, "veces")
    print(" - Suma total de los dígitos:", suma)

# Paso 5: Evaluación de condiciones lógicas con 'if'
print(" Evaluación de condiciones lógicas ")

# 1. Ver si todos los conjuntos tienen los mismos elementos
# Comparamos todos con el primero
son_equivalentes = True
for i in range(1, len(conjuntos)):
    if conjuntos[i] != conjuntos[0]:
        son_equivalentes = False
if son_equivalentes:
    # Todos tienen los mismos dígitos
    print("Todos los conjuntos son equivalentes")

# 2. Ver si todos los conjuntos tienen al menos 5 elementos
diversidad_alta = True
for c in conjuntos:
    if len(c) < 5:
        diversidad_alta = False
if diversidad_alta:
    # Todos tienen bastante variedad de dígitos
    print("Alta diversidad numérica")

# 3. Ver si no comparten ningún dígito intersección vacía entre todos
interseccion_total = conjuntos[0]
for c in conjuntos[1:]:
    # Intersección acumulada entre todos
    interseccion_total = interseccion_total & c
if len(interseccion_total) == 0:
    print("Conjuntos totalmente independientes")  # No tienen dígitos en común

# 4. Ver si hay más conjuntos con cantidad impar de dígitos que pares
cantidad_impares = 0
cantidad_pares = 0
for c in conjuntos:
    if len(c) % 2 == 1:  # Si el tamaño del conjunto es impar
        cantidad_impares += 1
    else:  # Si el tamaño del conjunto es par
        cantidad_pares += 1
if cantidad_impares > cantidad_pares:
    print("Etiqueta: grupo impar")  # Hay más conjuntos impares que pares

# 5. Buscar si algún dígito aparece en todos los conjuntos
for digito in union:  # Recorremos los dígitos de la unión entre A y B
    esta_en_todos = True
    for c in conjuntos:
        if digito not in c:
            esta_en_todos = False
    if esta_en_todos:
        print("El dígito", digito, "está en todos los conjuntos.")  # Dígito común
