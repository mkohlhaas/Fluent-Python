import asyncio
import itertools
import time


# THIS WILL NEVER BE OUTPUT
async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, flush=True, end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break


async def slow() -> int:
    time.sleep(3)  # wrong sleep function -> blocks async
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin("thinking!"))
    print(f"spinner object: {spinner}")
    result = await slow()
    spinner.cancel()
    return result


if __name__ == "__main__":
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")
