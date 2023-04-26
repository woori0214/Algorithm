N = int(input())

inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

node = [0] * inorder[-1]

for i in range(N):
    node[i] = i+1

def preorder(node):


