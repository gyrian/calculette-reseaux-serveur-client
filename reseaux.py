import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

nombre_1 =connexion_avec_client.recv(1).decode()

nombre_2=connexion_avec_client.recv(1).decode()
operation=connexion_avec_client.recv(1).decode()





if operation=="+":
	connexion_avec_client.send(str(int(nombre_1) + int(nombre_2)).encode())
elif operation=="-":
	connexion_avec_client.send(str(int(nombre_1)-int(nombre_2)).encode())
elif operation=="*":
	connexion_avec_client.send(str(int(nombre_1)*int(nombre_2)).encode())
elif operation=="/":
	connexion_avec_client.send(str(int(nombre_1)/int(nombre_2)).decode())


print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()