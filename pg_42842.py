def solution(brown, yellow):
    total_size = brown + yellow
    
    for h in range(3, int(total_size**0.5) + 1):
        if total_size % h == 0:  
            w = total_size // h
            
            if (w - 2) * (h - 2) == yellow:
                return [w, h]

print(solution(10, 2))