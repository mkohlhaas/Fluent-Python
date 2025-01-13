#!/usr/bin/env python

import asyncio
import itertools

import primes


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print("THIS WILL NEVER BE OUTPUT")


async def check(n: int) -> int:
    return primes.is_prime(n)


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
