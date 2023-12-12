# a,b를 통해 길이가 n인 새로운 배열 c를 만듬
import sys
input = sys.stdin.readline

def binary_search(target):
    s,e = 0,m-1
    while s<e:
        mid = (s+e) // 2
        if B[mid] == target:
            return mid
        elif B[mid] < target:
            s = mid + 1
        elif B[mid] > target:
            e = mid - 1
    return e

def find_c():
    cur = C[2]
    j = 2
    if C[1] <= cur:
        cur = C[1]
        j = 1
    if C[0] <= cur:
        j = 0
    return j 

T = int(input().rstrip())
for _ in range(T):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    B.sort()

    answer = 0
    for i in range(n):
        idx = binary_search(A[i])
        C = []
        # 왼쪽,현재,오른쪽 절댓값 차이를 모두 구함
        C.append(abs(B[idx-1] - A[i]))
        C.append(abs(B[idx] - A[i]))
        C.append(abs(B[(idx+1)%m] - A[i]))
        # 그 중 가장 작은 값에 해당하는 index를 return 
        answer += B[idx + find_c() - 1]
    
    print(answer)