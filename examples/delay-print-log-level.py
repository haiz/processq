import logging
import time
import random

from processq import ProcessQueue


def worker(data):
    time.sleep(random.randint(1, 2))
    # print(data["n"])
    if data["n"] % 10 == 9:
        raise Exception(f"Invalid n: {data['n']}")


def consumer():
    with ProcessQueue(
            10, worker, log_dir="logs", console_log_level=logging.CRITICAL, file_log_level=logging.INFO
    ) as pq:
        for i in range(1, 30):
            pq.put({"n": i})


if __name__ == "__main__":
    # export PYTHONPATH=[Path to src]
    consumer()
