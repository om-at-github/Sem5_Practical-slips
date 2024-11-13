// cd slip4

// javac display_alternate_character_given_string.java
// java display_alternate_character_given_string

// Write a java program to display alternate character from a given string



import java.util.Scanner;

public class  display_alternate_character_given_string{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for input
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        // Display alternate characters
        System.out.print("Alternate characters: ");
        for (int i = 0; i < input.length(); i += 2) {
            System.out.print(input.charAt(i));
        }

        // Close the scanner
        scanner.close();
    }
}
