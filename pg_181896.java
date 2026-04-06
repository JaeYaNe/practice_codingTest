import java.util.*;

public class pg_181896 {
    public static String[] solution(String my_string) {

        ArrayList<String> arr = new ArrayList<>();

        for(String str : my_string.split(" ")){
            arr.add(str);
        }

        String[] answer = new String[arr.size()];

        for(int i=0; i<arr.size(); i++){
            answer[i] = arr.get(i);
        }

        return answer;
    }

    public static void main(String[] args) {
        solution("i love you");
    }
}