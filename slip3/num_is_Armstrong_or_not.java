// cd slip3
// javac num_is_Armstrong_or_not.java
// java num_is_Armstrong_or_not

import java.util.Scanner;

public class num_is_Armstrong_or_not {

    // Function to check if a number is Armstrong or not
    public static boolean isArmstrong(int number) {
        int originalNumber, remainder, result = 0, n = 0;

        originalNumber = number;

        // Count number of digits
        while (originalNumber != 0) {
            originalNumber /= 10;
            ++n;
        }

        originalNumber = number;

        // Calculate Armstrong sum
        while (originalNumber != 0) {
            remainder = originalNumber % 10;
            result += Math.pow(remainder, n);
            originalNumber /= 10;
        }

        // Check if number is Armstrong
        if (result == number)
            return true;
        else
            return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number to check if it is an Armstrong number: ");
        int number = scanner.nextInt();

        if (isArmstrong(number))
            System.out.println(number + " is an Armstrong number.");
        else
            System.out.println(number + " is not an Armstrong number.");

        scanner.close();
    }
}
