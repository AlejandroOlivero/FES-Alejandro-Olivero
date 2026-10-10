# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador="Router oficina"
ubicació="oficina director"
nombre_de_ports=8
encaminador_encès=True
print(f"Encaminador: {nom_encaminador}; Ubicació: {ubicació}; Ports: {nombre_de_ports}; Encès: {encaminador_encès}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_inclosos= 15 
gb_consumits=6
gb_totals=gb_inclosos-gb_consumits
print("GB que queden:", gb_totals)

gb_consumits=5
gb_totals=gb_inclosos-gb_consumits
print("GB que queden:", gb_totals)