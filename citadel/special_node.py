import unittest
from collections import defaultdict
def special_node(tree_nodes: int, tree_from: list, tree_to: list):
    def bfs(graph, start) -> dict:
        dist = {start: 0}
        fringe = [start]
        level = 0
        while fringe:
            for i in range(len(fringe)):
                curr = fringe.pop(0)
                dist[curr] = level
                for n in graph[curr]:
                    if n not in dist.keys():
                        fringe.append(n)
            level += 1
        return dist

    def bi_dfs(graph, start0, start1):
        q0 = [start0]
        q1 = [start1]
        dist0 = {start0: 0}
        dist1 = {start1: 1}
        level = 0
        while q0 or q1:
            for i in range(len(q0)):
                curr = q0.pop(0)
                dist0[curr] = level
                for n in graph[curr]:
                    if n not in dist0.keys() and n not in dist1.keys():
                        q0.append(n)
            for i in range(len(q1)):
                curr = q1.pop(0)
                dist1[curr] = level
                for n in graph[curr]:
                    if n not in dist0.keys() and n not in dist1.keys():
                        q1.append(n)
            level += 1
        return dist0, dist1

    graph = defaultdict(lambda : [])
    for i in range(tree_nodes-1):
        graph[tree_from[i]].append(tree_to[i])
        graph[tree_to[i]].append(tree_from[i])
    # print(graph)
    if not graph:
        return []
    start_id = tree_from[0]
    start_dist = bfs(graph, start_id)
    max_dist = 0
    end0 = None
    for k, v in start_dist.items():
        if v > max_dist:
            max_dist = v
            end0 = k
    dist0 = bfs(graph, end0)
    max_dist = 0
    end1 = None
    for k, v in dist0.items():
        if v > max_dist:
            max_dist = v
            end1 = k
    diameter_len = v

    dist0, dist1 = bi_dfs(graph, end0, end1)
    # print(dist0)
    # print(dist1)

    res = []
    if diameter_len % 2 == 0:
        center = None
        for id in dist0.keys():
            if id in dist1.keys():
                center = id
        center_dist = bfs(graph, center)
        for k, v in center_dist.items():
            if v == diameter_len // 2:
                res.append(k)
            return res
    else:
        center = []
        for id in dist0.keys():
            if id in dist1.keys():
                center.append(id)
        for neighbor in graph[center[0]]:
            if neighbor in dist0.keys():
                center.append(neighbor)

        center_dist0, center_dist1 = bi_dfs(graph, center[0], center[1])
        # print(center_dist0, center_dist1)
        for k, v in center_dist0.items():
            if v == (diameter_len-1) // 2:
                res.append(k)
        for k, v in center_dist1.items():
            if v == (diameter_len-1) // 2:
                res.append(k)
    # print(res)
    return res




# @unittest
class specialnode_test(unittest.TestCase):
    def testcase1(self):
        treenode = 8
        treefrom = [1, 2, 3, 3, 1, 1, 3]
        treeto = [2, 8, 4, 5, 6, 7, 8]
        res = special_node(treenode, treefrom, treeto)
        self.assertEqual(1 in res, False)
        self.assertEqual(2 in res, False)
        self.assertEqual(3 in res, False)
        self.assertEqual(4 in res, True)
        self.assertEqual(5 in res, True)
        self.assertEqual(6 in res, True)
        self.assertEqual(7 in res, True)
        self.assertEqual(8 in res, False)
        # assert(res[1], 0)
        # assert(res[2], 0)
        # assert(res[3], 0)
        # assert(res[4], 1)
        # assert(res[4], 1)
        # assert(res[5], 1)
        # assert(res[6], 1)
        # assert(res[7], 1)
        # assert(res[8], 0)
        # assert(5 in res, True)
        # assert(6 in res, True)
        # assert(7 in res, True)
    def testcase2(self):
        treefrom = [1 for x in range(1_00_000)]
        treeto = [x for x in range(1_00_000)]
        treenode = 1_00_001
        res = special_node(treenode, treefrom, treeto)
        assert(len(res), 1_000_000)