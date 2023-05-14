R, S = map(int,input().split())

# X는 유성의 일부 / #는 땅의 일부 / .은 공기
# 상하좌우로 이동해서 다른 부분 유서엥 도달할 수 있다.
# 적어도 1줄 이상의 공기는 존재 / 유성은 공기보다 위에 / 땅은 공기보다 아래
# 유성은 수직낙하 / 유성은 원형 유지
star = []
for i in range(R):
    shining = list(map(str,input()))
    star.append(shining)
flag = False

while not flag:

    for i in range(R-1,-1,-1):
        if flag == True:
            break
        for j in range(S-1,-1,-1):
            if star[i][j] == "X":
                if star[i+1][j] == "#":
                    flag = True
                    break

                star[i+1][j] = "X"
                star[i][j] = "."

for x in star:
    for y in x:
        print(y, end="")
    print()