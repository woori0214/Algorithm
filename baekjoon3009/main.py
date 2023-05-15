
dictX = {}
dictY = {}
answer = []
for i in range(3):
    x,y = map(int,input().split())
    if x not in dictX:
        dictX[x] = 1
    else:
        dictX[x] += 1
    if y not in dictY:
        dictY[y] = 1
    else:
        dictY[y] += 1
# print(dictX)
for key,value in dictX.items():
    if value != 2:
        answer.append(key)

for key,value in dictY.items():
    if value != 2:
        answer.append(key)

for a in answer:
    print(a, end= " ")