def getmaxsubarraylen(team_a,team_b):
    n =len(team_a)
    ans = 0
    i = 0
    while i < n:
        j = i
        # Ensure the chosen team's skill levels are non-decreasing
        while j < n - 1 and max(team_a[j], team_b[j]) <= min(team_a[j + 1], team_b[j + 1]):
            j += 1

        # Move j as far right as possible while maintaining the condition that team_a[i] ≤ team_b[j]
        while j < n and team_a[i] <= team_b[j]:
            ans = max(ans, j - i + 1)  # Update the answer with the maximum possible length
            j += 1

        i += 1  # Move to the next position and repeat the process

    return ans

# team_a = [5,2,4,1]
# team_b = [3,6,2,2]

team_a = [2,7,3]
team_b = [4,2,6]

print(getmaxsubarraylen(team_a,team_b))
