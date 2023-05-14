# 0은 딸기우유만을 파는 가게,
# 1은 초코우유만을 파는 가게,
# 2는 바나나우유만을 파는 가게를 뜻하며,
# 0, 1, 2 외의 정수는 주어지지 않는다.

N = int(input())

milk = map(int,input().split())
flag = False
staw = 0

cnt = 0
for i in milk:
    print(i,"----")
    if i == 0 and staw != 1:
        flag = True
        staw = 1
        cnt += 1
        print("0",cnt)
    elif i == 1 and flag == True:
        flag = "banana"
        cnt += 1
        print("1",cnt)
    elif i == 2 and flag == "banana":
        flag = False
        cnt += 1
        staw = 0
        print("2",cnt)
print(cnt)