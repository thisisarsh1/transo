import java.util.Arrays;
import java.util.Scanner;

public class Swap {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int[] arr=new int[6];
        System.out.println("enter the array");
        for (int i = 0; i < arr.length; i++) {
            arr[i]= in.nextInt();

        }
        System.out.println("give index 1");
        int a = in.nextInt();
        System.out.println("give index 2");
        int b = in.nextInt();

        swap(arr,a,b);
        System.out.println(Arrays.toString(arr));
    }

    static void swap(int[] arr , int inx1 , int inx2) {
    int temp = arr[inx1];
    arr[inx1] =arr[inx2];
    arr[inx2]= temp;

    }
}

