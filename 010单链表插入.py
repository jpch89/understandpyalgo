"""
原链表：1 2 3 5 6 7
新链表：1 2 3 4 5 6 7
"""


def output(list_value, list_pointer, start):
    """遍历输出链表"""
    n = start
    while n != -1:
        print(list_value[n])
        n = list_pointer[n]


list_value = [1, 5, 6, 2, 7, 3]
list_pointer = [3, 2, 4, 5, -1, 1]
# 要插入的元素 4 的上一个元素是 3
# 3 的位置是 5（其实就是说 3 的内存地址是 5）
prepos = 5

# 添加值 4
list_value.append(4)
# 值 4 的指针指向值 5
list_pointer.append(list_pointer[prepos])
# 值 3 的指针指向值 4
list_pointer[prepos] = len(list_value) - 1

# 遍历输出
output(list_value, list_pointer, 0)
