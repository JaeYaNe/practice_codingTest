def solution(k, dungeons):
    visited = [False] * len(dungeons)
    ans = 0

    def dfs(current_k, count):
        nonlocal ans
        ans = max(ans, count)

        for i in range(len(dungeons)):
            # 방문하지 않았고, 필요 피로도가 충족될 때
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                dfs(current_k - dungeons[i][1], count + 1)
                visited[i] = False # 백트래킹 (다음 경우의 수를 위해)

    dfs(k, 0)
    return ans


print(solution(80,	[[80,20],[50,40],[30,10]]))