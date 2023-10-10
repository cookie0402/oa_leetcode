from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dp = {}
        dp[0] = {}
        dp[1] = {}
        dp[2] = {}

        dp[0][0] = 0
        dp[0][1] = 3
        dp[1][0] = 3
        dp[0][2] = 2
        dp[1][1] = 2
        dp[2][0] = 2

        def dfs(x, y, dp):
            abs_x = abs(x)
            abs_y = abs(y)
            if abs(x) in dp.keys() and abs(y) in dp[abs(x)].keys():
                return dp[abs(x)][abs(y)]
            dist = min(dfs(abs_x - 2, abs_y - 1, dp), dfs(abs_x - 1, abs_y - 2, dp)) + 1
            if abs_x not in dp.keys():
                dp[abs_x] = {}
            dp[abs_x][abs_y] = dist
            return dist

        return dfs(x, y, dp)