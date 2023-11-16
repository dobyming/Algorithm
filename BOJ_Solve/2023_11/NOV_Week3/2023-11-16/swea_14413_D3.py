T = int(input())
for idx in range(1,T+1):
    n,m = map(int,input().split())
    board = [list(input()) for _ in range(n)]

    # '#' 일때와 '.'일때 구분해서 ..
    # '?'는 상관 없으니 pass

    for i in range(n):
        for j in range(m):
            if board[i][j] == '#':
                # 짝수 턴에 나오면 다음 짝수턴에도 #이 나와야한다.(홀수 자리엔 .이): 즉 번갈아가는 아이디어로 풀이
                if (i+j) % 2 == 0:
                    even,odd = '#','.'
                else:
                    even,odd = '.','#'
                break
            elif board[i][j] == '.':
                if (i+j) % 2 == 0:
                    even,odd = '.','#'
                else:
                    even,odd = '#','.'
                break

    answer = ''
    # 번갈아 가면서 나온다.
    for k in range(n):
        for l in range(m):
            # 짝수일때
            if (k+l) % 2 == 0 and board[k][l] == odd:
                answer = 'impossible'
                break
            # 홀수일때
            if (k+l) % 2 != 0 and board[k][l] == even:
                answer = 'impossible'
                break

    if len(answer) == 0:
        answer = 'possible'

    print(f'#{idx} {answer}')