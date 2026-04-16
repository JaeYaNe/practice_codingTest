def solution(arr):
    # 최대공약수(GCD)를 구하는 함수 (유클리드 호제법)
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    # 두 수의 최소공배수(LCM)를 구하는 함수
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    answer = arr[0]

    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i]) 
        
    return answer

print(solution([2, 6, 8, 14])) 