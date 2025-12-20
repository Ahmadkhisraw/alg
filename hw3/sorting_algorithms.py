from __future__ import annotations

import argparse
import random
import time
import unittest
from typing import Callable, List

IntList = List[int]


def insertion_sort(arr: IntList) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def shell_sort(arr: IntList) -> None:
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def _partition(arr: IntList, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_impl(arr: IntList, low: int, high: int) -> None:
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_impl(arr, low, pi - 1)
        _quick_sort_impl(arr, pi + 1, high)


def quick_sort(arr: IntList) -> None:
    if arr:
        _quick_sort_impl(arr, 0, len(arr) - 1)


def generate_random_array(n: int, seed: int = 0) -> IntList:
    rng = random.Random(seed)
    return [rng.randint(0, 1_000_000) for _ in range(n)]


def measure_time(sort_fn: Callable[[IntList], None], original: IntList) -> float:
    data = original.copy()
    start = time.perf_counter()
    sort_fn(data)
    return time.perf_counter() - start


class SortingTest(unittest.TestCase):
    def test_insertion_sort(self) -> None:
        arr = [5, 2, 9, 1, 5, 6]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 5, 5, 6, 9])

    def test_shell_sort(self) -> None:
        arr = [3, 0, 2, 5, -1, 4, 1]
        shell_sort(arr)
        self.assertEqual(arr, [-1, 0, 1, 2, 3, 4, 5])

    def test_quick_sort(self) -> None:
        arr = [10, 7, 8, 9, 1, 5]
        quick_sort(arr)
        self.assertEqual(arr, [1, 5, 7, 8, 9, 10])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run insertion, shell, and quick sort benchmarks."
    )
    parser.add_argument(
        "--sizes",
        type=int,
        nargs="+",
        default=[1000, 5000, 10000, 20000],
        help="Input sizes to benchmark.",
    )
    parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducible arrays."
    )
    return parser.parse_args()


def format_row(
    n: int, insertion: float, shell: float, quick: float, precision: int = 6
) -> str:
    return (
        f"{n}\t"
        f"{insertion:.{precision}f}\t\t"
        f"{shell:.{precision}f}\t\t"
        f"{quick:.{precision}f}"
    )


def main() -> None:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SortingTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)

    args = parse_args()
    print("\nN\tInsertion\tShell\t\tQuick")
    print("------------------------------------------------")
    for n in args.sizes:
        data = generate_random_array(n, args.seed)
        times = [
            measure_time(insertion_sort, data),
            measure_time(shell_sort, data),
            measure_time(quick_sort, data),
        ]
        print(format_row(n, *times))


if __name__ == "__main__":
    main()
