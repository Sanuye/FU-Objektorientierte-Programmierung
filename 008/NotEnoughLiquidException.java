package u8;

public class NotEnoughLiquidException extends Exception {
	int volume;
	int out;
	
	public NotEnoughLiquidException(int vol, int ml) {
		super("Nicht genug Flüssigkeit vorhanden.");
		this.volume = vol;		//Wie viel vorhanden ist
		this.out = ml;			//Wie viel weg soll
	}
}
