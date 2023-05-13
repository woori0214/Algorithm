# N = int(input())
# board = [[0 for i in range(N)]for j in range(N)]
#
# res = []
# num = int(input())
# cnt1 = 0
# cnt2 = 0
# cnt3 = 0
# cnt4 = 0
# answerCnt = []
#
# for i in range(num):
#     x, y = map(int, input().split())
#     res.append([x,y])
#     board[x][y] = "*"
#
# answer = res[:]
# while True:
#     for star in answer:
#         if star[0] != 0 and star[1] != 0:
#             break
#     else:
#         answerCnt.append(cnt1)
#         break
#
#     # 위로 이동
#     for star in answer:
#         if star[0] == 0:
#             continue
#         star[0] -= 1
#         cnt1 += 1
#
#     # 좌로 이동
#     for star in answer:
#         if star[1] == 0:
#             continue
#         star[1] -= 1
#         cnt1 += 1
#
# answer = res[:]
#
# while True:
#     for star in answer:
#         if star[0] != 0 and star[1] != N-1:
#             break
#     else:
#         answerCnt.append(cnt2)
#         break
#
#     # 위로 이동
#     for star in answer:
#         if star[0] == 0:
#             continue
#         star[0] -= 1
#         cnt2 += 1
#
#     # 우로 이동
#     for star in answer:
#         if star[1] == N-1:
#             continue
#         star[1] += 1
#         cnt2 += 1
#
#
# answer = res[:]
#
# while True:
#     for star in answer:
#         if star[0] != N-1 and star[1] != 0:
#             break
#     else:
#         answerCnt.append(cnt3)
#         break
#
#     # 아래로 이동
#     for star in answer:
#         if star[0] == N-1:
#             continue
#         star[0] += 1
#         cnt3 += 1
#
#     # 좌로 이동
#     for star in answer:
#         if star[1] == 0:
#             continue
#         star[1] -= 1
#         cnt3 += 1
#
# answer = res[:]
#
# while True:
#     for star in answer:
#         if star[0] != N-1 and star[1] != N-1:
#             break
#     else:
#         answerCnt.append(cnt4)
#         break
#
#     # 아래로 이동
#     for star in answer:
#         if star[0] == N-1:
#             continue
#         star[0] += 1
#         cnt4 += 1
#
#     # 우로 이동
#     for star in answer:
#         if star[1] == N-1:
#             continue
#         star[1] -= 1
#         cnt4 += 1
#
# print(answerCnt)


N = int(input())
num = int(input())

res = []

for i in range(num):
    x, y = map(int, input().split())
    res.append([x, y])

# [0,0] , [N,0] , [0,N] , [N,N]

# leftUp
answer1 = [0, 0]
answerCnt = []
result1 = []

for star in res:
    row = abs(star[0] - answer1[0])
    col = abs(star[1] - answer1[1])
    result1.append(row + col)
answerCnt.append(max(result1))

# leftDown
answer2 = [N - 1, 0]
result2 = []

for star in res:
    row = abs(star[0] - answer2[0])
    col = abs(star[1] - answer2[1])
    result2.append(row + col)
answerCnt.append(max(result2))

# rightUp
answer3 = [0, N - 1]
result3 = []

for star in res:
    row = abs(star[0] - answer3[0])
    col = abs(star[1] - answer3[1])
    result3.append(row + col)
answerCnt.append(max(result3))

# rightDown
answer4 = [N - 1, N - 1]
result4 = []

for star in res:
    row = abs(star[0] - answer4[0])
    col = abs(star[1] - answer4[1])
    result4.append(row + col)
answerCnt.append(max(result4))

print(min(answerCnt)+1)