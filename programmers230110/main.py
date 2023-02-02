T = int(input())

for tc in range(1,T+1):
    N = int(input())
    sleep = [0]*10
    cnt = 1

    while 0 in sleep:
        num = str(N*cnt)
        for i in range(len(num)):
            sleep[int(num[i])]+=1
            print(num[i])
        cnt+=1
    print("#{} {}".format(tc,num))