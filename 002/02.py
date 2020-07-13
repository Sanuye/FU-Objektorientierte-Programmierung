# Übung 02
# bearbeitet von Jasmine Cavael & Alexander Chmielus
# Tutor: Fabian Halama, Übung 10 (Do. 16-18)

import random
import time
import turtle as t

# Aufgabe 1
# Der Ansatz ist, dass die n-te Mersennezahl genau n Einsen besitzt. Wir müssen also n Stellen mit 1 besetzen.
# Um das zu realisieren muss die zahl (mer) die mit Eins initialiert ist, um eine Stelle nach links verschoben und die dadurch entstehende 0 am Ende des Bitstrings mit 1 verodert werden
# Das ganze geht so lange, bis die Zahl größer als 2^(n-1) ist, da sie dann die richtige Anzahl an Einsen hat. (Lässt sich leicht nachrechnen)
def mersenne(n):
    help_mer = 1 << n			# = 1 * 2^n = 2^n
    help_mer = help_mer >> 1	# = 2 ^(n-1). Das ganze so umständlich, da (n-1) laut Aufgabe nicht erlaubt ist (denke ich zumindest).
    mer = 1
    while mer < help_mer:		
        mer = mer << 1
        mer = mer | 1
    return mer



# Aufgabe 2
def repeats(m,n):
	help_list = []
	end_list = []
	for i in range(0,m):			# Bei range ist m exklusiv, aber die 0 inklusiv - wir haben also genau m generierte Zufallszahlen...
		a = random.randint(0, n)	# ...die >= 0 und <= n sind. (Wir gehen davon aus, dass 0 und n auch dazugehören, ist nicht deutlich formuliert in der Aufgabe)
		help_list.append(a)			# Diese werden in einer Hilfsliste gespeichert
	# print(help_list), einfach Kommentar löschen, wenn man die Hilfsliste sehen möchte.
	for j in range(0,n+1):			# Jetzt brauchen wir für jede mögliche Zufallszahl eine Zelle in der Liste, die Ausgegeben wird. Da Range exklusiv ist, haben wir genau 0 bis einschließlich n Elemente
		end_list.append(0)			# Diese Initialisieren wir mit 0.
	for k in help_list:
		end_list[k] +=1				# Wann immer wir nun eine Zahl in der Hilfsliste lesen, wird genau diese Stelle um 1 erhöht.
	return end_list

def dic_repeats(m,n):				# Analog mit Dictionaries
	help_list = []
	end_dic = {}
	for i in range(0, m):
		a = random.randint(0, n)
		help_list.append(a)
	# print(help_list)
	for j in range(0, n+1):
		end_dic[j] = 0
	for k in help_list:
		end_dic[k] += 1
	return(end_dic)
		


# Aufgabe 3
# Zuerst kommen die 4 Funktionen aus den Folien

def linear_search_it(key, seq):
	for i in seq:
		if i == key:
			return True
	return False
	
def linear_search_rek(key, seq):
	for i in seq:
		if i == key:
			return True
	return False

def bin_search_rek(key,seq):
	if len(seq)>1:
		m = len(seq)//2
		if seq[m]==key:
			return True
		elif key<seq[m]:
			return bin_search_rek(key, seq[0:m])
		else:
			return bin_search_rek(key, seq[(m+1):])
	elif len(seq)==1:
		return seq[0]==key
	else:
		return False

def bin_search_it (nums, key):
	lowerBound = 0
	upperBound = len(nums) - 1
	while lowerBound <= upperBound:
		current = (lowerBound + upperBound)//2
		if nums[current] == key:
			return True
		else:
			if nums[current] < key:
				lowerBound = current + 1
			else:
				upperBound = current - 1
	
	return False
	
# Testprogramm

def test_searches():
	nums = list(range(1,501))		# Liste mit den zahlen 1 bis 500(sortiert).
	keys = []						# Liste mit 1.000 zufälligen Zahlen.
	for i in range(0,1000):				
		a = random.randint(1,1001)	# Wir nehmen Zahlen zwischen 1 und 1000 damit auch Zahlen vorkommen können, die nicht in der Liste sind.
		keys.append(a)
		
	start1 = time.time()											# Zeit vor der Ausführung
	for x in keys:
		linear_search_it(x, nums)
	end1 = time.time()												# Zeit nach der Ausführung
	print("Zeit der iterativen linearen Suche: ",end1 - start1)		# Ausgabe der Differenz
	
	start2 = time.time()
	for x in keys:
		(linear_search_rek(x, nums))
	end2 = time.time()
	print("Zeit rekursiven linearen Suche: ",end2 - start2)
	
	start3 = time.time()
	for x in keys:
		(bin_search_rek(x, nums))
	end3 = time.time()
	print("Zeit der rekursiven Binärsuche: ",end3 - start3)
	
	start4 = time.time()
	for x in keys:
		(bin_search_it(nums, x))
	end4 = time.time()
	print("Zeit der iterativen Binärsuche: ",end4 - start4)



# Aufgabe 4
# Zuerst wieder die Funktionen aus der VL

def factorial (n):
	if n<= 0:
		return 1
	else:
		return n*factorial(n-1)
		
def odd(n):				# Nicht in den Folien gefunden, schnell selbst geschrieben.
	if(n % 2) == 0:
		return False
	else:
		return True

res = []				# res muss vor der kommenden Definition definiert werden, da es sonst bei rekursiven Aufrufen wieder als leere Liste initialisiert wird
def apply_if(f,p,xs):
	if xs == []:
		return res
	if p(xs[0]):
		res.append(f(xs[0]))
		return apply_if(f,p,[i for i in xs if i != xs[0]])
	else:
	    res.append(xs[0])
	    return apply_if(f,p,[i for i in xs if i != xs[0]])
			
# Aufgabe 5	
# Das Bild zeigt in der möglichen Bildausgabe zwar ausgefüllte Sterne, die Aufgabe fordert aber keine. Daher haben wir das weggelassen.
# Aufgabe 5 a)
def paint_star(x, y, size):
	t.up()
	t.goto(x, y)
	t.down()
	angle = 160
	for i in range(9):
		t.forward(size)
		t.right(angle)
		t.forward(size)
		t.right(40 - angle)

# Aufgabe 5 b)

def sky(n):
	for i in range(n):
		x = random.randint(-200,200)
		y = random.randint(-200,200)
		r = random.random()
		g = random.random()
		b = random.random()
		size = random.randint(10,100)
		t.color(r,g,b)
		paint_star(x, y, size)
		i+=1
# Aufgabe 5 c)
# Für die nächsten Aufgaben haben wir uns entschieden, mit festen Werten zu programmieren, statt mit frei wählbaren, da wir ja genau die Bilder der Übung ausgeben sollen. Falsche Werte wären falsche Bilder.			
def squares(i):
	if i == 18:
		return
	else:
		t.up()
		t.goto(-5*i,-5*i)
		t.down()
		if i % 2 == 0:
			t.color("red")
		else:
			t.color("black")
		square(i, 4)
		squares(i+1)
		
def square(i, j):
	if j == 0:
		return
	else:
		t.forward(10 * (i+1))
		t.left(90)
		return square(i, j-1)

# Aufgabe 5 d)
# zunächst zwei Hilfsfunktionen
def new_squares(i, x, y, start_size, n, new_x, new_y):			# i = Zähler, der immer auf 0 gesetzt wird. x und y markieren die Startposition, start_size ist die größte des ersten (kleinsten) Quadrats und n die Anzahl der Quadrate, new_x und new_y gibt die "Ausdehnung" der Quadrate an
	if i == n:
		return
	else:
		t.up()
		t.goto(x + (new_x * i),y + (new_y * i))
		t.down()
		if i % 2 == 0:
			t.color("red")
		else:
			t.color("black")
		new_square(i, 4, start_size)
		new_squares(i+1, x, y, start_size, n, new_x, new_y)
		
def new_square(i, j, size):
	if j == 0:
		return
	else:
		t.forward(size * (i+1))
		t.left(90)
		return new_square(i, j-1, size)

def fractal_squares():
	new_squares(0, 0, 0, 20, 8, -10, -10)										# Großes Quadrat in der Mitte
	new_squares(0, -53, -53, (40/6), 6, -(20/6), -(20/6))						# Kleines Quadrat in großem unten links
	new_squares(0, -53, 67, (40/6), 6, -(20/6), -(20/6))						# Kleines Quadrat in großem oben links
	new_squares(0, 67, 67, (40/6), 6, -(20/6), -(20/6))							# Kleines Quadrat in großem oben rechts
	new_squares(0, 67, -53, (40/6), 6, -(20/6), -(20/6))						# Kleines Quadrat in großem unten rechts
	new_squares(0, -112, -112, 12, 6, -6, -6)									# Mittleres Quadrat unten links Quadrat
	new_squares(0, -165, -165, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, -165, -53, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, -53, -165, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, -112, 120, 12, 6, -6, -6)
	new_squares(0, -165, 67, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, -165, 179, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, -53, 179, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, 120, 120, 12, 6, -6, -6)
	new_squares(0, 67, 179, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, 179, 67, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, 179, 179, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, 120, -112, 12, 6, -6, -6)
	new_squares(0, 179, -53, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, 67, -165, (40/6), 6, -(20/6), -(20/6))
	new_squares(0, 179, -165, (40/6), 6, -(20/6), -(20/6))

# Aufgabe 6
def revDigits(n):
	rev = 0
	while n != 0:
		num = n % 10
		rev = rev*10 + num
		n = n // 10
	return rev

# Testfunktionen
def test_aufgabe_eins():
	print(mersenne(int(input("Von welcher Zahl soll die Mersennezahl berechnet werden?"))))
def test_aufgabe_zwei():
	print("Aufgabe 2a):")
	print(repeats(int(input("Größte Zahl in der Liste eingeben: ")),int(input("Obere Grenze für Zufallszahl eingeben: "))))
	print("Aufgabe 2b):")
	print(dic_repeats(int(input("Größte Zahl in der Liste eingeben: ")),int(input("Obere Grenze für Zufallszahl eingeben: "))))
	
def test_aufgabe_drei():
	test_searches()

def test_aufgabe_vier():							
	print(apply_if(factorial,odd,[2,5,7,4,9,6]))	# Wir haben die Liste aus der Aufgabe direkt mit übernommen um das Ergebnis prüfen zu könnnen. Kann aber gerne geändert werden.

def test_aufgabe_fuenf():							# Wir haben für jede Teilaufgabe extra Testfunktionen angefertig, damit man sie unabhängig testen kann	
	t.shape("turtle")
	t.color("green")
	def test_fuenf_a():
		paint_star(int(input("X-Koordinate eingeben: ")),int(input("Y-Koordinate eingeben: ")),int(input("Durchmesser eingeben: ")))
	test_fuenf_a()
	t.reset()
	def test_fuenf_b():
		sky(int(input("Anzahl der Sterne eingeben: ")))
	test_fuenf_b()

	print("Für Aufgabe 5c) bitte ENTER drücken")
	input()
	t.reset()	
	t.hideturtle()				# damit es schneller geht
	t.speed(0)
	def test_fuenf_c():
		squares(0)
	test_fuenf_c()

	print("Für Aufgabe 5d) bitte ENTER drücken")
	input()
	t.reset()	
	t.hideturtle()
	t.speed(0)
	def test_fuenf_d():
		fractal_squares()
	test_fuenf_d()
def test_aufgabe_sechs():
	print(revDigits(int(input("Welche Zahl soll umgedreht werden?"))))

# Testfunktionsaufrufe
print("Aufgabe 1:")
test_aufgabe_eins()
print("Aufgabe 2: ")
test_aufgabe_zwei()
print("Aufgabe 3: ")
test_aufgabe_drei()
print("Aufgabe 4:")
test_aufgabe_vier()
print("Aufgabe 5:")
test_aufgabe_fuenf()
print("Aufgabe 6:")
test_aufgabe_sechs()


input()	# damit Programm nicht aus der cmd verschwindet
