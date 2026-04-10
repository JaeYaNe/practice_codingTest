import math

def solution(n):
    qrt_n = math.isqrt(n)

    if qrt_n ** 2 == n :
        return (math.isqrt(n) + 1) ** 2
    else :
        return -1
    


print(solution(121))
print(solution(3))