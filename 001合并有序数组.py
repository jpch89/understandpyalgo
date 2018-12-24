arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]
ind = 0

for i in range(len(arr2)):
    for j in range(ind, len(arr1)):
        if arr2[i] < arr1[j]:
            arr1.insert(j, arr2[i])
            ind = j + 1
            break
    else:
        arr1.extend(arr2[i:])

print(arr1)
