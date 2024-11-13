// cd slip3
// javac calculate_area_and_volume_of_Cone_and_Cylinder.java
// java calculate_area_and_volume_of_Cone_and_Cylinder

//Define an abstract class Shape with abstract methods area () and volume (). Derive 
 //abstract class Shape into two classes Cone and Cylinder. Write a java Program 
 //to calculate area and volume of Cone and Cylinder.(Use Super Keyword.)
 // cylinder surface area- A=2πrh
 //cylinder volume - V=πr 
// cone suface area - A=πrs
// cone volume - V=1/3πr2h
 
// abstract class Shape with abstract methods area () and volume ().
import java.util.Scanner;
abstract class Shape{
    void area(int a , int b){};
    void volume(int a, int b){};
}

class Cone extends Shape{
    
    void area(int r,int l){
        
        double area_of_cone=3.14*r*l;
        System.out.println("Area of Cone = " +area_of_cone);
    }
    
    void volume(int r,int h){
        double volume_of_cone=1/3*3.14*r*2*h;
        System.out.println("Volume of Cone = " +volume_of_cone);
    }
}

class Cylinder extends Shape{
    
    void area(int r, int h){
        double areaOFcylinder=2*3.14*r*h;
        System.out.println("Area of Cylinder = " +areaOFcylinder);
    }
   
    void volume(int r,int h){
        double volumeOFcylinder=3.14*r; 
        System.out.println("Volume of Cylinder = " +volumeOFcylinder);
    }
}

class calculate_area_and_volume_of_Cone_and_Cylinder{
   
    public static void main(String[] args) {
    
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("enter the radius = ");
        int r=sc.nextInt();

        System.out.println("enter the length = ");
        int l=sc.nextInt();

        System.out.println("enter the height = ");
        int h=sc.nextInt();
        

        Shape shape1 = new Cone();
        shape1.area(r,l);
        shape1.volume(r,h);

        Shape shape2 = new Cylinder();
        shape2.area(r,h);
        shape2.volume(r,0);

        sc.close();

    }

}
