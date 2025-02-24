arr = [3, -7, 5, -1, 4, -3, 2, 8]

largest = arr[0]
second_largest = arr[0]

for i in arr:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest and i!=largest:
        second_largest = i



print(second_largest)