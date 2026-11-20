# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
  print(f"{salutacio} {nom}!")
saludar_a("Marc")
saludar_a("Cristina", "Bon dia")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
  return numero % 2 == 0

print(es_parell(4))  
print(es_parell(7))  

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma / len(numeros)

print(mitjana([10, 20, 30, 40, 50]))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_tot(1, 2))
print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
  for i in range(1, limit + 1):
    print(f"{numero} x {i} = {numero * i}")

taula_multiplicar(3)
taula_multiplicar(5, 3)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")

mostrar_perfil(nom="Anna", edat=19, grau="Enginyeria de Sistemes de Telecomunicació")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
  resultat = 1
  comptador = 1
  while comptador <= n:
    resultat *= comptador
    comptador += 1
  return resultat

def maxim(numeros):
  valor_maxim = numeros[0]
  for numero in numeros:
    if numero > valor_maxim:
      valor_maxim = numero
  return valor_maxim

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
  vocals = "aeiouàèéíòóúïü"
  comptador = 0
  for lletra in text.lower():
    if lletra in vocals:
      comptador += 1
  return comptador

print(f"Vocals a 'Hola Món': {comptar_vocals('Hola Món')}")  
print(f"Vocals a 'Enginyeria': {comptar_vocals('Enginyeria')}")  

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
  min_val = numeros[0]
  max_val = numeros[0]
  for numero in numeros[1:]:
    if numero < min_val:
      min_val = numero
    if numero > max_val:
      max_val = numero
  return min_val, max_val

val_min, val_max = minim_i_maxim([15, 3, 42, 8, 23, 4])
print(f"El mínim és {val_min} i el màxim és {val_max}")

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
  text_net = text.lower()
  return text_net == text_net[::-1]

print(es_palindrom("radar"))  
print(es_palindrom("Anna"))   
print(es_palindrom("Python"))