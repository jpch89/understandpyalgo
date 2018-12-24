list_value = [1, 5, 6, 2, 7, 3]
list_pointer = [3, 2, 4, 5, -1, 1]

# 要删除元素 5
# 遍历寻找 5 前面元素的下标


def find_element(element, list_value, list_pointer):
    n = 0
    pre = None
    while n != -1:
        if list_value[n] == element:
            return pre
        pre = n
        n = list_pointer[n]


pre = find_element(5, list_value, list_pointer)

# 删除元素 5
list_pointer[pre] = list_pointer[list_pointer[pre]]


def output(list_value, list_pointer):
    n = 0
    while n != -1:
        print(list_value[n], end=' ')
        n = list_pointer[n]
    print()


output(list_value, list_pointer)
"""
1 2 3 6 7 
"""
