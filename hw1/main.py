from __future__ import annotations

import argparse
import time

def measure_insert_time(n: int) -> float:
    """Insert n sequential keys into a dict and return elapsed seconds."""
    payload = {}
    start = time.perf_counter()
    for i in range(n):
        payload[i] = i * 2 + 1
    return time.perf_counter() - start


def run_unit_test() -> None:
    probe = {}
    probe[42] = 100
    assert len(probe) == 1 and probe[42] == 100, "Dict insert regressed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Measure how long it takes to insert N keys in a Python dict. "
            "Pass custom sizes to control the workload."
        )
    )
    parser.add_argument(
        "sizes",
        metavar="N",
        type=int,
        nargs="*",
        default=[10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],
        help="Sequence sizes to benchmark.",
    )
    return parser.parse_args()


def main() -> None:
    run_unit_test()
    args = parse_args()
    print("N,Time_sec")
    for n in args.sizes:
        duration = measure_insert_time(n)
        print(f"{n},{duration}")


if __name__ == "__main__":
    main()
