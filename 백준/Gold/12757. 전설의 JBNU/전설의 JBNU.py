import sys,bisect
input = sys.stdin.readline

# 초기 데이터 개수, 명령횟수, 근접한 key값 제한: k
n,m,k = map(int,input().split())
JBNU = {}
# 이진탐색 된 key값들의 모임
keys = []

# key 삽입 시, 이진탐색으로 삽입
def putKey(key):
    bisect.insort(keys,key)
    return

# 근접한 key 찾기
def findKey(key):
    # key가 jbnu에 있으면 val이 -1가 나올수 없음
    val = JBNU.get(key,-1)
    if val != -1:
        return key
    else:
        # 없으면 이진탐색 시작
        idx = bisect.bisect(keys,key)
        # 맨 앞에 위치할 수 있을때
        if idx == 0:
            if abs(keys[0]-key) <= k:
                return keys[0]
        # 맨 뒤에 위치할 수 있을때
        elif idx == len(keys):
            if abs(keys[idx-1]-key) <= k:
                return keys[idx-1]
        else:
            # ?
            if keys[idx] - key == key - keys[idx-1]:
                return -2
            # 왼쪽이 더 작을때
            if key - keys[idx-1] < keys[idx] - key:
                if key - keys[idx-1] <= k:
                    return keys[idx-1]
            # 오른쪽이 더 작을때
            if keys[idx] - key < key - keys[idx-1]:
                if keys[idx] - key <= k:
                    return keys[idx]
    
    return -1  

for _ in range(n):
    key,value = map(int,input().split())
    JBNU[key] = value
    putKey(key)

for _ in range(m):
    order = list(map(int,input().split()))
    if order[0] == 1:
        JBNU[order[1]] = order[2]
        # 새로운 key값이 들어오기 때문에 정렬하여 갱신 필요
        putKey(order[1])
    elif order[0] == 2:
        # new_key: 존재하는 key중 근접한 값 또는 자기자신 
        new_key = findKey(order[1])
        if new_key == -1 or new_key == -2:
            continue
        else:
            JBNU[new_key] = order[2]
    elif order[0] == 3:
        new_key = findKey(order[1])
        if new_key == -1:
            print(-1)
        elif new_key == -2:
            print('?')
        else:
            print(JBNU[new_key])