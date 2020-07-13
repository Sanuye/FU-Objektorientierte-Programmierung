# Übung 05.5
# bearbeitet von Jasmine Cavael & Alexander Chmielus
# Tutor: Fabian Halama, Übung 10 (Do. 16-18)

# Aufgabe 5 a)
def insertsort(seq):
	j = 1
	while j < len(seq):
		key = seq[j]
		k = j-1
		while k >= 0 and seq[k] > key:
			seq[k+1] = seq[k]
			k = k-1
		seq[k+1] = key
		j += 1

"""
INV Äußere Schleife:
Die Liste ist von 0 bis k ist zu jedem Zeitpunkt sortiert.
INV Innere Schleife:
seq[k] ist zu jedem Zeitpunkt >= key.
"""

# Aufgabe 5 b)
# Da unsere Invarianten sich nur auf die Liste beziehen, setzen wir die Assert-Anweisungen nur, nachdem die Liste verändert wurde.
def insertsort(seq):
	def isSorted(A, j):                                    # Hilfsfunktion, die uns am Ende sagt, ob die Liste absteigend sortiert ist.
	    res = True
	    for x in range(0, j):
	        if A[x] <= A[x+1]:
	            continue
	        else:
	            return False
	            break
	    return res

	j = 1
	while j < len(seq):
		assert isSorted(seq, j-1)
		key = seq[j]
		assert isSorted(seq, j-1)
		k = j-1
		assert isSorted(seq, j-1)
		while k >= 0 and seq[k] > key:
			seq[k+1] = seq[k]
			assert seq[k] >= key
			assert isSorted(seq, j-1)
			k = k-1
		seq[k+1] = key
		assert isSorted(seq, j-1)
		j += 1
