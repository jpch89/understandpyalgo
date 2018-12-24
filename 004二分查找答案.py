numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
head, tail = 0, len(numbers)
search = int(input('输入要搜索的数字：'))

while tail - head > 1:
    mid = (head + tail) // 2
    if search < numbers[mid]:
        tail = mid
    if search > numbers[mid]:
        head = mid + 1
    if search == numbers[mid]:
        ans = mid
        break
else:
    if search == numbers[head]:
        ans = head
    else:
        ans = -1

print(ans)
