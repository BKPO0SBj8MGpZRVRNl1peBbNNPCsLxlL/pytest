def solve(y, coins, x):
    if x < 0 or y < 0:
        return 0

    if y == 0:  # Change for 0 is only empty one.
        return 1
    count = solve(y, coins, x - 1) + solve(y - coins[x], coins, x)

    return count


def count_change(money, coins):
    return solve(money, coins, len(coins) - 1)
