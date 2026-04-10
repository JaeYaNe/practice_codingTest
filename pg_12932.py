def solution(n):

    int_list = [int(i) for i in str(n)]
    answer = [0] * len(int_list)

    answer = int_list[::-1]

    return answer

def solution1(n):

    int_list = [int(i) for i in str(n)]
     
    return list(reversed(int_list))

print(solution(12345))
print(solution1(6789))