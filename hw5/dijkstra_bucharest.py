from __future__ import annotations

import heapq
from typing import Dict, List, Tuple

Vertex = str
EdgeList = List[Tuple[Vertex, int]]
Graph = Dict[Vertex, EdgeList]


def dijkstra(graph: Graph, start: Vertex, end: Vertex) -> Tuple[List[Vertex], int]:
    pq: List[Tuple[int, Vertex]] = [(0, start)]
    dist: Dict[Vertex, int] = {node: float("inf") for node in graph}
    prev: Dict[Vertex, Vertex] = {}
    visited: set[Vertex] = set()

    dist[start] = 0
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            break

        for v, weight in graph.get(u, []):
            if v in visited:
                continue
            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    if dist[end] == float("inf"):
        return [], -1

    path = [end]
    cur = end
    while cur != start:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
    return path, int(dist[end])


def build_graph() -> Graph:
    graph: Graph = {}

    def add_edge(u: Vertex, v: Vertex, w: int) -> None:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))

    add_edge("A", "B", 2)
    add_edge("A", "C", 6)
    add_edge("A", "D", 4)
    add_edge("B", "C", 3)
    add_edge("B", "D", 5)
    add_edge("C", "D", 1)
    return graph


def main() -> None:
    graph = build_graph()
    path, distance = dijkstra(graph, "B", "D")

    print("Город: Бухарест, Румыния")
    print("Задача: найти кратчайший путь от B до D\n")

    if distance == -1:
        print("Путь не найден.")
        return

    arrow_path = " → ".join(path)
    print(f"Кратчайший путь: {arrow_path}")
    print(f"Длина пути: {distance} km")


if __name__ == "__main__":
    main()
