def solution(n):

    if n < 3: return n  
    a = 1
    b = 2
    c = 0
    for i in range(2,n):
        c = a+b
        a = b
        b = c

    return b % 1234567


print(solution(4))
print(solution(3))