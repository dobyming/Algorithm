n = int(input())
s = format(n+1,'b')
# n번쨰 숫자는 n+1 순서를 이진화 한것에서 앞자리를 뺸것 
s = s[1:]
print(s.replace('0','4').replace('1','7'))