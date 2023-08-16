import sys
input = sys.stdin.readline

def check(arr,left,right):
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -=1
        else:
            return False
    return True

def isPalindrome(word,left,right):
    if word == word[::-1]:
        return 0
    else:
        while left<right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                left_check = check(word,left+1,right)
                right_check = check(word,left,right-1)
                
                if left_check or right_check:
                    return 1
                else:
                    return 2
    

t = int(input().rstrip())
for _ in range(t):
    word = input().rstrip()
    left,right = 0,len(word)-1
    print(isPalindrome(word,left,right))