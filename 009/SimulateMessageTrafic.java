package u9;

public class SimulateMessageTrafic {
	public static void main(String[] args) {
		PriorityQueue<Integer, String> q = new PriorityQueue<Integer, String>();		//Hier tauchen die ersten Probleme auf, die wir uns nicht wirklich erklären können.
		for(int i = 0; i <10; i++) {
			PriorityQueue.HeapNode n = q.new HeapNode("Hallo: " + i, 1);
			q.enqueue(n);
		}
		q.toString();
	}
}
