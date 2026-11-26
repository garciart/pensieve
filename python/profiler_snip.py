"""A snippet that profiles a function.

Usage: python -B profiler_snip.py
"""
from datetime import timedelta
import time


def test_function(delay: float = 3.14) -> None:
    """Function to test profiling.

    :param float delay: Delay in seconds, defaults to 3.14.
    """
    time.sleep(delay)


if __name__ == '__main__':
    print('Profiling function...')
    start_time = time.perf_counter()
    test_function(12.34)
    end_time = time.perf_counter()
    elapsed_seconds = end_time - start_time
    elapsed_time = str(timedelta(seconds=elapsed_seconds))
    print('Profiling ended.')
    print(f"Elapsed seconds: {elapsed_seconds}")
    print(f"Elapsed time (h.m.s): {elapsed_time}")
