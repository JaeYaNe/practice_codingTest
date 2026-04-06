public class pg_181913 {
    public static String solution(String my_string, int[][] queries) {

        for(int[] query : queries){
            String str0 = my_string.substring(0, query[0]);
            String str1 = my_string.substring(query[0], query[1]+1);
            String str2 = my_string.substring(query[1]+1);
            String reversed = "";

            for (int i = str1.length() - 1; i >= 0; i--) {
                reversed += str1.charAt(i);
            }
            my_string = str0 + reversed + str2;
        }

        return my_string;
    }

    public static void main(String[] args) {
        int[][] queries = {{2, 3}, {0, 7}, {5, 9}, {6, 10}};

        System.out.println(solution("rermgorpsam", queries));
    }
}