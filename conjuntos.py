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





#ver si todos nacieron despues del 2000
#ver si alguno nacio en año bisiesto





