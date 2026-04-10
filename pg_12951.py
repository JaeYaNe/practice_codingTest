def solution(s):
    answer = ''

    str_list = s.split(" ")
    
    for i in range(len(str_list)):
        str_list[i] = str_list[i].capitalize()

    answer = " ".join(str_list)

    return answer

print(solution("3people unFollowed me")) 
print(solution(" 3people unFollowed me ")) 
print(solution("for the last week"))
print(solution("for the last a week"))