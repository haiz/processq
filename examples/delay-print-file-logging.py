import time
import random

from processq import ProcessQueue


def worker(data):
    if data["n"] % 10 == 9:
        raise Exception("Invalid n")


def consumer():
    with ProcessQueue(10, worker, log_dir="logs") as pq:
        for i in range(1, 30):
            pq.put({"n": i})


def consumer_retry():
    with ProcessQueue(10, worker, log_dir="logs", retry_count=2) as pq:
        for i in range(1, 10):
            pq.put({"n": i})


if __name__ == "__main__":
    # export PYTHONPATH=[Path to src]
    # consumer()
    consumer_retry()
