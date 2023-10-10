def group_options(people: int, groups: int):
    def allocate(g, p, dp):
        if g > p:
            return 0
        elif dp[g][p] is not None:
            return dp[g][p]
        else:
            dp[g][p] = allocate(g-1, p-1, dp) + allocate(g, p-g, dp)
            return dp[g][p]


    dp = [[None for _ in range(people+1)] for _ in range(groups+1)]
    for i in range(len(dp[0])):
        dp[0][i] = 0 if i != 0 else 1
    # dp[0][0] = 1
    # print(dp)
    return allocate(groups, people, dp)



if __name__ == '__main__':
    print(group_options(8, 4))
    print(group_options(24, 5))

