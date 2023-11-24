n = int(input())
for _ in range(n):
    a,b = input().split()
    val = 0

    a_int = int(a,2)
    b_int = int(b,2)
    val = a_int+b_int
    
    print(bin(val)[2:])