# 使用嵌套数组模拟单链表
linked_list = [[1, 3], [5, 2], [6, -1], [2, 5], [4, 1], [3, 4]]

# 好方法！
value = 0
pointer = 1
n = 0

while n != -1:
    print(linked_list[n][value])
    n = linked_list[n][pointer]
