N, M = map(int, input().split())

x, y, direction = map(int, input().split())
# d = 0 북 / d = 1 동 / d = 2 남 / d = 3 서
robot = []

for i in range(N):
    number = list(map(int, input().split()))
    robot.append(number)

dr = [[-1, 0], [0, -1], [1, 0], [0, 1]]
cnt = 0
answer = 0
flag = False

while True:

    if flag == True:
        break

    # 1. 현재 칸 청소
    if robot[x][y] != 1:
        answer += 1
        robot[x][y] = 2

    cnt = 0
    print("현재위치",x,y)


    # 네방향 돌 for문
    for i in range(direction, direction +5):
        i = i%4

        nxtR = x + dr[i][0]
        nxtC = y + dr[i][1]
        # print(nxtR,nxtC)

        if cnt == 4:
            rearR = x + dr[(i + 2) % 4][0]
            rearC = y + dr[(i + 2) % 4][1]

            if robot[rearR][rearC] == 1:
                flag = True
                break
            else:
                x = rearR
                y = rearC
                break

        # 범위가 초과될 시
        if nxtR < 0 or nxtR >= N or nxtC < 0 or nxtC >= M:
            nxtR -= dr[i][0]
            nxtC -= dr[i][1]

        # 4방향 중 청소할 곳이 있을 때
        if robot[nxtR][nxtC] == 0:
            x = nxtR
            y = nxtC
            # 현위치 바뀌면서 for문 빠져나감
            # direction 바꿔줌
            direction = i
            break

        # 4방향 중 청소할 곳이 없을 때
        else:
            cnt += 1




    # cont = input()
    # if cont == 'n':
    #     continue
    # elif cont == 'q':
    #     break

    cnt+=1

print(answer)