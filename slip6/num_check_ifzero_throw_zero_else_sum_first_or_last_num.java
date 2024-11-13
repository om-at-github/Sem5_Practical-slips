// cd slip6
// javac num_check_ifzero_throw_zero_else_sum_first_or_last_num.java
// java num_check_ifzero_throw_zero_else_sum_first_or_last_num

// Write a java program to accept a number from user, if it zero then  throw user 
// defined Exception “Number Is Zero”, otherwise calculate the sum of first and last digit
// of that number. (Use static keyword)

import java.util.Scanner;
class num_check_ifzero_throw_zero_else_sum_first_or_last_num {
    public static void main(String[] args) {
        try (Scanner S = new Scanner(System.in)) {
            System.out.println("Enter a number: ");
            int num=S.nextInt();
            if (num == 0) {
                    System.out.println("Number is zero");
                }
            else{
                int last_no = num % 10;
                System.out.println("last no is"+last_no);
                int first_no = 0;
                while(num>0){
                    first_no = num % 10;
                    num = num / 10;
                }
                System.out.println("first no is" + first_no);
                int sum = first_no + last_no ;
                System.out.println("sum of first and last digit of number is "+sum);
            }    
        }
}
}