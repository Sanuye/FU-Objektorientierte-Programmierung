package u9;

public class EmptyQueueException extends Exception {
	public EmptyQueueException() {
		super("Warteschlange ist zur Zeit leer");
	}

}
