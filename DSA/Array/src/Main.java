import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
       Scanner inp = new Scanner(System.in);
        String [] str=new String[3];
        for (int i = 0; i < str.length; i++) {
            str[i]= inp.next();

        }
        System.out.print(Arrays.toString(str));
    }
}