//Übung 06
//bearbeitet von Jasmine Cavael & Alexander Chmielus
//Tutorium 10, Fabian Halama (Do. 16-18)

/*Aufgabe 1*/

/*
def root(n):

 {P = n > 0}

 {Q2'} = {((k^2 - (k-2 - 2) -4 ) < n = (k^2 - (2k -2) - 1)}
 {Q2}  = {((k-1) -1)^2 < n = (k-1)^2}

	r = 0 
	
 {Q1} = {((k-1) -1)^2 < n = (k-1)^2}	
	
	k = 1

 {Q} = {(k -1)^2 < n = k^2}

			{INV ^ B} && INV} durch Konsequenzregel gegeben --> while Schleife korrekt!!!!
			
			{INV } = {r == S(k -1) ? (S(k -1) + S(k - 2)) < n}

			while (r + r + k) < n:

			{INV ? B} = {(r == S(k -1) ? (S(k -1) + S(k - 2)) < n) ? (r + r + k) < n}	

			{INV2`} Konsequenzregel {INV ^ B}
			{INV2`} = {  (r == S(k -1) ? (S(k)    + S(k - 1)) < n) ? ((r+k) + (r+k) + (k+1)) = n}
			{INV2} = {((r+k) == S((k+1) -1) ? (S((k+1) -1) + S((k+1) - 2)) < n) ? ((r+k) + (r+k) + (k+1)) = n}
	
				r = r + k
		
			{INV1} = {(r == S((k+1) -1) ? (S((k+1) -1) + S((k+1) - 2)) < n) ? (r + r + (k+1)) = n}	
		
				k = k + 1 
	
			{INV ? ¬B} = {(r == S(k -1) ? (S(k -1) + S(k - 2)) < n) ? (r + r + k) = n}
 
 
 {Q} = {(k -1)^2 < n = k^2}

 return k 


*/

//Aufgabe 2 a) + b)

package u6;

public class Rectangle {
int x, y, width, height;


public Rectangle(int x, int y, int width, int height) {
	this.x = x;
	this.y = y;
	this.width = width;
	this.height = height;
	}


public Rectangle() {
	this(0, 0, 100, 100);
	}

//Aufgabe 2 c)

public Rectangle clone() {
	Rectangle r = new Rectangle(this.x, this.y, this.width, this.height);
	return r;
}

public boolean equal(Rectangle r) {
	if(this.x == r.x && this.y == r.y && this.width == r.width && this.height == r.height) {
		return true;
	}
	else {
		return false;
	
	}
}

public int compareAreaTo(Rectangle r) {
	int area1 = this.width * this.height;	//Fläche des 1. Rechtecks
	int area51 = r.width * r.height;		//Fläche des 2. Rechtecks
	if (area1 == area51) {					//Vergleich
		return 0;
	} else if (area1 > area51) {
		return 1;
	} else {
		return -1;
	}
}

public boolean contains(Rectangle r) {
	if(r.x > this.x && r.x < this.x + this.width && r.x + r.width > this.x && r.x + r.width < this.x + this.width 
		&& r.y > this.y && r.y < this.y + this.height && r.y + r.height > this.y && r.y + r.height < this.y + this.height){
		return true;
	}
	else {
		return false;
	}
}

public boolean overlaps(Rectangle r) {
//Wenn mind. 2 Seiten von r teilweise, oder komplett im Rechteck liegen, gibt es eine Überlappung.
//Eigentlich wäre es ja keine Überlappung, wenn ein Rechteck komplett im anderen ist (= 4 Seiten enthalten), aber Esponda sieht das anscheinend anders. Daher nehmen wir das mit rein
//x und y markieren den Punkt der linken oberen Ecke.
//Das sind die 4 Seiten des 1. Rechtecks:
	int first_left = this.x;
	int first_right = this.x + this.width;
	int first_top = this.y;
	int first_bottom = this.y + this.height;
//jetzt die Seiten des 2. Rechtecks:
	int second_left = r.x;
	int second_right = r.x + r.width;
	int second_top = r.y;
	int second_bottom = r.y + r.height;
	boolean left = false, right = false, top = false, bot = false;
//Test, ob eine Seite des 2. Rechtecks im 1. enthalten ist
	if (second_left >= first_left && second_left <= first_right) {
		left = true;
	}
	if (second_right >= first_left && second_right <= first_right) {
		right = true;
	}
	if (second_top >= first_top && second_top <= first_bottom) {
		top = true;
	}
	if (second_bottom >= first_top && second_bottom <= first_bottom) {
		bot = true;
	}
//Test, ob mindestens 2 Seiten enthalten sind.
	if ((left && right && top && !bot) || (left && right && !top && bot) || (left && !right && top && bot) || (!left && right && top && bot)
		|| (left && right && !top && !bot) || (left && !right && top && !bot) || (left && !right && !top && bot)
		|| (!left && right && top && !bot) || (!left && right && !top && bot) || (!left && !right && top && bot) || (left && right && top && bot)) {
		return true;
	}
	else {
		return false;
	}
}

public Rectangle section(Rectangle r) {
	int new_x = 0, new_y = 0, new_width= 0, new_height = 0;
	if (!this.overlaps(r)) {
		return null;
	}
	else {
		if (this.x > r.x) {
			new_x = this.x;
		}
		else {
			new_x = r.x;
		}
		if(this.x + this.width > r.x + r.width) {
			new_width = r.x + r.width - new_x;
		}
		else {
			new_width = this.x + this.width - new_x;
		}
		if (this.y < r.y){
			new_y = r.y;
		}
		else {
			new_y = this.y;
		}
		if (this.y + this.height < r.y + r.height) {
			new_height = this.y + this.height - new_y;
		}
		else {
			new_height = r.y + r.height - new_y;
		}
		Rectangle rect = new Rectangle(new_x, new_y, new_width, new_height);
		return rect;
	}
}


public static Rectangle smallestBoundingRectangle (Rectangle[] recs) {
	int x = recs[0].x, y = recs[0].y, width = recs[0].width, height =recs[0].height, i = 0;
	while (i < recs.length-1) {
		if (x > recs[i+1].x) {		//Am weitesten linke Seite
			x = recs[i+1].x;
		}
		if (y > recs[i+1].y) {		//Höchste Seite
			y = recs[i+1].y;
		}
		if (width < recs[i+1].width + recs[i+1].x) {	//Am weitesten rechte Seite
			width = recs[i+1].width + recs[i+1].x;
		}
		if (height < recs[i+1].y + recs[i+1].height) {	//Tiefste Seite
			height = recs[i+1].y + recs[i+1].height;
		}
		i++;
	}	
	width = width - x;
	height = height - y;
	Rectangle rect = new Rectangle(x, y, width, height);
	return rect;
}

/*
public static void main(String [] args ) {
	Rectangle r1 = new Rectangle();
	Rectangle r2 = new Rectangle(5, -5, 20, 20);
	Rectangle r3 = r2.clone();
	Rectangle r4 = new Rectangle(4, -4, 20, 20);
	boolean e1 = r2.equal(r3);
	boolean e2 = r1.equal(r3);
	int u = r1.compareAreaTo(r2);
	boolean c1 = r1.contains(r2);
	boolean c2 = r2.contains(r1);
	boolean o1 = r2.overlaps(r4);
	boolean o2 = r1.overlaps(r2);
	Rectangle r5 = r2.section(r4);
	Rectangle r6 = r1.section(r2);
	Rectangle[] recs = {r1, r2, r4, r5, r6};
	Rectangle r7 = r1.smallestBoundingRectangle(recs);
	System.out.println(r3);
	System.out.println(e1);
	System.out.println(e2);
	System.out.println(u);
	System.out.println(c1);
	System.out.println(c2);
	System.out.println(o1);
	System.out.println(o2);
	System.out.println(r5);
	System.out.println(r6);
	System.out.println(r7);
}
*/
}

//Aufgabe 3

package u6;

public class Circle {
double x;
double y;
double r;

public Circle(double x, double y, double r) {
	this.x = x;
	this.y = y;
	this.r = r;
}

public static final float pi = 3.141598f;

public static void drawCircle(double x, double y, double r, int count) {
	StdDraw.setPenColor(StdDraw.BLACK);
	Circle c1 = new Circle(x, y, r);
	if (count <= 0) {
		return;
	}
	else {
		StdDraw.filledCircle(c1.x, c1.y, c1.r);
		double r1 = r / 2.0;
		count--;
		drawCircle(x-r, y-r, r1, count);
		drawCircle(x+r, y+r, r1, count);
		drawCircle(x-r, y+r, r1, count);
		drawCircle(x+r, y-r, r1, count);
	}
}

public static void main (String[] args) {
	drawCircle(0.5, 0.5, 0.1, 6);
}
}
