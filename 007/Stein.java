//bearbeitet von Jasmine Cavael & Alexander Chmielus
//Tutorium 10, Fabian Halama (Do. 16-18)
//Aufgabe 1c)
//Ein Stein wird an der immer gleichen Stelle erzeugt, fällt nach Gravitationsgesetz und zerspringt in kleine Stelle, die logischerweise auch immer an der gleichen Position sind.
package u7;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

//Bei uns gibt es nur kreisrunde Steine
public class Stein implements Shape, Animation {
	double radius;
	int x = -100;
	int y = -100;
	Color color;
	ShapesWorld welt;
	Random rand;
	final double grav = 9.81;						//Gravitationskonstante
	double i = 0.0;
	boolean start = true, hit = false;
	Point center;
	
	public Stein() {
		this.radius = 50;
		this.color = Color.GRAY;
		this.center = this.getCenter();
	}
	
	public void play() {	
		if (center.y + radius >= this.welt.getMax_Y()) {	
			hit = true;
		}
		else {															//Wir verwenden hier die Formel für den freien Fall h = grav*t² / 2, wobei h = Fallstrecke, t = Fallzeit.
			center.y = center.y + ((grav * Math.pow(i * 0.03, 2)) / 2);//Da diese Funktion alle 30 ms aufgerufen wird, müssen wir für t einfach i (Anzahl der Aufrufe) mit 0.03s multiplizieren.
			i++;
		}
	}
	
	public void draw (Graphics g) {
		if (start) {
			center.y = this.welt.getMin_Y();
			start = false;
		}
		if (hit) {
			int i = -2;
			while (i < 4) {
				MiniStein ms = new MiniStein();
				g.setColor(ms.color);
				int ms_x = i * 20;
				int ms_y = (int) this.welt.getMax_Y()- (int) ms.radius;
				int ms_width = (int) ms.radius;
				int ms_height = (int) ms.radius;
				g.fillOval(ms_x, ms_y, ms_width, ms_height);
				i++;
			}
		}
		else {
			g.setColor(color);
			x = (int) center.x - (int) radius;
			y = (int) center.y;
			int width = (int) radius*2;		//Wir wollen einen Kreis zeichnen, also ist Höhe = Breite
			int height = (int) radius*2;
			g.fillOval(x, y, width, height);
		}

	}
	
	public double getRadius() {
		return radius;
	}
	
	public Color getColor() {
		return color;
	}
	
	public Point getCenter() {
		return new Point((x+radius)/2, (y+radius)/2);
	}
	
	public void setShapesWorld(ShapesWorld welt) {
		this.welt = welt;
	}
	
	public void userClicked(double atX, double atY) {
		return;
	}
	
	public void userTyped(char key) {
		return;
	}
	
	public void moveTo(double x, double y) {
		center.x = (int) x;
		center.y = (int) y;
	}
	
	public boolean contains(double x, double y) {
		if (x<(center.x-radius) || x>center.x+radius || y<(center.y-radius) || y>(center.y+radius))
		    return false;
		else
			return true;
	}
}
