list_value = [1, 5, 6, 2, 4, 3]
list_pointer = [3, 2, -1, 5, 1, 4]

# 输出链表
n = 0
while n != -1:
    print(list_value[n])
    n = list_pointer[n]
