import time
import random

from processq import ProcessQueue


def worker(data):
    time.sleep(random.random())
    print("Process data: ", data)


def consumer():
    with ProcessQueue(2, worker) as pq:
        for i in range(1, 30):
            pq.put({"n": i})


if __name__ == "__main__":
    # export PYTHONPATH=[Path to src]
    consumer()
