def solution(n):
    char_list = list(str(n))
    answer = 0

    for i in range(len(char_list)) :
        answer += int(char_list[i])

    return answer


print(solution(123))