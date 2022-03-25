
from __future__ import annotations
from typing import Generic, List, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    '''Node Class'''

    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    @staticmethod
    def node_to_path(node: Node[T]) -> List[T]:
        path: List[T] = [node.state]
        while node.parent is not None:
            node = node.parent
            path.append(node.state)
        path.reverse()
        return path

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
