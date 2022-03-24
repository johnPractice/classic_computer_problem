from typing import Generic, List, TypeVar


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin=begin, end=temp, temp=end, n=n-1)
        hanoi(begin=begin, end=end, temp=temp, n=1)
        hanoi(begin=temp, end=end, temp=begin, n=n-1)


def main():
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    print(tower_a)
    print(tower_b)
    print(tower_c)
    hanoi(begin=tower_a, end=tower_c, temp=tower_b, n=num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)


if __name__ == '__main__':
    main()
