
# ** Case 1
# * Input: 1000 70 170
# * Output: 11

# ** Case 2
# * Input: 3 2 1
# * Output: -1

# ** Case 3
# * Input: 2100000000 9 10
# * Output: 2100000001

A, B, C = map(int,input().split())
if B >= C:
    print('-1')

else:
    print(A//(C-B)+1)