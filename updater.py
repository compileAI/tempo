import asyncio
from temporalio.client import Client, ScheduleSpec

async def main():
    client = await Client.connect("localhost:7233")
    
    # update daily article gen workflow
    handle = client.get_schedule_handle("daily-article-gen-workflow")
    # lambda is a hack to get the await
    await handle.update(lambda _: handle.spec.time_zone_name == "America/Toronto")

    # update daily stagehand workflow
    handle = client.get_schedule_handle("daily-stagehand-workflow")
    await handle.update(lambda _: handle.spec.time_zone_name == "America/Toronto")

if __name__ == "__main__":
    asyncio.run(main())
