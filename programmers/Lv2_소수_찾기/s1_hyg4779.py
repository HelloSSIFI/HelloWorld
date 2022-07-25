def solution(numbers=str):
    N = len(numbers)
    ans = 0
    '''
    1부터 N개까지 조합을 찾고
    각 개수 별 만들어진 수가 소수인지 찾음
    소수면 ans+=1    
    '''
    def dfs(n=int, tmp=str):
        if n==count:
            if int(tmp)>1:
                arr.add(int(tmp))
            return

        for j in range(N):
            if not vis[j]:
                vis[j] = 1
                dfs(n+1, tmp+numbers[j])
                vis[j] = 0

    arr = set()
    for count in range(1, N+1):
        vis = [0]*N
        for i in range(N):
            vis[i] = 1
            dfs(1, numbers[i])
            vis[i] = 0

    for arg in arr:
        for num in range(2, int(arg**0.5)+1):
            if arg%num==0:
                break
        else:
            ans+=1
    print(ans)
    return ans