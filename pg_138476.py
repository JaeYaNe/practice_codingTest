from collections import Counter

def solution(k, tangerine):
    # 1. 개수 세기
    counts = Counter(tangerine)
    
    # 2. 개수(value)만 뽑아서 내림차순 정렬 (key는 사실 몰라도 되니까요!)
    sorted_counts = sorted(counts.values(), reverse=True)
    
    answer = 0
    for count in sorted_counts:
        k -= count  # 일단 뺀다
        answer += 1 # 종류 하나 추가
        if k <= 0:  # 다 채웠으면 종료
            break
            
    return answer

print(solution(6,	[1, 3, 2, 5, 4, 5, 2, 3]	))