package u9;


public class PriorityQueue <P extends Comparable<P>, Data> {
	
	private HeapNode message;	//Nachricht
	private HeapNode[] heap;	//Heap
	private int tail;			//zeigt auf den n�chsten freien Platz
	private int head;			//zeigt auf das erste Element
	
	public class HeapNode{
		private Data d;
		private P prio;
		
		public HeapNode(Data d, P prio) {
			this.d = d;
			this.prio = prio;
		}
	}
	
	public PriorityQueue() {
		this.heap = (HeapNode[]) new Object[1];	//Wir initialisieren die Warteschlange mit Gr��e 1
		this.tail = 0;
		this.head = 0;
	}

	//Heap-Funktionen, gr��tenteils aus �bung 4 �bernommen, daher ersparen wir uns gr��tenteils das Kommentieren.
	public int getSize() {			//Gr��e
		return heap.length;
	}
	
	public int left(int pos) {		//Position des linken Kindes
		return pos*2;
	}
	
	public int right(int pos) {		//Position des rechten Kindes
		return pos*2+1;
	}
	
	public void max_heapify(int pos) {
		int biggest = pos;
		HeapNode temp;
		int left_t = left(pos);
	 	int right_t = right(pos);
	 	int compare;
	 	if (heap[left_t] != null) {										//Schaue zuerst, on linkes Kind existiert
	 		compare = heap[left_t].prio.compareTo(heap[pos].prio);		//Vergleicht Priorit�t mit linkem Kind
	 		if (compare > 0) {											//Wenn Prio des linken Kindes gr��er ist, merke es als gr��tes Element
	 			biggest = left_t;
	 		}
	 	}
	 	if (heap[right_t] != null) {									//Schaue, ob rechtes Kind existiert
	 		compare = heap[right_t].prio.compareTo(heap[pos].prio);		//Vergleiche Prio des rechten Kindes mit der des gr��ten Elements
	 		if (compare > 0) {											//Wenn sie Gr��er ist, ist das rechte Kind das gr��te, ansonsten bleibt alles
	 			biggest = right_t;
	 		}
	 	}
	 	if(heap[biggest] != heap[pos]) {								//Wenn biggest & das derzeitige Verschieden sind, vertausche sie und sortiere erneut.
	 		temp = heap[pos];
	 		heap[pos] = heap[biggest];
	 		heap[biggest] = temp;
	 		max_heapify(biggest);
	 	}
	 }
	
	public void build_max_heap() {
		int i = heap.length/2;											//Ganzzahlige Division, da wir einen Int erwarten.
		while (i >= 0) {
			max_heapify(i);
			i--;
		}
	}
	
	public void heapsort() {											//Dieser Heapsort sortiert aufsteigend.
		build_max_heap();
		int i = heap.length;
		HeapNode temp;
		while(i>0) {
			temp = heap[i];
			heap[i] = heap[0];
			heap[1] = temp;
			max_heapify(i);
			i--;
		}
	}
	
	//Das ganze funktioniert so aber nur in einem linearen Array. Daher wandeln wir zuerst das zirkulare in ein lineares.
	
	public void sort() {
		HeapNode[] temp = (HeapNode[]) new Object[heap.length];
		int j = 0;	//Wir m�ssen sicherstellen, dass in temp die Elemente bei temp[0] anfangen und ab da keine L�cken mehr auftreten, bis keine Elemente mehr da sind.
		if(tail > head) {									//Wenn Tail > Head, haben wir bereits eine lineare Struktur.
			for(int i = head; i<tail; i++) {				//Wir kopieren alle Elemente ab head, bis tail
				temp[j] = heap[i];	
				j++;
			}
		} else {
			for(int i = head; i<heap.length; i++) {			//Zuerst kopieren wir alle Elemente vom Head-Pointer bis zum Ende des Arrays
				temp[j] = heap[i];	
				j++;
			}
			for(int i = 0; i<tail; i++) {					//Jetzt alle bis tail
				temp[j] = heap[i];
				j++;
			}
		}
		heap = temp;										//Wir erhalten ein neues lineares Array
		head = 0;											//Deshalb zeigt head wieder auf 0
		tail = j+1;											//Und Tail auf das erste freie Element
		heapsort();
		
	}
	
	//Funktionen f�r Aufgabe 3d)
	
	public boolean empty() {
		return head == tail;
	}
	
	public boolean full() {
		return((tail == heap.length-1) && (head==0) || (head == tail+1));
	}
	
	public void resizeQ() {
		HeapNode[] temp = (HeapNode[]) new Object[heap.length*2];
		for (int i = 0; i<heap.length; i++){
			if (head == 0) {
				temp[i] = heap[i];
			}
			else {
				if (i < head) {
					temp[i] = heap[i];
				}else {
					temp[i+heap.length] = heap[i];
				}
			}
		}
		head+=heap.length;
		heap = temp;
	}
	
	public void enqueue(HeapNode elem){
		if(!full()){
			heap[tail] = elem;
			if(tail == heap.length-1){
				tail = 0;
			}else{
				tail++;
			}
		} else {
			resizeQ();
			heap[tail] = elem;
			if(tail == heap.length-1){
				tail = 0;
			}else{
				tail++;
			}
		}
	}
	
//Eigentlich w�re es effizienter, sort() nur vor dem suchen zu machen. Da das Sortieren aber in O(n*log(n)) liegt und das suchen & l�schen in O(log(n)) liegen soll, m�ssen wir das wohl hier machen.	
	
	public Data dequeue() throws EmptyQueueException{
		if (!empty()){
			HeapNode elem = heap[head];
			heap[head] = null;
			if(head == heap.length-1){
				head = 0;
			} else {
				head++;
			}
			return elem.d;
		} else {
			throw new EmptyQueueException();
		}
	}
	
	//Da wir immer einen sortierten maxHeap haben, m�ssen wir uns nur die Bl�tter angucken und die h�chste Prio herausfinden.
	//Die Bl�tter (falls vorhanden) befinden sich an allen Positionen nach
	public Data highest() throws EmptyQueueException{
		return heap[tail-1].d;
		//TODO Bin�rsuche 
	}
	
	//Wir haben diese Funktion noch rein genommen, um uns das Array ausgeben zu lassen
	public String toString() {
		String res = "";
		for (int i = 0; i<heap.length; i++){
			if (heap[i] != null) {
				res += heap[i].d;
			}
		}
		return res;
	}
}
