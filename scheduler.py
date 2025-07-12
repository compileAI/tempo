from temporalio.client import Client
from temporalio.schedules import Schedule, ScheduleSpec, ScheduleActionStartWorkflow
from workflows.article_generation import ArticleGenWorkflow

async def main():
    client = await Client.connect("localhost:7233")

    await client.create_schedule(
        id="daily-article-gen-workflow",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["0 5 * * *"]),  # 5:00 AM daily
            action=ScheduleActionStartWorkflow(
                workflow_type=ArticleGenWorkflow,
                task_queue="default",
            ),
        )
    )

import asyncio
asyncio.run(main())
