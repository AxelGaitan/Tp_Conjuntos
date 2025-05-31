
#Operaciones con el dni ingresado del usuario
#Generar conjuntos de digitos
#Conteo de frecuencia de cada digito por DNI
#Suma total de los digitos de cada DNI.
#Evaluacion de condiciones

#OPERACION CON LOS AÑOS de nacimiento   --> Axel
años =[]
cantidad =int(input("diga cuantos años de nacimiento quiere ingresar?: "))

for i in range (cantidad):
    anio = int(input(f"ingresa el año de nacimiento {i+1}: "))
    años.append(anio)

print("años ingresados:", años)

pares = sum( 1 for a in años if a % 2 == 0)
impares = len(años) - pares 
print("Cantidad de pares: ", pares)
print("cantidad de impares: ", impares)

if all (a > 2000 for a in años):
    print("todos pertenecen al grupo Z")
else:
    print("no todos pertenecen al grupo Z")

# Nueva funcionalidad: determinar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Ver si alguno nació en año bisiesto
if any(es_bisiesto(a) for a in años):
    print("Tenemos un año especial")
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
