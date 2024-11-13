// cd slip2
// javac display_vowels_from_string.java
// java display_vowels_from_string
//Write a java program to display all the vowels from a given string

class display_vowels_from_string{
    public static void main(String[] args) {
         String ch = "Hello World!";
         char[] vowels = {'a', 'e', 'i', 'o', 'u'};
         int count = 0;
         for (int i = 0; i < ch.length(); i++) {
            for (int j = 0; j < vowels.length; j++) {
                if (ch.charAt(i) == vowels[j]) {
                    System.out.print(ch.charAt(i) + " ");
                    count++;
                }
            }
        }
                    System.out.println("Total vowels in the string are: " + count);
    }
}
