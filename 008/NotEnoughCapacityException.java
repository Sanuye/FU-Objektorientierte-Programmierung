package u8;

public class NotEnoughCapacityException extends Exception {
	int kappazit�t;
	int volume;
	
	public NotEnoughCapacityException(int k, int ml) {
		super("Mach lieber nicht zu viel rein.");
		this.kappazit�t = k;	//Wie viel reinpasst
		this.volume = ml;		//Wie viel rein soll
	}
}
