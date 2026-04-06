import java.util.ArrayList;

public class pg_181918 {
    public static int[] solution(int[] arr) {
        ArrayList<Integer> arrayList = new ArrayList<>();

        int i = 0;
        while(i < arr.length){
            if(arrayList.isEmpty()) {
                arrayList.add(arr[i]);
                i++;
            } else {
                if(arrayList.get(arrayList.size()-1) < arr[i]) {
                    arrayList.add(arr[i]);
                    i++;
                }
                else if(arrayList.get(arrayList.size()-1) >= arr[i]) arrayList.remove(arrayList.size()-1);
            }
        }

        //int[] stk = new int[arrayList.size()];
        int[] stk = arrayList.stream().mapToInt(Integer::intValue).toArray();

        return stk;
    }

    public static void main(String[] args) {

        int[] list = new int[]{1, 4, 2, 5, 3};
        solution(list);
        ;
    }
}