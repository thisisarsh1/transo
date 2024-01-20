import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        fxn();
    }
    static int fxn(){
        int sum = 0;
        Scanner n = new Scanner(System.in);
        int num=n.nextInt();
        int og =num;
        while(num>0){
            int last=num%10;
            num=num/10;
             sum = sum + last*last*last;

            }
        return sum;
        }

        }




