# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("Ejercicio 1: Determinar el mayor de dos números enteros \n")
numero1 = int(input("Introduce el primer numero: \n"))
numero2 = int(input("Introduce el segundo numero: \n"))

if numero1 > numero2:
    print(f"numero mayor {numero1}")
elif numero1 == numero2:
    print("Numeros iguales")
else:
    print(f"numero mayor: {numero2}")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("Ejercicio 2: calculadora simple \n")
numero21 = int(input("introduce el primer numero \n"))
numero22 = int(input("introduce el segundo numero \n"))
operacion = input("introduce la operacion a realizar \n")

if operacion == "+":
    resultado = numero21 + numero22
    print(f"operacion: {numero21} + {numero22}", f"resultado: {numero21 + numero22}")
if operacion == "-":
    print(f"operacion: {numero21} - {numero22}", f"resultado: {numero21 - numero22}")
if operacion == "*":
    print(f"operacion: {numero21} * {numero22}", f"resultado: {numero21 * numero22}")
if operacion == "/":
    if numero22 == 0:
        print("No se puede dividir entre 0")
    else: 
        print(f"operacion: {numero21} / {numero22}", f"resultado: {numero21 / numero22}")

if "resultado" in locals():  # Comprueba si la variable resultado existe.
    print(f"el resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
anio = int(input("\n Introduce el año: \n"))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es bisiesto")
elif ():
    print("No es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\n Ejercicio 4: categorizar edad \n")

while True:
    edad = int(input("Introduce una edad: "))
    if ( 0 <= edad <= 2):
        print("Bebe")
    elif (3 <= edad <= 12):
        print("Niño")
    elif (13 <= edad <= 17):
        print("Adolecente")
    elif (18 <= edad <= 64):
        print("Adulto")
    elif ( edad > 64):
        print("Adulto mayor...")
    if edad == -1: break


    
