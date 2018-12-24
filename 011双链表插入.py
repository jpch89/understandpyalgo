"""
原列表：1 2 3 5 6 7
新列表：1 2 3 4 5 6 7
"""


def output(list_value, list_right, head):
    n = head
    while n != -1:
        print(list_value[n], end=' ')
        n = list_right[n]
    print()


list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]
head = 0
prepos = 5

# 添加值
list_value.append(4)
# 添加新元素的双向链接
list_right.append(list_right[prepos])
list_left.append(prepos)
# 改变原列表指向
list_left[list_right[prepos]] = len(list_value) - 1
list_right[prepos] = len(list_value) - 1

# 正序遍历
output(list_value, list_right, 0)
# 逆序遍历
output(list_value, list_left, 4)

"""
1 2 3 4 5 6 7 
7 6 5 4 3 2 1 
"""
