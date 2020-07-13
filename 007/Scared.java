//bearbeitet von Jasmine Cavael & Alexander Chmielus
//Tutorium 10, Fabian Halama (Do. 16-18)
//Aufgabe 1d)
//Klappt als einzige Klasse nicht so besonders gut. Interaktion mit anderen Objekten klappt nur abhängig vom Objekt gut. Da wir aber aufgrund anderer Kurse und Projektabgaben wenig Zeit für diesen (sehr umfangreichen)
//Zettel hatten, lassen wir das so stehen.
//Das Zittern haben wir absichtlich weggelassen und in Steine zerfallen haben wir weggelassen, da ja nicht mal das springen richtig klappt.


package u7;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;


//Wir implementieren Scared-Objekte als Quadrate.
public class Scared implements Shape, Animation{
	int x, y, width, height;
	ShapesWorld welt;
	Random rand;
	Color color;
	boolean swap = true;
	
	public Scared() {
		this.x = -30;
		this.y = -30;
		this.width = 30;
		this.height = 30;
		this.rand = new Random();
		this.color = Color.ORANGE;
	}
	
	public void draw(Graphics g) {
		g.setColor(color);
		g.fillRect(x, y, width, height);
	}
	
	public void play() {
		//Mindestens 1 Objekt muss in der Nähe sein, damit was passiert. Wir können uns also auf das näheste beschränken
		Shape enemy = this.welt.getClosestShape(this);
		//Schaue, ob eine der der äußersten Punkte des das Objekt umrahmenden Kreises in der Nähe sind
		//Zuerst holen wir die Werte der äußersten Punkte des das nähesten Objekt umrahmenden Kreises
		double enemy_r = enemy.getRadius();
		double enemy_x = enemy.getCenter().x;
		double enemy_y = enemy.getCenter().y;
		double enemy_right = enemy_x + enemy_r;
		double enemy_left = enemy_x - enemy_r;
		double enemy_top = enemy_y - enemy_r;
		double enemy_bottom = enemy_y + enemy_r;
		
		double scared_r = getRadius();
		double scared_x = getCenter().x;
		double scared_y = getCenter().y;
		double scared_right = scared_x + scared_r;
		double scared_left = scared_x - scared_r;
		double scared_top = scared_y - scared_r;
		double scared_bottom = scared_y + scared_r;
		
		if (enemy_right < scared_left || enemy_left > scared_right || enemy_top > scared_top || enemy_bottom < scared_bottom) {
		}
		else {
			x = rand.nextInt(200)-100;
			y = rand.nextInt(200)-100;
		}
	}
	
	public boolean contains(double x, double y) {
		if (x<(this.getCenter().x-width) || x>this.getCenter().x+width || y<(this.getCenter().y-height) || y>(this.getCenter().y+height))
		    return false;
		else
			return true;
	}
	//Der Radius des Kreises um ein Quadrat entspricht der Hälfte der Diagonale des Quadrats.
	public double getRadius() {
		double durchmesser = width * Math.sqrt(2);
		return (durchmesser/2);
	}
	
	public Color getColor() {
		return color;
	}
	
	//Der Mittelpunkt des Quadrats hat die Koordinaten, die dem Punkt als Parameter übergeben werden.
	public Point getCenter() {
		return new Point((x+width)/2, (y+height)/2);
	}
	
	public void setShapesWorld(ShapesWorld welt) {
		this.welt = welt;
	}
	
	public void userClicked(double atX, double atY) {
		this.welt.addShape(new Scared());
	}
	
	public void userTyped(char key) {
		return;
	}
	
	public void moveTo(double x, double y) {
		this.getCenter().x = (int) x;
		this.getCenter().y = (int) y;
	}
}
