package u8;

public class NotEnoughCapacityException extends Exception {
	int kappazität;
	int volume;
	
	public NotEnoughCapacityException(int k, int ml) {
		super("Mach lieber nicht zu viel rein.");
		this.kappazität = k;	//Wie viel reinpasst
		this.volume = ml;		//Wie viel rein soll
	}
}
