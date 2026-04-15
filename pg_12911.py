def solution(n):

    n_one_cnt = bin(n).count("1")
    
    target = n + 1

    while True:
        if bin(target).count("1") == n_one_cnt:
            return target
        target += 1


print(solution(78))
print(solution(15))