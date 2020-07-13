package u8;

public class UndrinkableException extends Exception {
	boolean d;
	int temperature;
	
	public UndrinkableException(boolean drinkable, int t) {
		super("Das solltest du besser nicht trinken!");
		this.d = drinkable;
		this.temperature = t;
	}
}
