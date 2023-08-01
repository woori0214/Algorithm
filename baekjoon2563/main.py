def square(graph):
    global answer
    count = 0
    count2 = 0
    for k in graph:
        for x in range(k[0],k[0]+10):
            for y in range(k[1],k[1]+10):
                box[x][y] += 1

    for x in range(100):
        for y in range(100):
            if box[x][y] >= 1:
                count += 1
    answer = count

N = int(input())
graph = []

for i in range(N):
    x,y = map(int,input().split())
    graph.append([x,y])

box = [[0 for i in range(100)] for j in range(100)]
answer = 0
square(graph)
print(answer)
