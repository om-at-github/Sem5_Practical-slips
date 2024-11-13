// cd slip9
// javac display_num_pattern.java
// java display_num_pattern

// Write a java Program to display following pattern:
// 1
// 0 1
// 0 1 0
// 1 0 1 0

public class display_num_partten {
        public static void main(String[] args) {
            int rows = 4; // Number of rows in the pattern
            
            // Loop through each row
            for (int i = 0; i < rows; i++) {
                int num = (i % 2 == 0) ? 1 : 0; // Determine starting number (1 for even rows, 0 for odd rows)
                
                // Loop through each column in the current row
                for (int j = 0; j <= i; j++) {
                    System.out.print(num + " "); // Print the current number followed by a space
                    num = (num == 1) ? 0 : 1; // Flip the number (1 to 0 or 0 to 1)
                }
                
                System.out.println(); // Move to the next line after each row is printed
            }
        }
    }