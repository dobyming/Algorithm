s = input()
t = input()

len_s ,len_t= len(s),len(t)

if s*len_t == t*len_s:
    print(1)
else:
    print(0)