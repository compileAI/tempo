import asyncio
from temporalio.client import Client, ScheduleSpec

async def main():
    client = await Client.connect("localhost:7233")

    def update_timezone(input):
        input.description.schedule.spec.time_zone_name = "America/Toronto"
        return input.description
    
    # update daily article gen workflow
    handle = client.get_schedule_handle("daily-article-gen-workflow")
    await handle.update(update_timezone)

    # update daily stagehand workflow
    handle = client.get_schedule_handle("daily-stagehand-workflow")
    await handle.update(update_timezone)

if __name__ == "__main__":
    asyncio.run(main())
