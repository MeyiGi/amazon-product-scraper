import time
import random
from typing import Iterable

def random_delay(min_delay: float, max_delay) -> None:
    time.sleep(random.uniform(min_delay, max_delay))

def random_proxy(proxies: Iterable[str]) -> str:
    return random.choice(proxies)