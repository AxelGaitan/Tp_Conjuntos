
#Operaciones con el dni ingresado del usuario
#Generar conjuntos de digitos
#Conteo de frecuencia de cada digito por DNI
#Suma total de los digitos de cada DNI.
#Evaluacion de condiciones

#OPERACION CON LOS AÑOS de nacimiento   --> Axel
años = []
cantidad = int(input("¿Cuántos años de nacimiento desea ingresar?: "))

for i in range(cantidad):
    anio = int(input(f"Ingrese el año de nacimiento {i + 1}: "))
    años.append(anio)

print("Años ingresados:", años)

pares = sum(1 for a in años if a % 2 == 0)
impares = len(años) - pares
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)

if all(a > 2000 for a in años):
    print("Todos pertenecen al grupo Z")
else:
    print("No todos pertenecen al grupo Z")

# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

# Ver si alguno nació en un año bisiesto
bisiestos = [a for a in años if es_bisiesto(a)]
if bisiestos:
    print("Tenemos un año especial. Años bisiestos ingresados:", bisiestos)
else:
    print("Ninguno nació en un año bisiesto")

# Calcular edades actuales (año actual: 2025)
edades = [2025 - a for a in años]
print("Edades actuales:", edades)

# Producto cartesiano entre años y edades
producto_cartesiano = [(a, e) for a in años for e in edades]
print("Producto cartesiano entre años y edades:")
for par in producto_cartesiano:
    print(par)
