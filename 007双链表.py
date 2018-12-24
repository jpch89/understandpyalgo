list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]

# 通过找到指针为空的找到第一个元素
head = list_left.index(-1)
print(list_value[head])
n = list_right[head]

while n != -1:
    print(list_value[n])
    n = list_right[n]
