
N = 4
square = []
box = [[0 for i in range(100)]for j in range(100)]
count = 0
answer1 = []
answer2 = []
for i in range(N):
    x1,x2,y1,y2 = map(int,input().split())

    for x in range(x2,y2):
        for y in range(x1,y1):
            box[x][y] += 1
    maxX = max(x1,x2)
    maxY = max(y1,y2)
    answer1.append(maxX)
    answer2.append(maxY)

maxAnswer1 = max(answer1)
maxAnswer2 = max(answer2)
for x in range(maxAnswer1):
    for y in range(100):
        if box[x][y] == 1:
            count += 1
print(count)
