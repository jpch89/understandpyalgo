"""
原列表：1 2 3 5 6 7
新列表：1 2 3 6 7
"""

# 建立双链表
list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]

pre = 5

# 值 6 的指向改成 3
list_left[list_right[list_right[pre]]] = pre
# 值 3 的指向改成 6
list_right[pre] = list_right[list_right[pre]]

# 正序输出
n = 0
while n != -1:
    print(list_value[n], end=' ')
    n = list_right[n]
print()

# 逆序输出
n = 4
while n != -1:
    print(list_value[n], end=' ')
    n = list_left[n]

"""
1 2 3 6 7 
7 6 3 2 1 
"""
