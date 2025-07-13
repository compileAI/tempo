from temporalio.client import Client, ScheduleSpec

async def main():
    client = await Client.connect("localhost:7233")
    handle = await client.get_schedule_handle("daily-article-gen-workflow")

    async def updater(sched):
        # set/replace the time-zone
        sched.spec.time_zone_name = "America/Toronto"  # IANA zone
        return sched.spec   # return mutated spec

    await handle.update(updater)

import asyncio; asyncio.run(main())
