# 트리(Tree)
# 가계도와 같은 계층적인 구조를 표현할 때 사용가능한 자료구조
# 기본적으로 트리의 크기가 N일 떄 간선의 개수 N-1

# 이진 탐색 트리(Binary Search Tree)
# 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조
# 왼쪽자식노드 < 부모노드 < 오른쪽 자식노드

# 트리 순회(Tree Traversal)
# 트리 자료구조의 포함된 노드를 특정한 방법으로 한번씩 방문하는 방법
# 트리의 정보를 시각적으로 확인 가능
# 대표적 트리 순회 방법
# 1)전위순회(pre-order traverse) : 루트 먼저
# 2)중위순회(in-order traverse) : 왼쪽 자식 - 루트
# 3)후위순회(post-order traverse) : 왼쪽자식 - 오른쪽자식 - 루트


# 트리의 순회 구현 예시
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input()) # 노드의 개수
tree = {}

# 입력 예시
# 7
# A B C 
# B D E 
# C F G 
# D None None
# E None None
# F None None
# G None None

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
