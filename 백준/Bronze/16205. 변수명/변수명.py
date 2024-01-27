info = input().split(' ')
od = int(info[0])

camel = ''
snake = ''
pascal = ''

if od == 1:
    words = info[1]
    # camel
    camel = words
    # snake
    snake = words
    i = 0
    while True:
        if snake[i].isupper():
            snake = snake[:i] + ('_') + snake[i].lower() + snake[i+1:]
            i = i+2
        else:
            i = i+1
        if i >= len(snake):
            break
    # pascal
    pascal = words[0].upper()+words[1:]

    print(camel)
    print(snake)
    print(pascal)

elif od == 2:
    words = info[1].split('_')
    snake = info[1]
    # 첫글자는 무조건 소문자로 
    camel += words[0]
    for i in range(1,len(words)):
        camel += words[i].capitalize()
    # 모든 문자의 첫글자는 대문자
    for word in words:
        pascal += word.capitalize()
    
    # camel 출력
    print(camel)
    # snake 출력
    print(snake)
    # pascal 출력
    print(pascal)

elif od == 3:
    words = info[1]
    # camel
    camel = words[0].lower() + words[1:]
    # snake
    snake = words
    i = 0
    while True:
        if snake[i].isupper():
            snake = snake[:i] + '_' + snake[i].lower() + snake[i+1:]
            i = i+2
        else:
            i+=1
        if i >= len(snake):
            break
    
    print(camel)
    print(snake[1:])
    print(words)