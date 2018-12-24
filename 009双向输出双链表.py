list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]

# 正向输出
n = list_left.index(-1)
while n != -1:
    print(list_value[n])
    n = list_right[n]

# 反向输出
n = list_right.index(-1)
while n != -1:
    print(list_value[n])
    n = list_left[n]

# 注意 left 和 right 互换
# 是双链表对称特性的体现
