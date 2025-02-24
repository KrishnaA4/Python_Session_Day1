arr = [1,2,3,1,2,4,5,6,1,7,8]

mpp = {}

for i in arr:
    if i not in mpp:
        mpp[i] = 1
    else:
        mpp[i]+=1

ans = []

for i in mpp.keys():
    if mpp.get(i)==1:
        ans.append(i)

print(ans)
