bids_size = 4
bids = [
    [1, 200000000, 5, 0], [2, 200000000, 4, 2], [3, 200000000, 4, 6], [4, 200000000, 3, 1]
]
print(bids)
shares = 400000000


# bids = sorted(bids,key=lambda x:( x[2],x[3]),reverse = True)
# print(bids)
# while shares>0:

def custom_sort_key(bid):
    return (-bid[2], bid[3])  # Use -bid[3] for descending order

# Sort the list using the custom key function
sorted_bids = sorted(bids, key=custom_sort_key)



# Print the sorted list
#
res = []
i = 1
prev_cost = bids[0][2]
size_group = {}
tmp_size = bids[0][1]




for i in range(len(bids)):
    cost = bids[i][2]
    wanted_share =  bids[i][1]

    if cost not in size_group:
        size_group[cost] = wanted_share
    else:
        size_group[cost]+=wanted_share
        #
print(size_group)

for i in range(1,len(bids)):
    prev_cost  = bids[i-1][2]
    cost = bids[i][2]


    if cost != prev_cost:
        shares -= size_group[prev_cost]

    else:
        shares-=1
        size_group[cost]-=1

    if shares <= 0:
        break

res = [b[0] for b in sorted_bids[i:]]
print(i)
print(sorted(res))