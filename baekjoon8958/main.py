# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX

N = int(input())

for i in range(N):
    s = input()
    answer = 0
    cnt = 0

    for j in s:
        cnt+=1
        if j == "O":
            answer += cnt
        else:
            cnt = 0
    print(answer)