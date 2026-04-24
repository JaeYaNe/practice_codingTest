import math

def solution(n, words):

    answer = []
    last_word = words[0]
    
    a = set()
    a.add(last_word)

    
    for i in range(1, len(words)):
        idx = i+1

        if(last_word[-1:] != words[i][:1] or words[i] in a):
            if(idx%n == 0): return [n, math.ceil(idx/n)]
            else : return [idx%n, math.ceil(idx/n)]
            
        else :
            last_word = words[i]
            a.add(last_word)
            
    return [0,0]



print(solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,	["hello", "one", "even", "never", "now", "world", "draw"]))

