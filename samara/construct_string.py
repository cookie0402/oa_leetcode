a = ["cat","dog","ferret","scorption"]
res = []

if not a:
    print([])
for i in range(1,len(a)):

    cur = a[i-1][0]+a[i][len(a[i])-1]
    res.append(cur)
    if i ==len(a)-1:
        cur = a[i][0] +a[0][len(a[0])-1]
        res.append(cur)
print(res)



