import unittest


def lego_blocks(rowA: list, rowB: list):
    a_zeros = rowA.count(0)
    a_sum = sum(rowA)
    b_zeros = rowB.count(0)
    b_sum = sum(rowB)
    if (a_zeros == 0 and a_sum < b_sum+b_zeros)or (b_zeros == 0 and b_sum < a_sum+a_zeros):
        return -1
    return max(a_zeros+a_sum, b_zeros+b_sum)


a = [1, 0, 2]
b = [1, 3, 0, 0]
res = lego_blocks(a, b)
print(res)

a = [2, 5, 0, 1, 1]
b = [2, 1, 0, 0]
print(lego_blocks(a, b))

a = [0, 0, 0]
b = [1, 1]
print(lego_blocks(a, b))