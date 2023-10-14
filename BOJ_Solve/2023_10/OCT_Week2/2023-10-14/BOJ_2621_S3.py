from collections import Counter

cards = [input().split() for _ in range(5)]
cards.sort(key=lambda x:(x[1]))
colors,nums = [],[]

for a,b in cards:
    colors.append(a)
    nums.append(int(b))

nums.sort()
color_dict = Counter(colors)
nums_dict = Counter(nums)

answer = []
if 5 in color_dict.values() and nums[0]+1==nums[1] and nums[1]+1==nums[2] and nums[2]+1==nums[3] and nums[3]+1==nums[4]:
    answer.append(max(nums) + 900)
elif 4 in nums_dict.values():
    tmp = 0
    for n in nums:
        if nums_dict[n] == 4:
            tmp = n
    answer.append(tmp+800)
elif 3 in nums_dict.values() and 2 in nums_dict.values():
    three,two = 0,0
    for n in nums:
        if nums_dict[n] == 3:
            three = n
        elif nums_dict[n] == 2:
            two = n
    answer.append(three*10+two+700)
elif 5 in color_dict.values():
    answer.append(max(nums)+600)
elif nums[0]+1==nums[1] and nums[1]+1==nums[2] and nums[2]+1==nums[3] and nums[3]+1==nums[4]:
    answer.append(max(nums)+500)
elif 3 in nums_dict.values():
    tmp = 0
    for n in nums:
        if nums_dict[n] == 3:
            tmp = n
    answer.append(tmp+400)
elif 2 in nums_dict.values():
    tmp = []
    max_two,min_two = 0,0
    for n in nums:
        if nums_dict[n] == 2:
            tmp.append(n)
    if len(tmp)>=4:
        max_two = max(tmp)
        min_two = min(tmp)
        answer.append(max_two*10+min_two+300)
    else:
        answer.append(tmp[-1]+200)
else:
    answer.append(max(nums)+100)

print(max(answer))