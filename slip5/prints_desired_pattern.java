// javac prints_desired_pattern.java
// java prints_desired_pattern
// Write a java program to display following pattern:
//5
//4 5
//3 4 5
//2 3 4 5
//1 2 3 4 5

public class prints_desired_pattern {
        public static void main(String[] args) {
            int rows = 5;
            
            // Outer loop for rows
            for (int i = 1; i <= rows; i++) {
                int num = i;
                
                // Inner loop for printing numbers
                for (int j = 1; j <= i; j++) {
                    System.out.print(num + " ");
                    num++;
                }
                
                // Move to the next line after each row is printed
                System.out.println();
            }
        }
}
