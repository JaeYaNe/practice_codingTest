def solution(elements):
    result = set() 
    size = len(elements)
    
    for i in range(size):  
        ssum = 0           
        for j in range(size):
            idx = (i + j) % size
            ssum += elements[idx]  


            result.add(ssum)     
            print(result)  
        
    return len(result) 

print(solution([7, 9, 1, 1, 4])) 