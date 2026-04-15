def solution(n):
    ans = n
    jp = 0

    while True:

        if ans == 0 :
            return jp
        
        elif ans % 2 == 0 : 
            ans /= 2
        else :
            jp +=  1
            ans -= 1


print(solution(5))
print(solution(6))
print(solution(5000))