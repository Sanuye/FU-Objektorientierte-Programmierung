# bearbeitet von Jasmine Cavael & Alexander Chmielus
# Tutor: Fabian Halama, Übung 10 (Do. 16-18)
import random
import operator

# Aufgabe 1

def random_list(min, max, n):
	lis = []
	if max < min:
		return "Denk nochmal über die Eingabe nach."
	while n != 0:
		x = random.randint(min, max)
		lis.append(x)
		n = n -1
	return lis
	
def sorted(op, l):
	i = 0
	while i<len(l)-1:
		if op(l[i], l[i+1]):			# die geforderten operatoren werden auf zwei elemente angewandt, nämlich Stelle i und i+1 der Liste (daher muss i auch nie = len(l) sein, weil wir ja i+1 auch bekommen).
			i = i + 1
			pass						# Wenn alles stimmt, mach nichts
		else:
		    i = i + 1
		    return False			    	# Sobald der erste Fehler auftritt, gib False zurück
	return True	
			

# Aufgabe 2
def count_bubblesort(A):
	counts = [0] * (max(A)+1)							# Diese Liste zählt an ihren Indizes, welches Element wie oft bewegt wurde (Elem(A) = index(counts)). Dazu muss sie mindestens so groß sein, wie max(A)+ 1 für die Null.
	idList = A[:]
	swap = True
	stop = len(A)-1
	while swap:
		swap = False
		for i in range(stop):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
				counts[A[i]] += 1
				counts[A[i+1]] += 1
				swap = True
		stop = stop -1
	diff = 0
	diffList = [0]* (max(A)+1)
	for x in A:
		diffList[x] = abs(idList.index(x) - A.index(x))
	for x in range(len(counts)-1):
	    diff = diff + (counts[x] - diffList[x])
	print("Anzahl der falschen Bewegungen: ", diff)                 # Als falsche Bewegungen zählen hier die Bewegungen in die falsche Richtung, sowie die Bewegungen in die richtige Richtung, die zur Korrektur der falschen Bewegungen benötigt werden.
	rights = 0
	for x in diffList:
	    rights = rights + x
	print("Anzahl der richtigen Bewegungen: ", rights)

# Aufgabe 3
# Erklärung zur Check-Variable:
# Da Range im For-Loop exklusiv ist, kann k nie den Wert -1 annehmen, was aber gebraucht wird um am Ende ggf. seq[k+1] = seq[0] = key zu setzen. Das ginge nämlich sonst nicht.
# Daher initialisieren wir check so, dass seq[k] = key.
# Das können wir aber nicht immer machen, da der while-loop aus der VL mit k abbricht und seq[k+1] = key setzt. Der For-Loop hier würde dann mit k abbrechen und seq[k) = key setzen.
# Dieser Fall tritt aber nur ein, wenn durch seq[k] <= key  der While-Loop abbricht, also müssen wir in unserem else-Fall sicherstellen, dass seq[k+1] verändert wird und nicht seq[k], wie es initialisiert ist.
def insertsort(seq):
    for j in range(1, len(seq)):
        key = seq[j]
        k = j-1
        n = k							# Der While-Loop läuft, solange k <= 0 ist, also von k bis 0. n übernimmt hier den Wert von k und ist der Zähler des for-Loops.
        check = -1
        for k in range(n,-1,-1):		# Stellt erste Bedingung des While-Loops sicher, dass er nur von k bis 0 läuft
            if seq[k] > key:			# Stellt die zweite Bedingung des While-Loops sicher, dass seq[k] > key sein muss
                seq[k+1] = seq[k]
                
            else:						# Wenn nicht, wird der Loop direkt mit dem derzeitigen Wert von k verlassen.
                check = 0				# Wir können auch nicht seq an k statt k+1 verändern, da die der While-Loop (wenn seq[k] <= key ist) mit k abbricht. seq wird daraufhin an k+1 verändert. Hier bricht di
                break   				# Der Abbruch des While-Loops wird hier im For-Loop durch break gemacht
        seq[k+1+check] = key	
	
# 3b)

def test_insert(min, max, n):
	lis = random_list(min, max, n)		# Generiere Liste mit Zufallszahlen, die Range & Anzahl der Elemente kann frei gewählt werden
	insertsort(lis)						# Sortiere Liste
	if sorted(operator.le, lis):		# Insertsort aus der VL sortiert so, dass a <= b <= c, also muss mit operator.le geschaut werden, ob alles passt.
		return "Hat geklappt"			# print-Anweisungen kommen bei der Testfunktion, daher hier die returns
	else:
		return "Hat nicht geklappt"
		

# Aufgabe 4

# 4a)

def quicksort(A, low, high):
	if low < high:
		m = partition(A, low, high)
		quicksort(A, low, m-1)
		quicksort(A, m+1, high)
		
def partition(A, low, high):
	a = random.randint(low, high)
	b = random.randint(low, high)
	c = random.randint(low, high)
	if A[a] < A[b]:							# suche mittleres Element
		if A[a] < A[c]:
			if A[b] < A[c]:					# Fall a < b < c
				pivot = A[b]
			else:
				pivot = A[c]				# Fall a < c <= b
		else:
			pivot = A[a]					# Fall c < a < b
	elif A[c] < A[b]:
		pivot = A[b]						# Fall c < b < a
	elif A[a] == A[b] == A[c]:					# Fall a = b = c
		pivot = A[a]
	else:
		if A[a] < A[c]:
			pivot = A[c]					# Fall b < a < c
		else:
			pivot = A[a]					# Fall b < a = c
	
	dex = A.index(pivot)				# Index des Pivotelements
	A[dex], A[low] = A[low], A[dex]		# Tausche Pivotelement mit Element an niedrigstem Index
	i = low								# Danach alles wie gehabt
	for j in range(low+1, high+1):
		if A[j] < pivot:
			i = i+1
			A[i], A[j] = A[j], A[i]
	A[i], A[low] = A[low], A[i]
	return i
	
# 4c)
# Geht, wenn man zB pythons enumerate benutzt. Diese Funktion gibt ein Tupel (Index, Wert) zurück, wodurch man nach Indizes sortieren kann. Desweiteren habe ich hier mehrere Listen benutzt, wodurch leider ein erhöhter Speicheraufwand besteht.
# Da hier der Reihe nach sortiert wird, kann es auch nicht vorkommen, dass zB zwei größerere Werte vertauscht in eine der beiden zusätzlichen Listen kommen.
def stable_quicksort(A):
	if len(A) <= 1:
		return A
	else:
		smaller = []
		bigger = []
		middex = len(A) // 2
		pivot = A[middex]
		for dex, val in enumerate(A):
			if dex != middex:					# Nimm alle Elemente, außer dem Pivot Element
				if val < pivot:
					smaller.append(val)			# Wenn der Wert kleiner ist, geh zum "kleinen" Array
				elif val > pivot:
					bigger.append(val)			# Wenn der Wert größer ist, geh zum "großen" Array
				elif dex > middex:
					bigger.append(val)			# Wenn der Wert gleich ist, aber der Index kleiner ist, gehe zum "kleinen" Array
				else:
					smaller.append(val)			# Und wenn der Index (der ja eindeutig ist) größer ist, gehe zum "großen" Array
		return stable_quicksort(smaller) + [pivot] + stable_quicksort(bigger)
		
# 4f)
# zuerst die Funktionen aus der VL


# Ab hier geht's los
# Wir benutzen die Funktionen aus der VL als lokale Funktionen, damit sie nicht mit anderen, gleichnamigen Funktionen aus anderen Aufgaben durcheinanderkommen.	
def quick_insert(A, low, high, k):
	def insertsort(seq):						# Insertsort aus der VL
	    for j in range(1, len(seq)):
		    key = seq[j]
		    k = j-1
		    while k >= 0 and seq[k] > key:
			    seq[k+1] = seq[k]
			    k = k-1	
		    seq[k+1] = key

	def partition(A, low, high):				# Partition als Teil von Quicksort aus der VL
		pivot = A[low]
		i = low
		for j in range(low+1, high+1):
			if A[j] < pivot:
				i+=1
				A[i], A[j] = A[j], A[i]
		A[i], A[low] = A[low], A[i]
		return i
		
												# Ab hier beginnt der veränderte Quicksort-Algorithmus
	if k > len(A):                              # Wenn das k zu groß gewählt wurde, brich ab
	    return "Kleineres k wählen!"
	elif high - low + 1 < k:					# high (= höchster Index=) - low (=kleinster Index)  entspricht der Länge des zu sortierenden Bereichs -1, also erhalten wir so die genaue Länge.
		insertsort(A)							# Wenn die Länge kleiner als k ist, wird Insertsort angewendet	
	else:										# Wenn nicht Partitionieren wir erneut und führen quick_insert auf die Bereiche [low...m-1] und [m+1... high] rekursiv aus, bis sie klein genug sind.
		m = partition(A, low, high)
		quick_insert(A, low, m-1, k)
		quick_insert(A, m+1, high, k)
	
	return A

# Aufgabe 5
# Wir sortieren zuerst die Liste. Dafür nehmen wir Mergesort wegen der garantierten Laufzeit O(n*log(n)) als lokale Funktion, damit es nicht mit anderen Funktionen in dieser Übung durcheinander kommt.

def min_diff(L):
	def merge(low, high):
		res = []
		i, j = 0, 0
		while i < len(low) and j < len(high):
			if low[i] <= high[j]:
				res.append(low[i])
				i = i+1
			else:
				res.append(high[j])
				j = j + 1
		res = res + low[i:]
		res = res + high[j:]
		return res
	
	def mergesort(A):
		if len(A) < 2:
			return A
		else:
			m = len(A) // 2
			return merge(mergesort(A[:m]), mergesort(A[m:]))
	
	
	A = mergesort(L)
	mini = abs(A[0] - A[1])
	a, b, = A[0], A[1]
	for i in range(1, len(A)-1):
		x = abs(A[i+1] - A[i])
		if x < mini:
			mini = x
			a, b = A[i], A[i+1]
	return (a, b)
"""
Das Sortieren der Liste ist durch Mergesort in jedem Fall in O(n* log(n))
Die for-Schleife wird n-2 mal ausgeführt.
Daraus ergibt sich: T(n) = c1 * n * log(n) + c2 * (n-2) = O(n* log(n))
"""
# Aufgabe 6
# Die Liste res in it_merge speichert die Ergebnisse der Merge-Operationen und ist die einzige weitere Liste.

def it_mergesort(A):
    def it_merge(A, l, r, current):
        res = []																			# Zwischenspeicher
        size1 = r																			# Grenze für erstes Teilarray
        size2 = r + current																	# Grenze für zweites Teilarray
        
        while l < size1 and r < min([size2, len(A)]):										# Für r müssen wir beachten, dass ggf. weniger Elemente, als r + current da sind. In dem Fall hat das letzte den Index len(A)-1
            if A[l] <= A[r]:
                res.append(A[l])															# Analoges Verfahren wie beim rekursiven Mergesort
                l = l + 1
            else:
                res.append(A[r])
                r = r + 1
        for x in range(l, size1):
            res.append(A[x])
        for x in range(r, min([size2, len(A)])):
            res.append(A[x])
        return res
        
    current = 1																				# Größe der Teilarrays, die sortiert werden sollen
    while current < len(A):																	# Sobald current = len(A) gibt es keine Teilarrays mehr, d.h. die Liste ist sortiert
        left = 0																			# Index des ersten Elements des ersten Teilarrays
        while left < len(A) -1:
            if left + current < len(A) -1:													# Index des ersten Elements des zweiten Teilarrays. Wir müssen beachten, dass ggf. nicht genug Elemente für ein Teilarray der Größe current vorhanden sind
                right = left + current
            else:
                right = len(A) - 1
            A = A[:left] + it_merge(A, left, right, current) + A[(right+current):]			# Das Ergebnis aus it_merge wird an der Stelle im Array gespeichert, wo die Zahlen hergenommen wurden.
            left = right + current															# Wiederhole das mit dem nächsten Teilarray, das nach right + current beginnt.
        current = current * 2																# Verdopple Teilarraygröße
    return(A)


# Aufgabe 7
	
def doubles(A, B):
	def merge(low, high):
		res = []
		i, j = 0, 0
		while i < len(low) and j < len(high):
			if low[i] <= high[j]:
				res.append(low[i])
				i = i+1
			else:
				res.append(high[j])
				j = j + 1
		res = res + low[i:]
		res = res + high[j:]
		return res
	
	def mergesort(A):
		if len(A) < 2:
			return A
		else:
			m = len(A) // 2
			return merge(mergesort(A[:m]), mergesort(A[m:]))
	
	lis = A + B
	print(lis)
	lis = mergesort(lis)
	print(lis)
	res = []
	for x in range(0, len(lis)-1):
	    if lis[x] == lis[x+1]:
	        res.append((lis[x], lis[x+1]))
	return res

"""
Zunächst konkatenieren wir die Listen: T(n) = c1 
Danach wird die erhaltene Liste mit Mergesort sortiert, um T(n) = c2 * n * log(n) zu garantieren
Die For-Schleife wird n-1 mal durchlaufen: T(n) = c3 * (n-1) = c3 * n - c3
Damit liegt die Funktion wie gefordert in T(n) = c1 + c2 * n * log(n) + c3 * n - c3 = O(n * log(n))
"""
		
# Testfunktionen
def test_aufgabe_eins():
	def test_eins_a():
		print("1 a)")
		print(random_list(int(input("Kleinstmögliche Zahl eingeben: ")),int(input("Größtmögliche Zahl eingeben:" )), int(input("Anzahl der Elemente eingeben: "))))
		
	def test_eins_b():
		print("1 b)")
		print(sorted(operator.lt, [2, 2, 4, 5, 8, 9]))
		print(sorted(operator.gt, [2, 2, 4, 5, 8, 9]))
		print(sorted(operator.le, [2, 2, 4, 5, 8, 9]))
	
	test_eins_a()
	test_eins_b()

def test_aufgabe_zwei():
	L = [9, 3, 8, 7, 6, 4, 2, 1, 5]
	print("Die Liste ist identisch mit der, aus der Bubblesortanimation aus der VL. Damit lässt sich das Ergebnis leicht überprüfen: ", L)
	print("Desweiteren Zählen sowohl Bewegungen in die falsche Richtung, als auch Bewegungen in die richtige Richtung um diese zu korrigieren zu den 'falschen Bewegungen', da sie ja eigentlichh unnötig sind.")
	count_bubblesort(L)
	
	
def test_aufgabe_drei():
	def test_drei_a():
		print("3 a)")
		L = [1, 3, 6, 2, 7, 9, 3, 5, 4, 0, 3]
		print("Liste = ", L)
		(insertsort(L))
		print("Sortierte Liste: ", L)
	def test_drei_b():
		print("3 b)")
		print(test_insert(int(input("Kleinstmögliche Zahl in der Liste eingeben: ")),int(input("Größtmögliche Zahl in der Liste  eingeben:" )), int(input("Anzahl der Elemente der Liste eingeben: "))))
	test_drei_a()
	test_drei_b()
	
def test_aufgabe_vier():
	def test_vier_a():
		print("4 a)")
		L = [1, 3, 6, 2, 7, 9, 3, 5, 4, 0, 3]
		print("Liste = ", L)
		quicksort(L, 0, len(L)-1)
		print("Sortierte Liste = ", L)
	def test_vier_c():
		print("4 c)")
		L = [1, 3, 6, 2, 7, 9, 3, 5, 4, 0, 3]
		print("Liste = ", L)
		print("Sortierte Liste = ", stable_quicksort(L))
	def test_vier_f():
		print("4 f)")
		L = [1, 3, 6, 2, 7, 9, 3, 5, 4, 0, 3]
		print("Liste = ", L)
		print(quick_insert(L, 0, len(L)-1, int(input("k eingeben: "))))
	
	test_vier_a()
	test_vier_c()
	test_vier_f()
	
def test_aufgabe_fuenf():
	L =[1,3,5,900,2,7,9,21]
	print("Liste: ", L)
	print("Elemente mit kleinstem Abstand: ", min_diff(L))
	
def test_aufgabe_sechs():
	L = [1, 3, 10, 24, 75, 14, 5, 7, 9, 2, 7, 22, 13, 4, 6, 8, 0]
	print("Liste: ", L)
	print("Sortierte Liste: ", it_mergesort(L))
	
def test_aufgabe_sieben():
	L1 = [1, 3, 5, 7, 9]
	L2 = [2, 4, 6, 8, 9, 1]
	print("1. Liste:", L1)
	print("2. Liste", L2)
	print(doubles(L1, L2))
		


# Funktionsaufrufe
print("Da die meisten Funktionen hier Listen als Eingaben verlangen, haben wir sie vorgegeben. Die können aber alle gerne im Code geändert werden zum ausführlichen testen."
print("Aufgabe 1:")
test_aufgabe_eins()
print("Aufgabe 2:")
test_aufgabe_zwei()
print("Aufgabe 3:")
test_aufgabe_drei()
print("Aufgabe 4:")
print("Aus reiner Bequemlichkeit habe ich immer die gleiche Liste zum sortieren genommen. Kann aber gerne im Code geändert werden.")
test_aufgabe_vier()
print("Aufgabe 5:")
test_aufgabe_fuenf()
print("Aufgabe 6:")
test_aufgabe_sechs()
print("Aufgabe 7")
test_aufgabe_sieben()

input()	# damit Programm nicht aus der cmd verschwindet
