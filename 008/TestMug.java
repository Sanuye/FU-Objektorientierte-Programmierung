package u8;

import java.awt.Color;

//Hier werden alle 3 Exceptions mindestens ein mal aufgerufen.

public class TestMug {
	
	public static void main(String[] args) throws NotEnoughCapacityException, NotEnoughLiquidException, UndrinkableException{
		System.out.println("Wir fangen mit Wasser an.");
		Mug<Water> Wasser = new Mug<Water>(new Water("Wasser", Color.BLUE, true));
		try {
			Wasser.pour(300);
		} catch (NotEnoughCapacityException n) {
			System.out.println(n.getMessage());
			System.out.println("So viel passt rein: " + n.kappazität);
			System.out.println("So viel willst du rein machen: " + n.volume);
		}
		System.out.println("Inhalt nach Operation 1: " + Wasser.volume);
		
		
		try {
		Wasser.takeOut(100);
		} catch (NotEnoughLiquidException n) {
			System.out.println(n.getMessage());
			System.out.println("So viel ist vorhanden: " + n.out);
			System.out.println("So viel soll raus: " + n.volume);
		}
		System.out.println("Inhalt nach Operation 2: " + Wasser.volume);
		
		
		try {
			Wasser.pour(400);
		} catch (NotEnoughCapacityException n) {
			System.out.println(n.getMessage());
			System.out.println("So viel passt rein: " + n.kappazität);
			System.out.println("So viel willst du rein machen: " + n.volume);
		}
		System.out.println("Inhalt nach Operation 3: " + Wasser.volume);
		
		
		try {
		Wasser.drink(100);
		} catch (NotEnoughLiquidException n) {
			System.out.println(n.getMessage());
			System.out.println("So viel ist vorhanden: " + n.out);
			System.out.println("So viel möchtest du trinken: " + n.volume);
			
		} catch (UndrinkableException u) {
			if (!u.d) {
				System.out.println(u.getMessage());
			} else {
				System.out.println("Kann man trinken, aber die Temperatur beträgt: " + u.temperature);
			}
		}
		System.out.println("Inhalt nach Operation 4: " + Wasser.volume);
		
		
		Wasser.empty();
		System.out.println("Inhalt nach Operation 5: " + Wasser.volume);
		
		
		try {
			Wasser.drink(100);
			} catch (NotEnoughLiquidException n) {
				System.out.println(n.getMessage());
				System.out.println("So viel ist vorhanden: " + n.out);
				System.out.println("So viel möchtest du trinken: " + n.volume);
				
			} catch (UndrinkableException u) {
				if (!u.d) {
					System.out.println(u.getMessage());
				} else {
					System.out.println("Kann man trinken, aber die Temperatur beträgt: " + u.temperature);
				}
			}
			System.out.println("Inhalt nach Operation 6: " + Wasser.volume);
		
		
		
		System.out.println("Jetzt versuchen wir jemanden zu vergiften.");
		Mug<Poison> Gift = new Mug<Poison>(new Poison("Würger", Color.red, false));
		try {
			Gift.pour(300);
		} catch (NotEnoughCapacityException n) {
			System.out.println(n.getMessage());
			System.out.println("So viel passt rein: " + n.kappazität);
			System.out.println("So viel willst du rein machen: " + n.volume);
		}
		System.out.println("Inhalt nach Operation 1: " + Gift.volume);
		
		
		
		try {
			Gift.takeOut(600);
			} catch (NotEnoughLiquidException n) {
				System.out.println(n.getMessage());
				System.out.println("So viel ist vorhanden: " + n.volume);
				System.out.println("So viel soll raus: " + n.out);
			}
		System.out.println("Inhalt nach Operation 2: " + Gift.volume);
		
		
		
		try {
			Gift.drink(500);
			} catch (NotEnoughLiquidException n) {
				System.out.println(n.getMessage());
				System.out.println("So viel ist vorhanden: " + n.out);
				System.out.println("So viel möchtest du trinken: " + n.volume);
			
			} catch (UndrinkableException u) {
				if (!u.d) {
					System.out.println(u.getMessage());
				} else {
					System.out.println("Kann man trinken, aber die Temperatur beträgt: " + u.temperature);
				}	
			}
		System.out.println("Inhalt nach Operation 3: " + Gift.volume);
	}
}
