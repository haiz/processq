import time
import random
from datetime import datetime

from processq import ProcessQueue


def process_child(child_id: int):
    print(f"start child {child_id} {datetime.utcnow()}")
    time.sleep(random.randint(0, 2))
    print(f"end child {child_id} {datetime.utcnow()}")


def process_parent(parent_id: int):
    print(f"start parent {parent_id} {datetime.utcnow()}")
    with ProcessQueue(2, process_child, name=f"Child#{parent_id}") as pq:
        for i in range(3):
            pq.put(parent_id * 10 + i)
    print(f"start parent {parent_id} {datetime.utcnow()}")


def run():
    with ProcessQueue(2, process_parent, name="Parent") as pq:
        for i in range(3):
            pq.put(i)


if __name__ == '__main__':
    # export PYTHONPATH=[Path to src]
    run()
