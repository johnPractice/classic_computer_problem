from typing import Callable, List, Optional, Sequence, Set, TypeVar
from typing_extensions import Protocol
from node import Node
from stack import Stack
T = TypeVar('T')
C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


def dfs(initial_state: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial_state, None))
    # explored is where we've been
    explored: Set[T] = {initial_state}
    # keep moving to explore more
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()

        current_state: T = current_node.state
        # check goal state
        if goal_test(current_state):
            return current_node
        # check where we can go next and haven't explored
        # print(successors(current_state))
        for child in successors(current_state):
            if child in explored:  # skip children we already explored
                continue
            explored.add(child)
            # create new node as child with current node as parent
            frontier.push(Node(child, current_node))
    return None  # went through everything and never found goal


if __name__ == "__main__":
    print(binary_contains([1, 5, 15, 15, 15, 15, 20], 5))
    print(binary_contains(["a", "d", "e", "f", "z"], "f"))
    print(binary_contains(["john", "mark", "ronald", "sarah"], "sheila"))
