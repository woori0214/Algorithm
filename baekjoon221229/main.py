
# ** Case 1
# * Input: nums =
#0 32
#3 13
#28 25
#17 5
#21 20
#11 0
#12 12
#4 2
#0 8
#21 0
# * Output: 42

totalHuman = 0
maxHuman_list = []

for i in range(10):
    outHuman, inHuman = map(int,input().split())
    totalHuman-=outHuman
    totalHuman+=inHuman
    maxHuman_list.append(totalHuman)

print(max(maxHuman_list))