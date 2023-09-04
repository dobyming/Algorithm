def dfs(x,arr):
    arr[x] = -2
    for i in range(len(arr)):
        # 자식 노드 중에서 x를 부모로 갖고 있는게 있다면 
        if x == arr[i]:
            dfs(i,arr)

n = int(input())
# 각 노드의 부모 노드가 주어진 배열 
arr = list(map(int,input().split()))
t = int(input())

cnt = 0
dfs(t,arr)
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1

print(cnt)