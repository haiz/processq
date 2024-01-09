import random
import asyncio

from processq import ProcessQueue


async def worker(data, uid: int = 0, pb: int = 0):
    await asyncio.sleep(random.randint(1, 2))
    print({"data": data, "uid": uid, "pb": pb})


async def worker_params_builder():
    await asyncio.sleep(0.1)
    return {"pb": random.randint(10, 99)}


async def on_close_process(**kwargs):
    await asyncio.sleep(0.1)
    print(f"ON CLOSE PROCESS: {kwargs}")


async def consumer():
    # Start process queue
    async with ProcessQueue(
        10, worker, worker_params_builder=worker_params_builder, worker_params={"uid": random.randint(1, 10)},
        on_close_process=on_close_process
    ) as pq:
        for i in range(1, 30):
            await pq.put({"r": i})


if __name__ == "__main__":
    # export PYTHONPATH=[Path to src]
    asyncio.run(consumer())
