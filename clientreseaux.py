import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


nombre_1=input("premierchiffre")
connexion_avec_serveur.send(nombre_1.encode())

nombre_2=input("deuxieme chiffre")
connexion_avec_serveur.send(nombre_2.encode())

symbole=input("symbole")
connexion_avec_serveur.send(symbole.encode())

print(connexion_avec_serveur.recv(1).decode())
print("Fermeture de la connexion")
connexion_avec_serveur.close()