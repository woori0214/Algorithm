N = 5
bingo = []
order = []

for i in range(10):
    if i > 4:
        order.extend(list(map(int, input().split())))
    else:
        bingo.append(list(map(int, input().split())))
print(order)

visit = [[False for i in range(N)] for j in range(N)]

answer = 0

def horizCheck(visit):
    count = 0
    answer = 0

    for x in range(N):
        count = 0
        for y in range(N):
            # 가로
            if visit[x][y]:
                count += 1

        if count == N:
            answer += 1

    return answer


def verticalCheck(visit):
    count = 0
    answer = 0

    for x in range(N):
        count = 0
        for y in range(N):
            if visit[y][x]:
                count += 1

        if count == N:
            answer += 1

    return answer


def diagonalLeftCheck(visit):
    count = 0
    for x in range(N):
        # 정방향대각선
        if visit[x][x]:
            count += 1

    if count == N:
        return 1
    else:
        return 0


def diagonalRightCheck(visit):
    count = 0
    for x in range(N):
        # 정방향대각선
        if visit[x][N - x - 1]:
            count += 1

    if count == N:
        return 1
    else:
        return 0


def check(bingo):
    # 명령문
    for i in range(N * N):
        orderNumber = order[i]

        # orderNumber가 bingo에 있는지 찾기
        for a in range(N):
            for b in range(N):
                if bingo[a][b] == orderNumber:  # 같은 숫자일 때
                    visit[a][b] = True

                answer = verticalCheck(visit) + horizCheck(visit) + diagonalLeftCheck(visit) + diagonalRightCheck(visit)

                if answer >= 3:
                    return i+1

print(check(bingo))
