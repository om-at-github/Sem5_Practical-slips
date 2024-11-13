// cd slip11
// javac command_line_arguments_opertor.java
// java command_line_arguments_opertor

// Write a menu driven java program using command line arguments for the following: 
// 1. Addition 
// 2. Subtraction
// 3. Multiplication
// 4. Division

public class command_line_arguments_opertor{
    public static void main(String[] args) {
        num1= int(input("enter the number1 :")) 
        num2= int(input("enter the number2 :"))
        result=0
        operation = input("Enter the operation")

        switch (operation) {
            case +:
                result = num1 + num2;
                System.out.println("Addition result: " + result);
                break;

            case -:
                result = num1 - num2;
                System.out.println("Subtraction result: " + result);
                break;

            case *:
                result = num1 * num2;
                System.out.println("Multiplication result: " + result);
                break;

            case /:
                if (num2 == 0) {
                    System.out.println("Error: Division by zero is not allowed.");
                } else {
                    result = num1 / num2;
                    System.out.println("Division result: " + result);
                }
                break;

            default:
                System.out.println("Invalid operation. Please use 1 for Addition, 2 for Subtraction, 3 for Multiplication, or 4 for Division.");
                break;
        }
    }
}
