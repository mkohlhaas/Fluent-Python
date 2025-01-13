#!/usr/bin/env python

import itertools
from threading import Thread, Event

from primes import is_prime


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        if done.wait(0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def supervisor(n: int) -> bool:
    done = Event()
    spinner = Thread(target=spin, args=("thinking!", done))
    print(f"spinner object: {spinner}")
    spinner.start()
    result = is_prime(n)
    done.set()
    spinner.join()
    return result


if __name__ == "__main__":
    n = 5_000_111_000_222_021
    result = supervisor(n)
    msg = "is" if result else "is not"
    print(f"{n:,} {msg} prime")
