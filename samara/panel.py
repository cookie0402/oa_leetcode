panel = "2311453915"
codes = ["0211","639"]

res = []
for c in codes:
    for i in range(1, len(c)):
        idx = int(c[:i])
        # print(idx)
        if idx > len(panel):
            res.append("not found")
            break
        pattern_len = len(c)-i
        # pattern = c[i:pattern_len]
        # if c[]
        if c[i:i+pattern_len] == panel[idx:idx+pattern_len]:
            res.append(c[i:i+pattern_len])
        else:
            res.append("not found")
    # idx  = [int(c[0:i+1]) for i in range(len(c)-1)]
    #
    # for
print(res)
    # print(idx)