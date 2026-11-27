# Exercici 1 - Bàsic. Magnitud d'una mesura
# Importa math amb l'àlies matematiques. Calcula el mòdul d'un vector de
# components x i y amb sqrt(x * x + y * y).
# Entrada: x = 3.0, y = 4.0. Sortida esperada: 5.0.
# Cas límit: x = 0.0, y = 0.0 ha de donar 0.0.
x = 3.0
y = 4.0
# TODO: escriu les importacions i els càlculs.
import math as matematiques
modul = matematiques.sqrt(x * x + y * y)        modul = matematiques.sqrt(x * x + y * y)   

# Exercici 2 - Bàsic. Conversions reutilitzables
# Importa conversions amb l'àlies conv i utilitza les seves funcions.
# Converteix cada temperatura a kelvins i cada tensió a volts.
# Entrades següents. Sortides esperades en el mateix ordre:
# [263.15, 273.15, 298.15] i [0.0, 3.3, 5.0].
# Amb una llista buida, el resultat corresponent ha de ser [].
temperatures = [-10.0, 0.0, 25.0]
tensions_mv = [0, 3300, 5000]
# TODO: obtén i mostra dues llistes amb les conversions.
import conversions as conv
temperatures_kelvins = [conv.celsius_a_kelvin(t) for t in temperatures]
tensions_volts = [conv.milivolts_a_volts(v) for v in tensions_mv]       