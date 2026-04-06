def solution(myString):
    char_list = list(myString)
    
    for i in range(len(char_list)):
        if char_list[i] < 'l':
            char_list[i] = 'l'
            
    return "".join(char_list)


print(solution("abcdevwxyz"))
print(solution("jjnnllkkmm"))