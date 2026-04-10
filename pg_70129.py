def solution(s):
    zero_cnt = 0
    turn_cnt = 0

    while s != "1":
        turn_cnt += 1
        zeros = s.count("0")
        zero_cnt += zeros
        
        s = bin(s.count("1"))[2:]

    return [turn_cnt, zero_cnt]

print(solution("110010101001")) 