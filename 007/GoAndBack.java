//bearbeitet von Jasmine Cavael & Alexander Chmielus
//Tutorium 10, Fabian Halama (Do. 16-18)
//Aufgabe 1a)


package u7;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Polygon;

//Da nichts konkretes über das Aussehen dieser Objekte gesagt wurde, orientieren wir uns an den Dreiecken der Around-Klasse.
public class GoAndBack implements Shape, Animation {
	double radius;
	Point center;
	Color color;
	ShapesWorld welt;
	double speed = 5.0;
	boolean go_left = false;
	boolean go_right = true;
	
	public GoAndBack() {
		this.radius = 25;
		this.color = Color.MAGENTA;
		this.center = new Point();
	}
	
	public Color getColor() {
		return color;
	}
	
	public void moveTo(double x, double y) {
		center.x = (int) x;
		center.y = (int) y;
	}
	
	public void setShapesWorld(ShapesWorld world) {
		this.welt = world;
	}
	
	public void fillTriangle(Graphics g, double x, double y, double w, double h) {
		int[] x_coords = {(int) (x+w/2), (int) (x), (int) (x+w)};
		int[] y_coords = {(int) (y), (int) (y+h), (int) (y+h)};
		Polygon p = new Polygon(x_coords, y_coords, 3);
		g.fillPolygon(p);
	}
	
	public void draw(Graphics g) {
		g.setColor(color);
		fillTriangle(g, center.x-radius, center.y-radius, radius*2, radius*2);
	}
	
	public Point getCenter() {
		return center;				
	}
	
	public void userClicked(double atX, double atY) {
		return;
	}
	
	public void userTyped(char key) {
		return;
	}
	
	public void play() {
		if (center.x + radius >= welt.getMax_X()) {
			go_left = true;
			go_right = false;
		}
		if(center.x - radius <= welt.getMin_X()) {
			go_right = true;
			go_left = false;
		}
		if (go_left) {
			center.x = center.x - speed;
		}
		else if (go_right) {
			center.x = center.x + speed;
		}
		return;
	}
	
	public boolean contains(double x, double y) {
		if (x<(center.x-radius) || x>center.x+radius || y<(center.y-radius) || y>(center.y+radius))
		    return false;
		else
			return true;
	}
	
	public double getRadius() {
		return radius;
	}	
}







