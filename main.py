import mysql.connector
import time

#time.sleep(1)
myDatabase = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "smsys_db"
)
cursor = myDatabase.cursor()

queryUser = "SELECT username, password FROM smsys_users WHERE user_ID = 1"
cursor.execute(queryUser)
resultUsers = cursor.fetchall()

print("Queried Data: ")
for users in resultUsers:
	usernameq = users[0]
	passwordq = users[1]

	print(usernameq + "@" + passwordq)

passwordinterested = "alexandru"
choiceInput = raw_input("\n Ai deja un cont? y/n: ")
if choiceInput == "y": 
	print("Bine ai revenit in sistem! Trebuie sa te autentifici")
	usernameInput = raw_input("Introdu numele de utilizator: ")
	passwordInput = raw_input("Introdu parola aici: ")
	if usernameInput == usernameq and passwordInput == passwordinterested:
		print("Te-ai autentificat cu succes in sistem!\n")
		newCmd = raw_input("Scrie 'show' pentru a arata tot ce este in registru: ")
		if newCmd == "show":
			queryElements = "SELECT * FROM smsys_announcements"
			cursor.execute(queryElements)
			resultAnnouncements = cursor.fetchall()

			for announcements in resultAnnouncements:
				print("\nTitlu: " + announcements[1])
				print("Message: " + announcements[2])
	else:
		print("Username sau parola gresit!")

raw_input("\n Apasa orice tasta pentru a termina...")
myDatabase.close()
