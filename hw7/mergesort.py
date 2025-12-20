from __future__ import annotations

from typing import List


def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    left_part = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def max_sub_array(arr: List[int]) -> int:
    max_so_far = max_ending = arr[0]
    for value in arr[1:]:
        max_ending = max(value, max_ending + value)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


def main() -> None:
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max Subarray Sum: {max_sub_array(arr)}")
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", " ".join(str(x) for x in arr))


if __name__ == "__main__":
    main()
