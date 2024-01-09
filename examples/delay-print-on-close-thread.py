import time
import random
import asyncio

from processq import ProcessQueue


def worker(data, uid: int = 0, pb: int = 0):
    time.sleep(random.randint(1, 2))
    print({"data": data, "uid": uid, "pb": pb})


def worker_params_builder():
    return {"pb": random.randint(10, 99)}


def on_close_process(**kwargs):
    print(f"ON CLOSE PROCESS: {kwargs}")


def consumer():
    # Start process queue
    with ProcessQueue(
        10, worker, worker_params_builder=worker_params_builder, worker_params={"uid": random.randint(1, 10)},
        on_close_process=on_close_process
    ) as pq:
        for i in range(1, 30):
            pq.put({"r": i})


if __name__ == "__main__":
    # export PYTHONPATH=[Path to src]
    consumer()
