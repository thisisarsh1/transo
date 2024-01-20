//import java.lang.runtime.SwitchBootstraps;
import java.util.Scanner;

public class New {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String inp = in.next();

        switch (inp) {
            case "Home" -> System.out.println("Virar");
            case "College" -> System.out.println("Bandra");
            case "Gym" -> System.out.println("clubone");
            default -> System.out.println("jo diya hai usme se likh:");
        }
    }
}
