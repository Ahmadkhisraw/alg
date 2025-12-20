from __future__ import annotations

import argparse
import random
import threading
import time
from typing import Callable, List

IntList = List[int]


def partition(arr: IntList, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_seq(arr: IntList, low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_seq(arr, low, pi - 1)
        quick_sort_seq(arr, pi + 1, high)


def quick_sort_seq_wrapper(arr: IntList) -> None:
    if arr:
        quick_sort_seq(arr, 0, len(arr) - 1)


def quick_sort_parallel(arr: IntList, low: int, high: int, depth: int) -> None:
    if low >= high:
        return
    if depth <= 0:
        quick_sort_seq(arr, low, high)
        return
    pi = partition(arr, low, high)
    left_thread = threading.Thread(
        target=quick_sort_parallel, args=(arr, low, pi - 1, depth - 1)
    )
    left_thread.start()
    quick_sort_parallel(arr, pi + 1, high, depth - 1)
    left_thread.join()


def quick_sort_parallel_wrapper(arr: IntList, num_threads: int) -> None:
    if not arr:
        return
    depth = 0
    t = max(1, num_threads)
    while t > 1:
        depth += 1
        t //= 2
    quick_sort_parallel(arr, 0, len(arr) - 1, depth)


def generate_array(n: int, seed: int = 0) -> IntList:
    rng = random.Random(seed)
    return [rng.randint(0, 1_000_000) for _ in range(n)]


def measure_time(fn: Callable[[IntList], None], data: IntList) -> float:
    arr = data.copy()
    start = time.perf_counter()
    fn(arr)
    return time.perf_counter() - start


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Benchmark sequential and threaded quick sort implementations."
    )
    parser.add_argument(
        "--sizes",
        type=int,
        nargs="+",
        default=[10000, 20000, 30000, 40000, 50000],
        help="Input sizes to measure.",
    )
    parser.add_argument(
        "--threads",
        type=int,
        nargs="+",
        default=[1, 2, 4, 8],
        help="Thread counts to compare.",
    )
    parser.add_argument(
        "--seed", type=int, default=42, help="Seed for deterministic data generation."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    threads = sorted(set(t for t in args.threads if t >= 1))

    print("N", end="")
    for t in threads:
        label = "QuickSort" if t == 1 else f"P-{t}T"
        print(f"\t\t{label}", end="")
    print("\n------------------------------------------------------------")

    for n in args.sizes:
        data = generate_array(n, args.seed)
        print(n, end="")
        for t in threads:
            if t == 1:
                duration = measure_time(quick_sort_seq_wrapper, data)
            else:
                duration = measure_time(
                    lambda v, workers=t: quick_sort_parallel_wrapper(v, workers), data
                )
            print(f"\t\t{duration:.6f}", end="")
        print()


if __name__ == "__main__":
    main()
