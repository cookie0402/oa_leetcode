import unittest

from collections import defaultdict
def best_sum(parents, values):
    children = defaultdict(lambda: [])
    for i in range(len(parents)):
        if parents[i] >= 0:
            children[parents[i]].append(i)
    print(children)
    max_sum = -float('inf')

    def gain(idx, children, values):
        nonlocal max_sum
        if not children[idx]:
            max_sum = max(values[idx], max_sum)
            return max(values[idx], 0)
        else:
            gains = [0, 0]
            for c in children[idx]:
                gains.append(max(gain(c, children, values), 0))
            gains.sort(reverse=True)
            max_sum = max(max_sum, values[idx]+sum(gains[:2]))
            return max(values[idx]+gains[0], 0)

    gain(0, children, values)
    return max_sum



class best_sum_test(unittest.TestCase):
    def testcase1(self):
        p = [-1, 0, 1, 2, 0]
        v = [-2, 10, 10, -3, 10]
        res = best_sum(p, v)
        self.assertEquals(res, 28)

    def testcase2(self):
        p = [-1, 0, 1, 2, 0]
        v = [5, 7, -10, 4, 15]
        res = best_sum(p, v)
        self.assertEquals(res, 27)

    def testcase3(self):    
        p = []
# if __name__ == '__main__':
#     p = [-1, 0, 1, 2, 0]
#     v = [-2, 10, 10, -3, 10]
#     res = best_sum(p, v)
#     print(res)
#
#     p = [-1, 0, 1, 2, 0]
#     v = [5, 7, -10, 4, 15]
#     res = best_sum(p, v)
    # print(res)