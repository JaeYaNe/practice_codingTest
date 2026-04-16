def solution(n):
    answer = 1
    
    for i in range(1, n // 2 + 1):
        current_sum = 0
        next_num = i
        box = str(i) 
        while current_sum < n:
            current_sum += next_num
            next_num += 1
            box += str(next_num)
        if current_sum == n:
            answer += 1
            print(box)

    return answer
    
def solution1(n):
    return len([i for i in range(1, n + 1) if n % i == 0 and i % 2 == 1])


print(solution(15))
print(solution1(15))