def solution(absolutes, signs):
    answer = 0

    n = len(absolutes)
    for i in range(n):
        if(signs[i]) :
            answer += absolutes[i]
        else :
            answer -= absolutes[i]

    return answer


solution([4,7,12], [true,false,true])