# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num1 = float(input("introdueix nombre: "))
num2 = float(input("introdueix nombre: "))
if num1 > num2:
    print(f"{num1} és més gran que {num2}")
elif num1 < num2:
    print(f"{num2} és més gran que {num1}")
else:
    print(f"son iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
num1 = float(input("introdueix nombre: "))
num2 = float(input("introdueix nombre: "))
operacio = input("introdueix la operacio(+, -, *, /):").strip()

if operacio == "/" and num2 == 0:
    print("error no es por dividir per zero")
elif operacio == "+":
    resultat = num1 + num2
    print(f"El resultat es {resultat}")
elif operacio == "-":
    resultat = num1 - num2
    print(f"El resultat és: {resultat}")
elif operacio == "*":
    resultat = num1 * num2
    print(f"El resultat és: {resultat}")
elif operacio == "/":
    resultat = num1 / num2
    print(f"El resultat és: {resultat}")
else:
    print("Operació no vàlida.")


# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
any = int(input("introdueix un any:"))
if any % 4 == 0 and any % 100 != 0:
    print(f"{any} és de traspàs")
elif any % 400== 0:
    print(f"{any} és de traspàs")
else:
    print(f"{any} no és de traspàs")



# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)
edat = int(input("Introdueix una edat: "))
if 0 <= edat <= 2:
    print("Nadó")
elif 3 <= edat <= 12:
    print("Infant")
elif 13 <= edat <= 17:
    print("Adolescent")
elif 18 <= edat <= 64:
    print("Adult")
elif edat >= 65:
    print("Persona gran")
else:
    print("Edat no vàlida.")


# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
rssi = float(input("Introdueix el nivell de senyal RSSI en dBm: "))

if rssi >= -50:
    print("Cobertura excel·lent.")
elif rssi >= -67:
    print("Cobertura bona.")
elif rssi >= -75:
    print("Cobertura feble.")
else:
    print("Cobertura molt feble.")


# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia_optica = float(input("Introdueix la potencia optica en dBm:"))
if -27<=potencia_optica<=-8:
    print("Nivell acceptable")
elif potencia_optica<-27:
    print("Nivell massa baix")
else:
    print("Nivell massa alt")



# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum_gb = float(input("Introdueix el consum mensual de dades en GB: "))

if consum_gb <= 20:
    print("El consum està dins del límit de 20 GB.")
else:
    extra_gb = consum_gb - 20
    print(f"S'ha superat el límit en {extra_gb:.2f} GB.")


# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los_encès = input("L'indicador LOS està encès? (s/n): ").strip().lower()
internet_encès = input("L'indicador d'Internet està encès? (s/n): ").strip().lower()

if los_encès == "s":
    print("Cal revisar el cable de fibra.")
elif internet_encès != "s":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
percentatge_de_bateria = float(input("Introdueix el percentatge de bateria: "))

if percentatge_de_bateria < 0 or percentatge_de_bateria > 100:
    print("Error: el valor ha d'estar entre 0 i 100")
elif percentatge_de_bateria < 20:
    print("El nivell és crític")
elif percentatge_de_bateria <= 49:
    print("El nivell és baix")
else:
    print("El nivell és suficient")


# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix latencia en mil·lisegons: "))
paquets_perduts = float(input("percentatge de paquets perduts: "))

if latencia < 0 or paquets_perduts < 0 or paquets_perduts > 100:
    print("parametres no valids")
elif latencia <= 30 and paquets_perduts <= 1:
    print("Excel·lent")
elif latencia <= 80 and paquets_perduts <= 3:
    print("Bona")
elif latencia <= 150 and paquets_perduts <= 5:
    print("Acceptable")
else:
    print("Deficient")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
tipus_de_pla = input("tipus de pla: (basic/plus)").strip().lower()
consum_mensual = float(input("consum mensual en GB: "))

if consum_mensual < 0:
    print("El consum no pot ser negatiu")
elif tipus_de_pla == "basic":
     cost = 10
     if consum_mensual > 10:
        cost = (consum_mensual - 10) * 1.50
elif tipus_de_pla == "plus":
     cost = 20
     if consum_mensual > 30:
         cost = (consum_mensual - 30) * 0.75
else:
    print("pla mensual desconegut")
         

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.



# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.