

arr = [3, -2, 5, -1, 4, -3, 2, 1]

min = arr[0]

for i in arr:
    
    if abs(i)<abs(min):
        min = i

print(min)
