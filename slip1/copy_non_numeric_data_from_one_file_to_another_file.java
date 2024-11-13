// cd slip1
// javac copy_non_numeric_data_from_one_file_to_another_file.java
// java copy_non_numeric_data_from_one_file_to_another_file
// Write a ‘java’ program to copy only non-numeric data from one file to another file.


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class copy_non_numeric_data_from_one_file_to_another_file{

    public static void main(String[] args) {
        String sourceFile = "source.txt";
        String destinationFile = "destination.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(sourceFile));
             BufferedWriter writer = new BufferedWriter(new FileWriter(destinationFile))) {

            String line;
            while ((line = reader.readLine()) != null) {
                String nonNumericData = line.replaceAll("[0-9]", ""); // Remove all numeric characters
                writer.write(nonNumericData);
                writer.newLine(); // Add a newline to keep the format
            }

            System.out.println("Non-numeric data has been copied successfully.");

        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}