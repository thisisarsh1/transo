import java.util.Scanner;

public class range {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        System.out.println("enter starting range");
        int start =in.nextInt();
        System.out.println("enter ending range");
        int end =in.nextInt();
        int target= 1;
        int[] inx = {18,15,55,8,484,1};

        int ans=check(inx,start,end,target);
        System.out.println(ans);

    }
    static int check( int[] ints,int start ,int end,int target){
        for (int i = 0; i <ints.length; i++) {
            if(ints[i]==target){

                return ints[i];
            }


       }
        return -1;

    }
}
