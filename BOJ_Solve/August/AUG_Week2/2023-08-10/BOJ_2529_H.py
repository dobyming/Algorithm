# 부등호를 만족하는 숫자들 중 최댓값과 최솟값 return 
# 숫자는 0~9까지 

def check(a,b,op):
    if op == '<':
        if a>b:
            return False
    if op == '>':
        if a<b:
            return False
    return True

def dfs(cnt,num):
    if cnt == k+1:
        answer.append(num)
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or check(num[cnt-1],str(i),arr[cnt-1]):
                visited[i] = 1
                dfs(cnt+1,num+str(i))
                visited[i] = 0

k = int(input())
arr = input().split()
visited = [0] * 10
answer = []
dfs(0,'')

answer.sort()
print(max(answer))
print(min(answer))
