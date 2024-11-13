// cd slip6
// javac MatrixTranspose.java
// java MatrixTranspose
// Write a java program to display transpose of a given matrix. 

import java.util.Scanner;

public class MatrixTranspose {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of rows in the matrix: ");
        int rows = scanner.nextInt();
        System.out.print("Enter the number of columns in the matrix: ");
        int columns = scanner.nextInt();
        
        int[][] matrix = new int[rows][columns];
        
        System.out.println("Enter the elements of the matrix:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        
        System.out.println("The original matrix is:");
        displayMatrix(matrix);
        
        int[][] transpose = calculateTranspose(matrix);
        
        System.out.println("The transpose of the matrix is:");
        displayMatrix(transpose);
        
        scanner.close();
    }
    
    // Function to calculate the transpose of a matrix
    public static int[][] calculateTranspose(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        
        int[][] transpose = new int[columns][rows];
        
        for (int i = 0; i < columns; i++) {
            for (int j = 0; j < rows; j++) {
                transpose[i][j] = matrix[j][i];
            }
        }
        
        return transpose;
    }
    
    // Function to display a matrix
    public static void displayMatrix(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
