from dataclasses import replace
from temporalio.client import (
    Client,
    Schedule,
    ScheduleSpec,
    ScheduleActionStartWorkflow,
    ScheduleUpdate,
)
from workflows.scrape import DailyScrapeWorkflow
from workflows.article_generation import ArticleGenWorkflow


async def main() -> None:
    client = await Client.connect("localhost:7233")

    # Article generation workflow - runs after scraping completes
    await client.create_schedule(
        id="daily-article-gen-workflow",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["30 5,17 * * *"]),
            action=ScheduleActionStartWorkflow(
                workflow=ArticleGenWorkflow,
                id="article-gen-instance",
                task_queue="default",
            ),
        ),
    )

    # Daily scraping workflow - runs before article generation
    await client.create_schedule(
        id="daily-scrape-workflow",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["0 5,17 * * *"]),
            action=ScheduleActionStartWorkflow(
                workflow=DailyScrapeWorkflow,
                id="scrape-instance",
                task_queue="scrape",
            ),
        ),
    )

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
    import asyncio 
    asyncio.run(main())
