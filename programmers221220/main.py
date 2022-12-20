# ** Case 1
# * Input: n = 1
# * Output: 1

# ** Case 2
# * Input: n = 7
# * Output: 1

# ** Case 3
# * Input: n = 15
# * Output: 3


def solution(n):
    cnt = 1
    pizza = 7
    while (True):
        if pizza >= n:
            answer = cnt
            break
        cnt += 1
        pizza += 7

    return answer