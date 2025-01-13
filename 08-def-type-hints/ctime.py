import time
from typing import Optional


def ctime(secs: Optional[float] = None, /) -> str:
    return time.ctime(secs)


if __name__ == "__main__":
    # ctime(secs=0.23)
    ctime(0.23)
