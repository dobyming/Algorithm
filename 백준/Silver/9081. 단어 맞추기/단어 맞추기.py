import sys
input = sys.stdin.readline
# 주어진 단어 다음 단어를 출력하시오

# 순서대로 perm 출력할 수 있도록 
def next_permutation(arr):
    k = -1

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            k = i
    if k == -1:
        return False
    
    for i in range(len(arr)-1,-1,-1):
        if arr[k] < arr[i]:
            m = i
            break
    
    arr[k],arr[m] = arr[m],arr[k]
    new_arr = arr[:k+1]
    new_arr.extend(list(reversed(arr[k+1:])))

    return new_arr

T = int(input().rstrip())
for _ in range(T):
    word = input().rstrip()
    answer = next_permutation(list(word))

    if answer:
        print(''.join(answer))
    else:
        print(word)