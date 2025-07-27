import asyncio, os
from temporalio.client import Client
from temporalio.worker import Worker
from activities import run_stagehand

async def main():
    client = await Client.connect(os.getenv("TEMPORAL_ADDRESS", "localhost:7233"))
    async with Worker(
        client,
        task_queue="stagehand-tq",
        activities=[run_stagehand],
    ):
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
