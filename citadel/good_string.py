class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        dp = [0 for _ in range(maxLength+1)]
        dp[zeroGroup] += 1
        dp[oneGroup] += 1
        for i in range(maxLength+1):
            # k = 1
            if i - oneGroup > 0:
                dp[i] += dp[i - oneGroup]
                dp[i] %= (10 ** 9 + 7)
                # k += 1

            # k = 1
            if i - zeroGroup > 0:
                dp[i] += dp[i - zeroGroup]
                dp[i] %= (10 ** 9 + 7)
                # k += 1
        # print(dp)
        res = 0
        for i in range(minLength, maxLength+1):
            res += dp[i]
            res %= (10 ** 9 + 7)
        return res