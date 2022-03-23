from typing import Generator
from typing import Dict
# global object for memoization
memo: Dict[int, int] = {0: 0, 1: 1}  # base case


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-1)+fib(n-2)
    return memo[n]


def generator_fib(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0:
        yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    print(fib(50))

    # with enumerate can handel when print the result
    for i, data in enumerate(generator_fib(50)):
        if i == 50:
            print(data)
