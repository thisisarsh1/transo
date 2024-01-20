import java.util.Arrays;
import java.util.Scanner;

public class twod {
    public static void main(String[] args) {
        Scanner in= new Scanner(System.in);
        int[][]arr={
                {11,55,854},
                {66,369,84,82},
                {85,27,95}
        };
        System.out.println("enter the number:");
        int target = in.nextInt();
        int[] ans =check(arr,target);
        System.out.println(Arrays.toString(ans));
    }
    static int[] check(int[][] arr,int target){
        for (int rows = 0; rows < arr.length; rows++) {
            for (int col = 0; col < arr[rows].length; col++) {
                if(arr[rows][col]==target){
                    return new int[] {rows,col};
                }
            }
        }
        return new int[]{-1,-1};
    }
}
