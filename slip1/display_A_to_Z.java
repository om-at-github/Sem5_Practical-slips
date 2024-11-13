// cd slip1
// javac display_A_to_Z.java
// java display_A_to_Z

public class display_A_to_Z {
    public static void main(String[] args) {
        // ASCII value of 'A' is 65 and 'Z' is 90
        int start = 'A'; 
        int end = 'Z';   

        for (int i = start; i <= end; i++) {
            char ch = (char) i; 
          
            System.out.print(ch + " ");
        }
        
        System.out.println();
    }

}

