import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
       Scanner inp = new Scanner(System.in);
        System.out.println("enter Target");
        int target = inp.nextInt();

        int[] arr = new int[5];
        System.out.println("enter arrey");

        for (int i = 0; i < arr.length; i++) {
            arr[i]= inp.nextInt();

        }

        int ans = search(arr,target);
        System.out.println(ans);



    }
    static int search (int[] arr , int target) {
        for (int i : arr) {
            if (arr[i] == target) {
                return i;
            }



        }
        return -1;

    }}