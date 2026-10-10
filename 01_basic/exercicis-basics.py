print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
nom="Alejandro" 
ciutat="Barcelona"
print(nom)
print(ciutat)
print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí
print(type(a)) 
print(type(b)) 
print(type(c)) 
print(type(d)) 
print(type(e))
print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
cadena = "12345"
nombre_enter = int(cadena)  # Converteix la cadena a enter
nombre_decimal = float(nombre_enter)  # Converteix l'enter a nombre decimal

print("Nombre enter:", nombre_enter)
print("Nombre decimal:", nombre_decimal)

decimal_original = 3.99
enter_convertit = int(decimal_original) # s'elimina la part decimal
print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí
nom = "Alejandro"
edat = 18
alcada = 1.83
print(f"Em dic {nom}, tinc {edat}, i faig {alcada} metres")
print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")
resultat=int(round((3.14159)/2))

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
celsius=float(input("introdueix temperatura en graus celsius:"))
fahrenheit = (celsius * 9 / 5) + 32
print(f"el valor en celsius és: {celsius}")
print(f"el valor en fahrenheit és: {fahrenheit}")
print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
total_compte=float(input("total del compte"))
percentatge_propina=float(input("percentatge de propina"))
propina=total_compte*(percentatge_propina/100)
total_final=total_compte+propina
print(f"la propina és: {propina:.2f} i el total a pagar és: {total_final:.2f}")
print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
contrasenya=input("escriu contrasenya:")
if len(contrasenya)>= 8:
    print("Contrasenya vàlida")
else: 
    print("Contrasenya no vàlida")