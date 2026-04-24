def solution(citations):
    
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i+1: return i
    
    return len(citations)

print(solution([3, 0, 6, 1, 5, 10]))