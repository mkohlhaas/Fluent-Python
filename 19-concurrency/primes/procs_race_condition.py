#!/usr/bin/env python3

"""
procs.py: shows that multiprocessing on a multicore machine
can be faster than sequential code for CPU-intensive work.
"""

import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]
ResultQueue = queues.SimpleQueue[PrimeResult]


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:
    while n := jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))


def start_jobs(workers: int) -> ResultQueue:
    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()

    for n in NUMBERS:
        jobs.put(n)

    for _ in range(workers):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0)

    return results


def report(workers: int, results: ResultQueue) -> int:
    workers_done = 0
    checked = 0
    while workers_done < workers:
        n, prime, elapsed = results.get()
        if n == 0:
            workers_done += 1
        else:
            checked += 1
            label = "P" if prime else " "
            print(f"{n:16}  {label} {elapsed:9.6f}s")
    return checked


if __name__ == "__main__":
    if len(sys.argv) < 2:
        workers = cpu_count()
    else:
        workers = int(sys.argv[1])

    print(f"Checking {len(NUMBERS)} numbers with {workers} processes:")
    t0 = perf_counter()
    results = start_jobs(workers)
    checked = report(workers, results)
    elapsed = perf_counter() - t0
    print(f"{checked} checks in {elapsed:.2f}s")
