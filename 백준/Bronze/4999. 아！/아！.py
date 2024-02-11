import sys
input = sys.stdin.readline

jae = input().rstrip()
doctor = input().rstrip()

jae_len = len(jae[:-1])
doc_len = len(doctor[:-1])

if jae_len >= doc_len:
    print('go')
else:
    print('no')