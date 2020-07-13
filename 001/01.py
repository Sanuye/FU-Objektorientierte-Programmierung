# Übung 01
# bearbeitet von Jasmine Cavael & Alexander Chmielus
# Tutor: Fabian Halama, Übung 10 (Do. 16-18)


import random	# Für den Glücksspieler Aufg. 4

# Aufgabe 1

a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))
c = int(input("Dritte Zahl: "))

if a > b and b > c:
	print("Streng Absteigend")
elif a < b and b < c:
	print("Streng Aufsteigend")
else:
	print("Fluktuierend")


# Aufgabe 2

numList = input("Zahlen durch Leerzeichen getrennt eingeben: ")
list = numList.split()	# Split schreibt die durch Leerzeichen getrennten Strings in eine Liste
pro = 1

for i in list:
	pro*=float(i)			# Die Elemente der Liste sind noch Strings, float wandelt sie in Zahlen um. Kein int, da wir nicht davon ausgegagen sind, dass nur int Zahlen eingegeben wurden
print("Ergebnis: ",pro)

# Aufgabe 3

def weekday(day, month, year):
	y0 = year - ((14-month)//12)
	x = y0+ (y0//4) - (y0//100) + (y0//400)
	m0 = month + (12*((14-month)//12))-2
	num = (day+x+(31*m0//12)) % 7
	if num == 0:
	    name = 'Sonntag'
	elif num == 1:
	    name = 'Montag'
	elif num == 2:
	    name = 'Dienstag'
	elif num == 3:
	    name = 'Mittwoch'
	elif num == 4:
	    name = 'Donnerstag'
	elif num == 5:
	    name = 'Freitag'
	else:
	    name = 'Samstag'
	return name

# Aufgabe 4
# Wir haben die Aufgabenteile a) und b) gleich zusammen gemacht und die jeweiligen Schritte gekennzeichnet
# Desweiteren haben wir auf das anzeigen einzelner Runden (2. Codebeispiel) verzichtet
def gluecksspieler(n):
	turns= 0							# a) Rundenzähler
	current = n							# b) n = bargeld, current zählt aktuelles Geld
	end = "Verloren"					# Endausgabe, wenn verloren
	end2 = ""							# b )Zusatzausgabe, wenn gewonnen
	while current > 0:
		if random.randint(0,1):
			current -= 1				# Verloren, also aktuelles Geld -1
			turns+= 1					# Nach jedem Versuch Zähler erhöhen
		else:
			current += 1 				# Gewonnen, also aktuelles Geld +1
			turns+=1					# Nach jedem Versuch Zähler erhöhen
			if current == 2*n:	# b )Fall: Geld verdoppelt
				end = "Einsatz verdoppelt, Gewonnen: "	# b) Endausgabe, wenn gewonnen
				end2 = current			# b) Gewinn als Zusatzausgabe
				break					# b) Schleife bricht dann ab
	print(end,end2)
	return turns						# a) Rückgabewert = Anzahl der Runden

# Aufgabe 5
def friends(m,n):
	if n!=m and divsum(m) == n and divsum(n) == m:
		return "Befreunet"
	else:
		return "Verfeindet"


def divsum(x):
	sum = 0
	i = 1
	while i <= x/2:
		if x % i == 0:
			sum += i
		i+=1
	return sum
	
# Aufgabe 6

def wind(speed):
	# speed = int(input("Geschwindigkeit eingeben: ")
	if speed < 1:
		return "Windstille"
	elif speed < 4:
		return "leiser Zug"
	elif speed < 7:
		return "leichte Briese"
	elif speed < 11:
		return "schwache Briese"
	elif speed < 16:
		return "mäßige Briese"
	elif speed < 22:
		return "frische Briese"
	elif speed < 28:
		return "starker Wind"
	elif speed < 34:
		return "steifer Wind"
	elif speed < 41:
		return "stürmischer Wind"
	elif speed < 48:
		return "Sturm"
	elif speed < 56:
		return "schwerer Sturm"
	elif speed < 64:
		return "orkanartiger Sturm"
	else:
		return "Orkan"
	

# Testfunktionen (Aufgabe 7)
def test_aufgabe_drei():
	print(weekday(int(input("Tag eingeben: ")),int(input("Monat eingeben: ")), int(input("Jahr eingeben: "))))

def test_aufgabe_vier():
	print("Das ganze hat ",gluecksspieler(int(input("Startgeld eingeben: ")))," Runden gedauert.")
	
def test_aufgabe_fuenf():
	print(friends(int(input("Erste Zahl eingeben: ")),int(input("Zweite Zahl Eingeben: "))))

def test_aufgabe_sechs():
	print(wind(speed = int(input("Geschwindigkeit eingeben: "))))


# Aufrufe Aufgabe 3-6
print("Aufgabe 3:")	
test_aufgabe_drei()
print("Aufgabe 4:")
test_aufgabe_vier()
print("Aufgabe 5:")
test_aufgabe_fuenf()
print("Aufgabe 6:")
test_aufgabe_sechs()
	


input()	# damit Programm nicht aus der cmd verschwindet
