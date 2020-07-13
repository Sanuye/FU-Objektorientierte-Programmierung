//bearbeitet von Jasmine Cavael & Alexander Chmielus
//Tutorium 10, Fabian Halama (Do. 16-18)
//Aufgabe 1b)


package u7;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class Captive implements Shape, Animation {
	double radius;
	Point center;
	Random rand;
	ShapesWorld welt;
	Color color;
	
	public Captive() {
		this.radius = 20;
		this.center = new Point();
		this.rand = new Random();
		this.color = Color.GREEN;
	}
	
	public Color getColor() {
		return color;
	}
	
	public void play() {
		int new_x = rand.nextInt(7)-3;		//Zahlen von -3 bis 3 sind möglich
		int new_y = rand.nextInt(7)-3;
		center.x = center.x  + new_x;
		center.y = center.y + new_y;
	}
	
	public void draw(Graphics g) {
		g.setColor(this.color);
		int x = (int) center.x;				//fillOval braucht ints statt doubles
		int y = (int) center.y;
		int width = (int) this.radius;		//Wir wollen einen Kreis zeichnen, also ist Höhe = Breite
		int height = (int) this.radius;
		g.fillOval(x, y, width, height);
	}
	
	public double getRadius() {
		return radius;
	}
	
	public Point getCenter() {
		return center;
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
