from __future__ import annotations

import argparse
from typing import Callable


def integrand(x: float) -> float:
    return 8.0 - 2.0 * x * x


def simpson(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n, 2):
        total += 4.0 * f(a + i * h)
    for i in range(2, n, 2):
        total += 2.0 * f(a + i * h)
    return (h / 3.0) * total


def calculate_area(n: int) -> float:
    return simpson(integrand, -2.0, 2.0, n)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Approximate the area under 8 - 2x^2 using Simpson's rule."
    )
    parser.add_argument(
        "subdivisions",
        metavar="N",
        type=int,
        nargs="*",
        default=[2, 4, 10, 100, 1000],
        help="Number of subintervals to use (odd values are rounded up).",
    )
    return parser.parse_args()


def main() -> None:
    exact = 64.0 / 3.0
    args = parse_args()
    print("N\t\tApproximate Area\t\tError")
    print("----------------------------------------------------------")
    for n in args.subdivisions:
        approx = calculate_area(n)
        error = abs(approx - exact)
        print(f"{n}\t\t{approx:.12f}\t\t{error:.12f}")


if __name__ == "__main__":
    main()
