# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tècnic=input("nom del tècnic:")
xarxa=input("nom de la xarxa:")
print(f"el nom del tècnic és: {tècnic}; i el nom de la xarxa és: {xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_enllaç=float(input("longitud d'un enllaç de fibra en km:"))
velocitat_transmissió=float(input("velocitat de transmissió en Gbps"))
temps=8/velocitat_transmissió
print(f"segons que caldrien: {temps}")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina=float(input("hores de feina:"))
preu_instalació=float(input("preu per hora:"))
preu_material=float(input("preu del material:"))
cost=hores_feina*preu_instalació+preu_material
print(f"el preu total és:{cost}")