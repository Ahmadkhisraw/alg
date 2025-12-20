from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def insert(root: Optional[Node], key: int) -> Node:
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def search(root: Optional[Node], key: int) -> bool:
    if root is None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


def inorder(root: Optional[Node]) -> None:
    if root is None:
        return
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


def main() -> None:
    root: Optional[Node] = None
    for key in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, key)

    print("Inorder traversal:", end=" ")
    inorder(root)
    print()
    result = "Found" if search(root, 40) else "Not found"
    print(f"Search 40: {result}")


if __name__ == "__main__":
    main()
