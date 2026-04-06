import java.util.*;
import java.math.*;

public class pg_181916 {
    public static int solution(int a, int b, int c, int d) {
        int[] list = new int[]{a,b,c,d};

        Map<Integer, Integer> map = new HashMap<>();

        for (int num : new int[]{a, b, c, d}) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // {1: 1, 4: 2, 5: 1}일때 keys = [1, 4, 5] 할당.
        List<Integer> keys = new ArrayList<>(map.keySet());
        /*
            keys를 sort하는데, list에서 저장된 키값 1, 4를 가지고 map에서 각 val를 가져와 비교
            val이 큰 값이 앞으로
            같다면 return에서 키값 비교로 큰 키값이 앞으로
        */
        keys.sort((k1, k2) -> {
            if (map.get(k1) != map.get(k2)) {
                return map.get(k2) - map.get(k1); // 빈도수 높은 순
            }
            return k2 - k1; // 빈도수 같으면 눈이 큰 순
        });

        int size = map.size();
        if (size == 1) { // 다 같음 (종류 1개)
            return 1111 * keys.get(0);
        }else if (size == 2) { // 종류 2개
            int p = keys.get(0);
            int q = keys.get(1);
            if (map.get(p) == 3) { // 3개, 1개
                return (int) Math.pow(10 * p + q, 2);
            } else { // 2개, 2개
                return (p + q) * Math.abs(p - q);
            }
        } else if (size == 3) { // 종류 3개
            return keys.get(1) * keys.get(2);
        } else { // 다 다름 (종류 4개)
            return Collections.min(map.keySet());
        }
    }

    public static void main(String[] args) {
        System.out.println(solution(2,2,2,2));
        ;
    }
}