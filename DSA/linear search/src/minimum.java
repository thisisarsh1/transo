public class minimum {
    public static void main(String[] args) {
        int[] arr={1111,88,4,55,88,9,3,4};
        int ans= mini(arr);
        System.out.println(ans);
    }
    static int mini(int[] arrs){
        int x=10000000;
        for (int i = 0; i < arrs.length; i++) {
            if(arrs[i]<x){
                x=arrs[i];


            }}
            return x;

    }
}
