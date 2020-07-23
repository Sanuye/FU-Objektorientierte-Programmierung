package u9;


public class Queue<E> implements Q<E> {
	private E[] queue;	//Warteschlange
	private int tail;	//Zeigt auf die erste Freie Stelle
	private int head;	//Zeigt auf das vorderste (erste) Element
	
	
	public class QueueIterator<K> implements Iterator<K>{
		public int cur;
		
		public boolean hasNext() {
			return queue[cur+1]!= null;
		}
		
		public K next() {
			if (queue[cur]==null) {
				return null;
			}
			else {
				return (K) queue[cur+1];
			}
		}
	}
	
	public Queue(){
		this.queue = (E[]) new Object[2];	//Wir Initialisieren die Warteschlange mit Größe 2
		this.tail = 0;						//Beide Pointer zeigen auf die erste Stelle
		this.head = 0;
	}
	
	public boolean full() {
		return((tail == queue.length-1) && (head==0) || (head == tail+1));
	}

	//Wenn wir die Größe des Arrays erhöhen, müssen wir darauf achten, die zirkulare Struktur zu erhalten.
	//Dafür können alle Elemente bis zum head-pointer da bleiben, wo sie sind, aber alle danach müssen (die Reihenfolge erhaltend) bis ans Ende verschoben werden.
	//Wenn allerdings head = 0 ist, kann alles so bleiben
	public void resizeQ() {
		E[] temp = (E[]) new Object[queue.length*2];
		for (int i = 0; i<queue.length; i++){
			if (head == 0) {
				temp[i] = queue[i];
			}
			else {
				if (i < head) {
					temp[i] = queue[i];
				}else {
					temp[i+queue.length] = queue[i];
				}
			}
		}
		head+=queue.length;
		queue = temp;
	}
	
	public void enqueue(E elem){
		if(!full()){
			queue[tail] = elem;
			if(tail == queue.length-1){
				tail = 0;
			}else{
				tail++;
			}
		} else {
			resizeQ();
			queue[tail] = elem;
			if(tail == queue.length-1){
				tail = 0;
			}else{
				tail++;
			}
		}
	}
	
	public boolean empty() {
		return head==tail;
	}
	
	public E dequeue() throws EmptyQueueException{
		if (!empty()){
			E elem = queue[head];
			queue[head] = null;
			if(head == queue.length-1){
				head = 0;
			} else {
				head++;
			}
			return elem;
		} else {
			throw new EmptyQueueException();
		}
	}
	
	public E first() throws EmptyQueueException{
		return queue[head];
	}
	
	public String toString() {
		String res = "";
		for (int i = 0; i<queue.length; i++){
			if (queue[i] != null) {
				res += queue[i];
			}
		}
		return res;
	}
}
