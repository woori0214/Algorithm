
N = int(input())
file = []

for i in range(N):
    x = input().split(".")
    file.append(x[1])

fileExtension = {}

for i in file:
    if i not in fileExtension:
        fileExtension[i] = 1
    else:
        fileExtension[i] += 1

newFileExtionsion = dict(sorted(fileExtension.items()))

for key, value in newFileExtionsion.items():
    print(key, value)

