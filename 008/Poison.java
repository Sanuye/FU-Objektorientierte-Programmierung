package u8;

import java.awt.Color;

public class Poison extends Liquid {

	public Poison(String name, Color color, boolean drinkable) {
		super(name, color, drinkable);
		this.temperature = 20;
	}
	
	public String getName() {
		return this.name;
	}

	public Color getColor() {
		return this.color;
	}

	public boolean isDrinkable() {
		return this.drinkable;
	}

	public void hitUp(int temperature) {		//Die Aufgabe sagt nicht, was das hier machen soll.
		return;
	}

	public int getTemperature() {
		return this.temperature;
	}

}
