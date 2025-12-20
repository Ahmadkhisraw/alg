from __future__ import annotations

from typing import List


def knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


def main() -> None:
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print(f"Max value: {knapsack(capacity, weights, values)}")


if __name__ == "__main__":
    main()
