//bearbeitet von Jasmine Cavael & Alexander Chmielus
//Tutorium 10, Fabian Halama (Do. 16-18)
//Aufgabe 1b)


package u7;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class Feuerwerk implements Shape, Animation {
	double radius;
	int x, y;
	Point center;
	Random rand;
	ShapesWorld welt;
	Color color;
	boolean clicked = true;
	
	//Nicht der beste Stil, alles Hard zu coden, aber es funktioniert so und wird fristgerecht fertig.
	public Feuerwerk() {
		this.radius = 30;
		this.center = new Point(72.0, 72.0);
		this.rand = new Random();
		this.color = Color.RED;
	}
	
	public Color getColor() {
		return color;
	}
	
	public void play() {
		return;
	}
	
	public void draw(Graphics g) {
		g.setColor(color);
		x = 42;
		y = 42;
		int width = (int) this.radius*2;		//Wir wollen einen Kreis zeichnen, also ist Höhe = Breite
		int height = (int) this.radius*2;
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
	//"Alle Richtungen" ist ein sehr weiter Begriff. Wir haben uns hier auf 8 Richtungen beschränkt, prinzipiell ginge aber mehr.
	public void userClicked(double atX, double atY) {
		Feuerwerk f = this;
		this.welt.removeShape(f);
		this.welt.addShape(new Bunte(atX, atY, 1, 0));
		this.welt.addShape(new Bunte(atX, atY, 1, 1));
		this.welt.addShape(new Bunte(atX, atY, 0, 1));
		this.welt.addShape(new Bunte(atX, atY, -1, 1));
		this.welt.addShape(new Bunte(atX, atY, -1, 0));
		this.welt.addShape(new Bunte(atX, atY, -1, -1));
		this.welt.addShape(new Bunte(atX, atY, 0, -1));
		this.welt.addShape(new Bunte(atX, atY, 1, -1));
		
		
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
