target = input()
check = ['U','C','P','C']
flag = True

for c in check:
    if c in target:
        target = target[target.index(c)+1:]
    else:
        flag = False
        break

if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")