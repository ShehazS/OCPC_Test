import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // Print the name in uppercase
        System.out.println(nametoupper("hasna"));

        // Add a pause, waiting for the user to press Enter to close
        System.out.println("Press Enter to close the program...");
        Scanner scanner = new Scanner(System.in);
        scanner.nextLine(); // Waits for the user to press Enter
        scanner.close(); // Close the scanner
    }

    public static String nametoupper(String name) {
        name = name.toUpperCase();
        return name;
    }
}
