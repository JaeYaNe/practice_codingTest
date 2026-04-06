import java.util.ArrayList;

public class pg_181917 {
    public static boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        return (x1 || x2) && (x3 || x4);
    }

    public static void main(String[] args) {
        solution(false,	true,	true,	true);
        ;
    }
}