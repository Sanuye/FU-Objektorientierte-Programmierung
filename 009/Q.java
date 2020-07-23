package u9;

public interface Q<E> {
	public void enqueue(E elem);
	public E dequeue() throws EmptyQueueException;
	public E first() throws EmptyQueueException;
	public boolean empty();
	public String toString();
}