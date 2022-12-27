
# ** Case 1
# * Input: nums = 10
# * Output: 3

# ** Case 2
# * Input: nums = 12
# * Output: 11

def solution(n):
    cnt = 1

    while (cnt <= 1000000):
        if n % cnt == 1:
            result = cnt
            return result
        cnt += 1