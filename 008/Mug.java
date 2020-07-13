package u8;

public class Mug <T extends Liquid> {
	T fluid;			//Das, was reingefüllt wird
	int volume;			//Derzeitiger Inhalt
	int kappazität;		//Maximaler Inhalt
	boolean drinkable;
	int temperature;
	
	public Mug(T fluid) {
		this.fluid = fluid;
		this.volume = 0;
		this.kappazität = 500;
		this.drinkable = fluid.isDrinkable();
		this.temperature = fluid.getTemperature();
	}
	
	public void pour(int ml) throws NotEnoughCapacityException{
		
		if(this.volume+ml > kappazität) {
			throw new NotEnoughCapacityException(kappazität-volume, ml);
		}
		else {
			this.volume +=ml;
		}
	}
	
	public void takeOut(int ml) throws NotEnoughLiquidException{
		if(this.volume-ml <0) {
			throw new NotEnoughLiquidException(volume, ml);
		}else {
			this.volume -=ml;	
		}
	}
	
	public void drink(int ml) throws UndrinkableException, NotEnoughLiquidException {
		if (!fluid.drinkable || this.isHot()) {				//Wenn es nicht trinkbar, oder zu heiß ist -> Exception
			throw new UndrinkableException(fluid.drinkable, fluid.temperature);
		}
		else if (this.volume-ml < 0){
			throw new NotEnoughLiquidException(volume, ml);	//Will man mehr trinken, als vorhanden ist --> Exception
		}
		else {
			this.volume-=ml;
		}
	}
	
	public int empty() {
		volume = 0;
		return volume;
	}
	
	public boolean isHot() {
		if (fluid.temperature >= 60) {			//Wir haben uns nach einigen Recherchen auf 60 Grad als Grenze zum trinkbaren entschieden.
			return true;
		}
		else {
			return false;
		}
	}
	
	public boolean isEmpty() {
		if (volume == 0) {
			return true;
		}
		else {
			return false;
		}
	}
}
