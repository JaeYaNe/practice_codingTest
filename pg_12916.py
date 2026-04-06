def solution(s):
    char_list = list(s)

    p_cnt = 0
    y_cnt = 0

    for i in range(len(char_list)):
        upper_char = char_list[i].upper()
        if upper_char == 'P' : p_cnt += 1
        elif upper_char == 'Y' : y_cnt += 1

    return p_cnt == y_cnt

# 게시판 참고
def solution1(s):
   return s.lower().count('p') == s.lower().count('y')


print(solution('Hello Python'))
print(solution('Hello Pyython'))
print(solution1('Hello Python'))
print(solution1('Hello Pyython'))