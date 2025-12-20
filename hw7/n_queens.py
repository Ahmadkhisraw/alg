from __future__ import annotations

from typing import List


def is_safe(board: List[int], row: int, col: int) -> bool:
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


def solve_n_queens(n: int, row: int, board: List[int]) -> None:
    if row == n:
        print(" ".join(str(c + 1) for c in board))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board)


def main() -> None:
    n = 4
    print(f"Solutions for {n}-Queens:")
    board = [-1] * n
    solve_n_queens(n, 0, board)


if __name__ == "__main__":
    main()
