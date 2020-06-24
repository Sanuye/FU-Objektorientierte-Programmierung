# Übung 04
# bearbeitet von Jasmine Cavael & Alexander Chmielus
# Tutor: Fabian Halama, Übung 10 (Do. 16-18)

import random
import sys

# Aufgabe 1
# 1 a)
def shellSort(A):
	magic = [1391376, 463792, 198768, 86961, 33936, 13776, 4592, 1968, 861, 336, 112, 48, 21, 7, 3, 1]		# magic definieren
	for x in magic:																							# seg_size herausfinden. Wenn das erste mal A größer ist, als eine der Zahlen in magix, wird diese genommen als erste seg_size
		if len(A) > x:
			seg_size = x
			break
	dex = magic.index(seg_size)																				# Hier finden wir den Index der seg_size heraus
	while dex < len(magic)-1:																				# Wir können das nur so lange machen, wie Elemente in magic vorhanden sind, daher geht die Schleife bis zum Index len-1
		for start_i in range(seg_size):
			jump_InsertSort(A, start_i, seg_size)
		dex = magic.index(seg_size)
		if dex != len(magic) - 1:																			# Wenn wir noch nicht am letzten Index (also am letzten Schritt) angekommen sind, hole die nächste seg_size aus magic
		    seg_size = magic[dex+1]
		else:																								# Ansonsten brich ab
		    break
		
def jump_InsertSort(A, start, step):																		# Hier ist alles, wie immer
	for i in range(start+step, len(A), step):
		value = A[i]
		j = i
		while j >= step and A[j-step] > value:
			A[j] = A[j-step]
			j = j - step
		A[j] = value

# 1 b)

def count_shellSort(A):
	magic = [1391376, 463792, 198768, 86961, 33936, 13776, 4592, 1968, 861, 336, 112, 48, 21, 7, 3, 1]
	comp = 0											# Vergleichszähler
	for x in magic:
		if len(A) > x:									# Hier wird das erste Element aus Magic definiert.
			comp += 1
			seg_size = x
			break
		else:
		    comp += 1                                   # ist die if-Bedingung nicht erfüllt, wurde aber trotzdem verglichen.
	dex = magic.index(seg_size)
	comp += 1											# Wir erhöhen hier im voraus den Zähler, weil wenn die While-Schleife abbricht das comp+=1 in der Schleife nicht ausgeführt wird, der Vergleich aber gezählt werden muss.
	while dex < len(magic)-1:							# Bei jedem durchlauf wird etwas verglichen.
		comp += 1
		for start_i in range(seg_size):
			comp = count_jump_InsertSort(A, start_i, seg_size, comp)
		dex = magic.index(seg_size)
		if dex != len(magic) - 1:
			comp += 1									# Hier wird der Index mit der Länge von Magic -1 verglichen um das nächste Element zu holen.
			seg_size = magic[dex+1]
		else:
			comp += 1									# Der If-vergleich wurde ausgeführt, der Befehlsblock nach dem If aber nicht. Daher hier das Erhöhen.
			break
	return (comp, A)
	
def count_jump_InsertSort(A, start, step, comp):
	for i in range(start+step, len(A), step):
		value = A[i]
		j = i
		while j >= step and A[j-step] > value:			# Die Schleifung Bedingung vergleich immer 2 Dinge. Also müssen wir den Zähler um 2 erhöhen.
			comp += 2
			A[j] = A[j-step]
			j = j - step
		comp += 2										# Am Ende muss er nochmal erhöht werden, da die Vergleiche in der While-Schleife stattfinden, aber die Schleife nicht ausgeführt wird.
		A[j] = value
	return comp
		
# 1c)

def shell_vs_insert():
	def insertsort(seq):
		ins_comp = 0
		for j in range(1, len(seq)):
			key = seq[j]
			k = j-1
			while k >= 0 and seq[k] > key:
				ins_comp += 2							# Am Anfang jeder Schleife werden 2 Vergleiche ausgeführt um die Bedingung zu prüfen
				seq[k+1] = seq[k]
				k = k-1
			ins_comp += 2								# Am Ende auch, aber die Schleife wird nicht ausgeführt, deswegen müssen wir hier erneut Erhöhen.
			seq[k+1] = key
		return ins_comp


	# Zuerst definieren wir eine Liste, die unsere Listen enthält.
	lists = [[1, 3, 5, 7, 9, 2, 4, 6, 8, 0], [9 ,0 ,2 ,2 ,6 ,3 ,7 ,1 ,9 ,0 ,2 ,6 ,3 ,7 ,4 ,8 ,5 ,6 ,3 ,7], [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13 ,12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 
			[2, 18, 37, 49, 65, 71, 82, 93, 104, 4], [346, 13, 7, 3587, 258, 837, 1363, 357, 258, 246, 245, 235 , 1, 1, 35, 23, 57, 12, 34, 67, 12], [x + random.randint(100, 1000) for x in range(100)]]
	for i in range(len(lists)):
		copy = lists[i]
		print("Liste:", lists[i])
		print("Anzahld der Vergleiche: Insertsort - shellSort mit Magic: ", insertsort(lists[i]), " - " , count_shellSort(copy)[0])

# Aufgabe 2

# Aufgabe 2b)

def next_message():
	prio = random.randint(1, 50)
	message = random.randint(1, 1000)
	time = random.randint(1, 24)
	return (prio, time, message)

# Aufgabr 2c)
# Wir stellen uns die Priority-Queue als Heap vor, d.h Im ersten Feld der Liste steht die Größe des Heaps, dahinter fängt erst die eigentliche Priority-Queue an.

def is_empty(priority_queue):
	def heap_size(H):
		return H[0]
		
	if heap_size(priority_queue) == 0:			# Wenn Heap-Größe = 0 -> Heap ist leer.
		return True
	else:
		return False

# Wir nehmen hier an, dass die messages bereits Prio und Zeit besitzen.
def insert (priority_queue, message):
	priority_queue.append(message)				# Message hinzufügen
	priority_queue[0] += 1						# Heap-Größe += 1

# Da wir die Heap-Struktur verwenden sollen, denken wir, dass Heap-Sort angebracht wäre.
# Am Ende des Sortierens muss das Element mit der Höchsten Priorität ganz vorne stehen. Bei Gleichstand das, mit der kleineren Zeit.
# Die Zeit interpretieren wir so, dass das Element mit t = 0 als erstes eingefügt wurde, das mit t= 1 danach usw..
# Um auf die Prio der Elemente zuzugreifen benutzen wir H[Pos][0]. Wir schauen uns also die 0. Stelle im Tupel an Position Pos in H an. Für die Zeit verwenden wir analog H[Pos][1].
# Der Rest ist so ziemlich gleich mit dem Algorithmus aus der VL. Wir benutzen auch hier wieder lokale Funktionen um nicht mit anderen Aufgaben zu interferieren.
def sort_messages(priority_queue):
	def heap_size(H):
		return H[0]
	
	def left(i):
	    return i*2
	
	def right(i):
		return i*2 + 1
	
	def dec_heap_size(H):
		H[0] = H[0] -1

	def max_heapify(H, pos):
		left_t = left(pos)
		right_t = right(pos)
		if left_t <= heap_size(H) and H[left_t][0] < H[pos][0]:
			smallest = left_t
		elif left_t <= heap_size(H) and H[left_t][0] == H[pos][0] and H[left_t][1] > H[pos][1]:
			smallest = left_t
		else:
			smallest = pos
		if right_t <= heap_size(H) and H[right_t][0] < H[smallest][0]:
			smallest = right_t
		elif right_t <= heap_size(H) and H[right_t][0] == H[smallest][0] and H[right_t][1] > H[smallest][1]:
			smallest = right_t
		if smallest != pos:
			H[pos], H[smallest] = H[smallest], H[pos]
			max_heapify(H, smallest)
		
	def build_max_heap(H):
		H[0] = len(H)-1
		for i in range(heap_size(H)//2, 0, -1):
			max_heapify(H, i)
		
		
	def heapsort(H):
		build_max_heap(H)
		for i in range(heap_size(H), 1, -1):
			H[i], H[1] = H[1], H[i]
			dec_heap_size(H)
			max_heapify(H, 1)
		dec_heap_size(H)
	save = heap_size(priority_queue)				# nach dem Heapsort ist H[0] = 0, was aber falsch ist. Daher müssen wir diesen Wert vor dem Sortieren Zwischenspeichern..
	heapsort(priority_queue)
	priority_queue[0] = save						# Und am Ende wieder einfügen.

# Vor der Delete-Funktion sollte, wenn nötig, sortiert werden. Wenn wir bspw. delete 2x aufrufen, wäre es unnötig, erneut zu sortieren, da sie nach dem 1. Aufruf immernoch sortiert ist. 	
# Die Q hat immer mindestens Länge 1, weil dort die Größe des Heaps gespeichert ist. Ist die Länge größer, befinden sich noch Elemente dort. Da wir eine sortierte Q erwarten, reicht es, das Element an Stelle 1 zu entfernen, da dieses als nächstes dran ist.
def delete(priority_queue):
	if len(priority_queue) > 1:
		old = priority_queue[1]
		print("Task completed, deleted: ", old)
		del priority_queue [1]
		priority_queue[0] -= 1
	else:
		return None

# Aufgabe 2d)
# Die Aufgabenstellung war leider auch hier etwas unklar. Was soll " nach zufälligen Zeitabständen und Prioritäten einfügt bzw. entfernt" heißen?!
def sim_message_traffic(priority_queue):
	sort_messages(priority_queue)
	in_or_del = random.randint(0, 1)
	if in_or_del == 0:
		delete(priority_queue)
	else:
		new = next_message()
		print("New Message incoming:", new)
		insert(priority_queue, new)
		sort_messages(priority_queue)
	return priority_queue

# 2e)
"""
next_message:
Jeder Befehl wird 1x ausgeführt. Daher liegt die gesamte Funktion in O(1)
is_empty:
Hier wird auch alles nur 1x aufgerufen. -> O(1)
insert:
Das gleiche. O(1)
delete:
Analog dazu. O(1)
sort_messages:
Da hier eine Variante des Heap-Sort-Algorithmus verwendet wurde, liegt diese Funktion in O(n*log(n))
sim_message_traffic:
Da sort_messages in O(n*log(n)) liegt und der Rest nur 1x aufgeruden wird, liegt diese Funktion auch in O(n*log(n))
"""

# Aufgabe 3
# Im Tut haben wir uns ja darüber unterhalten, dass es okay ist, das Aufsummieren im Countingsort aus der VL wegzulassen, daher diese Lösung:
def in_place_cs(A, k):				# A = unsortierte Liste, k = größtes Element in der Liste.
    C = [0] * (k+1)
    for i in A:
        C[i] += 1
    index = 0
    for i in range (len(C)):
        while 0 < C[i]:
            A[index] = i
            index = index + 1
            C[i] -= 1
"""
A hat n Elemente. Die erste For-Schleife wird also n mal durchlaufen. Die zweite For-Schleife wird k mal durchlaufen.
Die While-Schleife wird n mal durchlaufen, da wir C[i] n-mal dekrementieren müssen.
T(n) = c1 * n + c2 * k + c3 * n = (c1 + c3) * n + c2 * k = O(n + k)
"""


# Aufgabe 4

import random

def google_vs_obama():
	def counting_sort(A, e):
		size = len(A)
		B = [0] * size
		C = [0] * 10									# Da Radixsort nach Ziffern sortiert, können wir nur 10 Werte (0-9) im C-Array haben.
		for j in range(0, size):
		    index = A[j] / e                            # Die Stelle, auf die es gerade ankommt, wird vor das Komma gestellt
		    index = int(index % 10)                     # Durch % 10 erhalten wir genau diese Stelle. Int wandelt den vorher erhaltenen Float zurück, damit wir ihn als Index verwenden können.
		    C[index] += 1                               # Und erhöhen im C-Array den entsprechenden Zähler
		for i in range(1, 10):
			C[i] += C[i-1]                              # Hier wird aufsummiert
		for j in range(size-1, -1, -1):                 # Analoges Verfahren beim Einfügen in B.
			index = A[j] / e
			index = int(index % 10)
			C[index] -= 1
			B[C[index]] = A[j]
		return B
	
	def radixsort(A):
		maxi = max(A)
		expo = 1
		while maxi/expo >= 1:                           # Solange Der Exponent genau so viele Stelle hat, wir die größte Zahl
			A = counting_sort(A, expo)                  # Wird sortiert.
			expo *= 10                                  # Exponent wird auf die nächste Stelle erhöht (erst 1er, dann 10er, dann 100er,...)
		return A
	
	def isSorted(A):                                    # Hilfsfunktion, die uns am Ende sagt, ob die Liste absteigend sortiert ist.
	    res = True                                      # Es wäre ziemlich unpraktisch, eine Liste mit 1.000.000 Zahlen als Rückgabewert zu haben
	    for x in range(len(A)-1):                       # Daher haben wir uns entschieden, mit dieser Hilfsfunktion zu testen, ob alles Funktioniert hat.
	        if A[x] <= A[x+1]:
	            continue
	        else:
	            return False
	            break
	    return res
	
	L = []
	for x in range(0, 100):
		i = random.randint(0, 1000)
		i = i & 0xffffffff								# Damit es eine 32-Bit Zahl wird.
		L.append(i)
	L = radixsort(L)                                    # Sortiere Liste
	ret = isSorted(L)
	return ret
	#Wenn du doch Lieber die Liste sehen möchtest, nimm einfach diese return-Anweisung stattdessen:
	#return L  

"""
Vorteile: 
Liegt in O(n) und ist damit relativ schnell
Stabil
Nachteile: 
Countingsort braucht zusätzlichen Speicher, der erstmal vorhanden sein muss.
Dadurch nicht In-Place.
"""


# Testfunktionen
def test_aufgabe_eins():
	def test_aufgabe_eins_a():
		L = [9 ,0 ,2 ,2 ,6 ,3 ,7 ,1 ,9 ,0 ,2 ,6 ,3 ,7 ,4 ,8 ,5 ,6 ,3 ,7]		
		print("Unsortierte Liste: ", L)
		shellSort(L)
		print("Sortierte Liste: ", L)
	def test_aufgabe_eins_b():
		L = [9 ,0 ,2 ,2 ,6 ,3 ,7 ,1 ,9 ,0 ,2 ,6 ,3 ,7 ,4 ,8 ,5 ,6 ,3 ,7]		
		print("Unsortierte Liste: ", L)
		print("Sortierte Liste: ", count_shellSort(L)[1])
		print("Anzahl der Vergleiche:" ,count_shellSort(L)[0])
	def test_aufgabe_eins_c():
		shell_vs_insert()
	test_aufgabe_eins_a()
	test_aufgabe_eins_b()
	test_aufgabe_eins_c()

def test_aufgabe_zwei():
	Q = [0]
	print("Jetzt werden zufällig 20 Operationen aufgerufen, die zur Zeit leere Queue sieht so aus: ", Q)
	for i in range(20):
		print(sim_message_traffic(Q))

		
def test_aufgabe_drei():
	L = [9 ,0 ,2 ,2 ,6 ,3 ,7 ,1 ,9 ,0 ,2 ,6 ,3 ,7 ,4 ,8 ,5 ,6 ,3 ,7]
	print("Unsortierte Liste: ", L)
	in_place_cs(L, max(L))
	print("Sortierte Liste: ", L)

def test_aufgabe_vier():
	print("Gib True aus, wenn alles wie gefordert geklappt hat (Weitere Hinweise im Quellcode): ", google_vs_obama())

		
# Funktionsaufrufe
print("Aufgabe 1")
test_aufgabe_eins()
print("ENTER drücken für Aufgabe 2. Es sollte eine Simulation der Warteschlange starten.")
input()
print("Aufgabe 2")
test_aufgabe_zwei()
print("Aufgabe 3")
test_aufgabe_drei()
print("ENTER drücken für Aufgabe 4.")
input()
print("Aufgabe 4")
test_aufgabe_vier()


		
input() # damit das Programm nicht aus der cmd verschwindet