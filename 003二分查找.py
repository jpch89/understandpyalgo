numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]

target = int(input('请输入要查找的数字：'))
head = 0
tail = len(numbers) - 1

while tail >= head:
    mid = (head + tail) // 2
    if numbers[mid] == target:
        print(mid)
        break
    elif numbers[mid] < target:
        head = mid + 1
    else:
        tail = mid - 1
