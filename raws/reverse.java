//!eman Ruoy Esrever (java)
/* Author: Md. Nuruzzaman Khan */

import java.util.Scanner;

public class reverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String nam = sc.nextLine();
        sc.close();
        System.out.print("Reverse:");
        String name = nam.concat(" ");
        int l = name.length();
        int xm = 0;
        for (int i = l; i > 0; i--) {
            String str = name.substring(i - 1, i);
            if (xm == 1 && str.isBlank() == false ) {
                System.out.print(str.toUpperCase());
                xm = 0;
            } else if (str.isBlank() == true) {
                System.out.print(str);
                xm = 1;
            } else {
                System.out.print(str.toLowerCase());
            }
        }
    }
}

// OUTPUT:

// Enter your name: Nuruzzaman 
// Reverse: Namazzurun

// Enter your name: !eman Ruoy Esrever
// Reverse: Reverse Your Name!

