from collections import deque

def is_valid(s):
    stack = []
    # 짝이 맞는지 확인하기 위한 딕셔너리
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        # 열린 괄호는 스택에 추가
        if char in "({[":
            stack.append(char)
        else:
            # 닫힌 괄호인데 스택이 비어있거나 짝이 안 맞으면 False
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    answer = 0
    queue = deque(s)
    
    # 문자열 길이만큼 회전하며 검사
    for _ in range(len(s)):
        if is_valid(queue):
            answer += 1
        # 왼쪽으로 1칸 회전 (abc -> bca)
        queue.rotate(-1)
        
    return answer