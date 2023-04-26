# N = int(input()) # 달팽이 관 범위
# lastNumber = int(input()) # 구할 값
# box = [[0 for i in range(N)]for i in range(N)] # 달팽이 관
#
# r = N//2 # 처음 x값
# c = N//2 # 처음 y값
#
# # 좌표 이동 리스트
# # 상 우 하 좌
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]
#
# dir = 0 # dr,dc를 돌릴 방향
# moveCnt = 1 # 이동 횟수
# maxMoveCnt = 1
#
# data = 1 # 달팽이 관을 돌리면서 넣을 값
# dirCnt = 0
#
# answer = []
#
# while True:
#
#     box[r][c] += data
#
#     if data == lastNumber:
#         answer.append(r+1)
#         answer.append(c+1)
#
#     data += 1
#
#     r += dr[dir]
#     c += dc[dir]
#
#     moveCnt -= 1
#
#     if moveCnt == 0:
#         dirCnt += 1 # 방향 리스트를 돌리기 위해 count
#
#         if dirCnt == 2:
#             maxMoveCnt += 1
#             dirCnt = 0
#
#         moveCnt = maxMoveCnt
#         dir += 1
#
#         if dir == 4:
#             dir = 0
#
#     if r == 0 and c == 0:
#         box[r][c] += data
#         if data == lastNumber:
#             answer.append(r + 1)
#             answer.append(c + 1)
#
#         for x in box:
#             for y in x:
#                 print(y,end=" ")
#             print()
#         for rc in answer:
#             print(rc,end=" ")
#         break

############# 역순 풀이
# [0,0]부터 좌표를 돌림
N = int(input())
selectedNumber = int(input())

box = [[0 for i in range(N)]for i in range(N)]

r,c = 0,0

dr = [1,0,-1,0]
dc = [0,1,0,-1]

dir = 0
data = N*N

while True:

    box[r][c] = data

    if data == selectedNumber:
        answer = [r+1,c+1]

    r += dr[dir]
    c += dc[dir]

    # 다음 좌표 확인
    nextR = r+dr[dir]
    nextC = c+dc[dir]

    if nextR >= N or nextC >=N or nextR < 0 or nextC <0 or box[nextR][nextC] != 0:
        dir += 1
        dir %= 4

    data -= 1

    if data == 0:
        break

for x in box:
    for rc in x:
        print(rc, end = " ")
    print()
print(*answer)

