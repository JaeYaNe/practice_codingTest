from collections import Counter

def solution(X, Y):
    answer = ''
    cnt = [0] * 10 

    for i in range(10):
        x_cnt = X.count(str(i))
        y_cnt = Y.count(str(i))
        cnt[i] = min(x_cnt, y_cnt) 

    for i in range(9, -1, -1):
        if cnt[i] > 0:
            answer += str(i) * cnt[i] 

    if answer == '': return "-1"
    if answer[0] == '0': return "0" 
    
    return answer


# 게시판 참고 (시간복잡도 해결)
def solution1(X, Y):
    answer = ''
    cnt = [0] * 10 

    x_cnt = Counter(X)
    y_cnt = Counter(Y)

    for i in range(9, -1, -1):
        char = str(i)
        common_count = min(x_cnt[char], y_cnt[char])
        answer += char * common_count

    if not answer: return "-1"
    if answer[0] == "0": return "0"
    
    return answer



print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "425315"))
print(solution1("100", "2345"))
print(solution1("100", "203045"))
print(solution1("100", "123450"))
print(solution1("12321", "425315"))