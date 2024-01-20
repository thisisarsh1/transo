public class string {
    public static void main(String[] args) {
        String str ="Rehbar";
        char x= 'k'  ;
                boolean ans=check(str,x);
        System.out.println(ans);
    }
    static boolean check(String str ,char x){
        if (str.isEmpty()){
            return false;
        }
//        for (int i = 0; i <str.length() ; i++) {
//
//            if (str.charAt(i)==x){
//                return true;
//            }
//        }return false;
        for(int j :str.toCharArray()){
            if (j==x){
                return true;
            }

        }
        return false;
    }
}
