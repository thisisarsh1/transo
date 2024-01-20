import java.util.Arrays;
import java.util.Scanner;

public class max {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] arr =new int[6];
            for (int i = 0; i < arr.length; i++) {
            arr[i]= in.nextInt();
            }
        reverse(arr);
        System.out.println(Arrays.toString(arr));
    }
static void reverse(int[] arr){
        int start=0;
        int end=(arr.length)-1;
        while(start<end){
            swap(arr,start,end);
            start++;
            end--;
        }

}
static void swap(int[] arr, int  idx1 ,int idx2){
        int temp = arr[idx1];
    arr[idx1] =arr[idx2];
    arr[idx2]=temp;
}

}

