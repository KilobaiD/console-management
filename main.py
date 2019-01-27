import mysql.connector
import sys

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

#Remove this comment

print("QUERIED_DATA_OUTPUT ")
for users in resultUsers:
	usernameq = users[0]
	passwordq = users[1]

	print(usernameq + "@" + passwordq + "\n")
#Define basic password
passwordinterested = "alexandru"

def printMenu():
	print (30 * "-" + "MENIU" + 30 * "-")
	print("1. Afiseaza toate anunturile")
	print("2. Afiseaza toti utilizatorii")
	print("3. Iesire")
	print (65 * "-")

def subMenuAnnouncements():
	annoMenuChoice = input("Scrie 'show' pentru a afisa toate anunturile: ")
	if annoMenuChoice == "show":
			queryElements = "SELECT * FROM smsys_announcements"
			cursor.execute(queryElements)
			resultAnnouncements = cursor.fetchall()
			for announcements in resultAnnouncements:
				print("\nTitlu: " + announcements[1])
				print("Message: " + announcements[2] + "\n")

def subMenuExit():
	print("\nAi parasit aplicatia cu succes!")
	sys.exit()

questionInput = input("Ai deja cont pe aplicatie? y/n: ")
if questionInput == "y":
	usernameInput = input("Introdu numele de utilizator: ")
	passwordInput = input("Introdu parola: ")
	if usernameInput == usernameq and passwordInput == passwordinterested:
		print("\nBine ai revenit " + usernameInput + "\n")
		menuLoop = True
		while menuLoop:
			printMenu()
			menuChoice = input("Alege o intrare din meniu [1-3]: ")
			if menuChoice == "1":
				print("\nMeniul 1 a fost selectat. Aici sunt afisate toate anunturile\n")
				subMenuAnnouncements()
			elif menuChoice == "2":
				print("\nMeniul 2 a fost selectat. Aici sunt afisati toti utilizatorii\n")
			elif menuChoice == "3":
				subMenuExit()
			else: 
				print("\nAlegerea facuta este incorecta. Te rugam sa reincerci din nou!\n")
	else:
		print("Username sau parola incorecte! Reincearca din nou!")
elif questionInput == "n":
	print("Momentan aplicatiile sunt inchise. Incarca alta data!")			
else:
	print("Alegerea facuta este invalida te rugam sa incerci mai tarziu")			


