from collections import Counter

def solution(k, tangerine):

    a = Counter(tangerine)
    a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))

    c = 0
    for key, value in a.items():
        
        if(k - value > 0):
            k -= value
            c += 1
            continue
        else :
            c += 1
            return c
    

print(solution(6,	[1, 3, 2, 5, 4, 5, 2, 3]	))