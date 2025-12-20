from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

Grid = List[List[str]]
Point = Tuple[int, int]


@dataclass(order=True)
class Node:
    f: int
    x: int = field(compare=False)
    y: int = field(compare=False)
    g: int = field(compare=False)
    h: int = field(compare=False)
    parent: Optional["Node"] = field(compare=False, default=None)


def heuristic(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def valid(x: int, y: int, grid: Grid) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "#"


def reconstruct(goal: Node) -> List[Point]:
    path: List[Point] = []
    cur: Optional[Node] = goal
    while cur:
        path.append((cur.x, cur.y))
        cur = cur.parent
    path.reverse()
    return path


def a_star(grid: Grid, start: Point, goal: Point) -> List[Point]:
    sx, sy = start
    gx, gy = goal

    open_heap: List[Node] = []
    g_score = [[float("inf")] * len(grid[0]) for _ in grid]
    start_node = Node(
        f=heuristic(sx, sy, gx, gy),
        x=sx,
        y=sy,
        g=0,
        h=heuristic(sx, sy, gx, gy),
        parent=None,
    )
    heapq.heappush(open_heap, start_node)
    g_score[sx][sy] = 0

    closed = [[False] * len(grid[0]) for _ in grid]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_heap:
        current = heapq.heappop(open_heap)
        if closed[current.x][current.y]:
            continue
        closed[current.x][current.y] = True

        if (current.x, current.y) == goal:
            return reconstruct(current)

        for dx, dy in directions:
            nx, ny = current.x + dx, current.y + dy
            if not valid(nx, ny, grid) or closed[nx][ny]:
                continue

            tentative_g = current.g + 1
            if tentative_g < g_score[nx][ny]:
                g_score[nx][ny] = tentative_g
                h = heuristic(nx, ny, gx, gy)
                heapq.heappush(
                    open_heap,
                    Node(
                        f=tentative_g + h,
                        x=nx,
                        y=ny,
                        g=tentative_g,
                        h=h,
                        parent=current,
                    ),
                )
    return []


def main() -> None:
    grid_rows = [
        "..........",
        ".####.....",
        ".#..#.....",
        ".#..#.....",
        ".#........",
        "....######",
        "..........",
    ]
    grid: Grid = [list(row) for row in grid_rows]

    start: Point = (0, 0)
    goal: Point = (6, 9)

    path = a_star(grid, start, goal)
    if not path:
        print("Путь не найден")
        return

    for x, y in path:
        if (x, y) != start and (x, y) != goal:
            grid[x][y] = "*"

    print("Путь найден:")
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()
