import java.util.*;

public class pg_181842 {
    public static int solution(String str1, String str2) {

        for(int i=0; i<=str2.length()-str1.length(); i++){
            if(str1.equals(str2.substring(i, i+str1.length()))) {
                System.out.println(str1);
                System.out.println(str2.substring(i, i+str1.length()));
                return 1;
            }
        }

        return 0;
    }

    public static void main(String[] args) {
        System.out.println(solution("abc", "aabcc"));
        System.out.println(solution("tbt", "tbbttb"));
    }
}