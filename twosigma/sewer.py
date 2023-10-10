# parent = [-1,0,1,2]
# input = [1,4,3,4]

#
# parent = [-1,0,0,1,1,2]
# input =  [1,2,2,1,1,1]

parent = [-1,0,0,0]
input = [10,11,10,10]


for i in range(len(input)-1,0,-1):
    # print(i)
    # idx = parent[i]
    input[parent[i]]+=input[i]
res = float("inf")
print(input)
for i in range(1,len(input)):
    res = min(abs(input[0]-2*input[i]),res)
print(res)

print(input)


