package u7;

import java.awt.Color;
import java.awt.Graphics;

public class Bunte extends Feuerwerk {
	int new_x, new_y;
	public Bunte(double x, double y, int new_x, int new_y) {
		this.center = new Point(x, y);
		this.radius = 20;
		this.new_x = new_x;
		this.new_y = new_y;
		int c = rand.nextInt(5);
		this.color = Color.BLACK;
		System.out.println(c);
		switch (c) {
			case 0:
				this.color = Color.BLUE;
				break;
			case 1:
				this.color = Color.GREEN;
				break;
			case 2:
				this.color = Color.RED;
				break;
			case 3:
				this.color = Color.YELLOW;
				break;
			case 4:
				this.color = Color.PINK;
				break;
		}
	}
	
	public void play() {
		int new_x = x +  this.new_x;		//Zahlen von -3 bis 3 sind möglich
		int new_y = y +  this.new_y;
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
}
