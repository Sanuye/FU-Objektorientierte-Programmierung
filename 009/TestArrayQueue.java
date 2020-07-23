package u9;

public class TestArrayQueue {
	public static void main(String[] args) {
		Queue<Integer> q = new Queue<Integer>();
		q.enqueue(1);
		q.enqueue(2);
		q.enqueue(3);
		System.out.println("Warteschlange: " + q.toString());
		try {
			System.out.println(q.first());
		}catch(EmptyQueueException eqe) {
			System.out.println(eqe.getMessage());
		}
		try {
			System.out.println("Element entfernt: " + q.dequeue());
		}catch(EmptyQueueException eqe) {
			System.out.println(eqe.getMessage());
		}
		System.out.println("Warteschlange: " + q.toString());
		try {
			System.out.println("Element entfernt: " + q.dequeue());
		}catch(EmptyQueueException eqe) {
			System.out.println(eqe.getMessage());
		}
		System.out.println("Warteschlange: " + q.toString());
		System.out.println(q.empty());
		try {
			System.out.println("Element entfernt: " + q.dequeue());
		}catch(EmptyQueueException eqe) {
			System.out.println(eqe.getMessage());
		}
		System.out.println("Warteschlange: " + q.toString());
		try {
			System.out.println("Element entfernt: " + q.dequeue());
		}catch(EmptyQueueException eqe) {
			System.out.println(eqe.getMessage());
		}
		System.out.println(q.empty());
		q.enqueue(5);
		q.enqueue(9);
		q.enqueue(7);
		q.enqueue(2);
		q.enqueue(13);
		q.enqueue(14);
		try {
			System.out.println(q.first());
		}catch(EmptyQueueException eqe) {
			System.out.println(eqe.getMessage());
		}
		System.out.println("Warteschlange: " + q.toString());
	}
}
