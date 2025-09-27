import asyncio
from dataclasses import replace
from temporalio.client import Client, ScheduleSpec, ScheduleUpdate

async def main():
    client = await Client.connect("localhost:7233")

    def update_timezone(input):
        # Update the spec with new timezone
        updated_spec = replace(
            input.description.schedule.spec,
            time_zone_name="America/Toronto"
        )
        
        # Update the schedule with new spec
        updated_schedule = replace(
            input.description.schedule,
            spec=updated_spec
        )
        
        return ScheduleUpdate(schedule=updated_schedule)
    
    # update daily article gen workflow
    handle = client.get_schedule_handle("daily-article-gen-workflow")
    await handle.update(update_timezone)

    # update daily scrape workflow
    handle = client.get_schedule_handle("daily-scrape-workflow")
    await handle.update(update_timezone)

if __name__ == "__main__":
    asyncio.run(main())
