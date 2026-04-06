def solution(arr):
    
    n = len(arr)
    for i in range(n) :
        for j in range(n):
            if(arr[i][j] != arr[j][i]) : return 0
        
    return 1

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))