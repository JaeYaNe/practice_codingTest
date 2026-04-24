def solution(n, left, right):
    answer = []
    
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        
        answer.append(max(i, j) + 1)
        
    return answer


print(solution(4,	7,	14))
print(solution(3,	2,	5))