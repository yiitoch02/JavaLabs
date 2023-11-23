public class ExceptionHandlingDemo extends Exception{
    private double radius;

 /** Construct an exception */
    public ExceptionHandlingDemo(double radius) {
        super("Invalid radius " + radius);
        this.radius = radius;
    }

 /** Return the radius */
    public double getRadius() {
    return radius;
    }
 }