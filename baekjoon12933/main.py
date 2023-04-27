from collections import deque

duck = input()

visit = [False for i in range(len(duck))]
sound = ""
answer = 0
soundCount = 0
visitFlag = 0

while visitFlag < len(duck):
    prevVisitFlag = visitFlag

    for i in range(len(duck)):

        if duck[i] == 'q' and visit[i] == False:
            if sound == '':
                visitFlag += 1
                visit[i] = True
                sound+=duck[i]

        elif duck[i] == 'u' and visit[i] == False:
            if sound == 'q':
                visitFlag += 1
                visit[i] = True
                sound+=duck[i]

        elif duck[i] == 'a' and visit[i] == False:
            if sound == 'qu':
                visitFlag += 1
                visit[i] = True
                sound+=duck[i]

        elif duck[i] == 'c' and visit[i] == False:
            if sound == 'qua':
                visitFlag += 1
                visit[i] = True
                sound+=duck[i]

        elif duck[i] == 'k' and visit[i] == False:
            if sound == 'quac':
                visitFlag += 1
                visit[i] = True
                sound+=duck[i]

                # sound에 quack이 다 있다면
            if sound == "quack":
                soundCount += 1  # 한마리 오리인지 count
                sound = ""  # 초기화

    if sound != "" or visitFlag == prevVisitFlag:
        answer = -1
        break

    # for문 실행시 한마리 오리인거 확인하기 위해
    if soundCount >= 1:
        answer += 1
        soundCount = 0
print(answer)