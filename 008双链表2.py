right = 1
left = 2
value = 0

linked_list = [[1, 3, -1], [5, 2, 5], [6, 4, 1],
               [2, 5, 0], [7, -1, 2], [3, 1, 3]]

n = 0
while n != -1:
    print(linked_list[n][value])
    n = linked_list[n][right]
