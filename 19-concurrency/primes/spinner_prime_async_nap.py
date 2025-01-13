#!/usr/bin/env python

import asyncio
import itertools
import math


async def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
        # every 100.000 times return control to async event loop
        if i % 100_000 == 1:
            await asyncio.sleep(0)
    return True


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


async def check(n: int) -> int:
    return await is_prime(n)


async def supervisor(n: int) -> int:
    spinner = asyncio.create_task(spin("thinking!"))
    print("spinner object:", spinner)
    result = await check(n)
    spinner.cancel()
    return result


if __name__ == "__main__":
    n = 5_000_111_000_222_021
    result = asyncio.run(supervisor(n))
    msg = "is" if result else "is not"
    print(f"{n:,} {msg} prime")
