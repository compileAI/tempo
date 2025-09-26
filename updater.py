import asyncio
from temporalio.client import Client, ScheduleSpec, ScheduleUpdate

async def main():
    client = await Client.connect("localhost:7233")

    def update_timezone(input):
        return ScheduleUpdate(
            schedule=input.description.schedule.with_spec(
                input.description.schedule.spec.with_time_zone_name("America/Toronto")
            )
        )
    
    # update daily article gen workflow
    handle = client.get_schedule_handle("daily-article-gen-workflow")
    await handle.update(update_timezone)

    # update daily stagehand workflow
    handle = client.get_schedule_handle("daily-stagehand-workflow")
    await handle.update(update_timezone)

if __name__ == "__main__":
    asyncio.run(main())
