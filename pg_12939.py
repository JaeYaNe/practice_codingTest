def solution(s):
    answer = ''

    char_list =  s.split()
    int_list = [int(i) for i in char_list]

    int_list.sort()
    answer += str(int_list[0]) + ' '+ str(int_list[-1])

    return answer


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))