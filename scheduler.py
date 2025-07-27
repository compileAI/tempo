from temporalio.client import (
    Client,
    Schedule,
    ScheduleSpec,
    ScheduleActionStartWorkflow,
)
from workflows.article_generation import ArticleGenWorkflow
from workflows.stagehand import StagehandWorkflow

async def main() -> None:
    client = await Client.connect("localhost:7233")

    await client.create_schedule(
        id="daily-article-gen-workflow",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["0 5 * * *"]),   # 5 AM daily
            action=ScheduleActionStartWorkflow(
                workflow=ArticleGenWorkflow,
                id="article-gen-instance",
                task_queue="default",
            ),
        ),
    )

    await client.create_schedule(
        id="stagehand-nightly",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["30 4 * * *"]),
            action=ScheduleActionStartWorkflow(
                workflow=StagehandWorkflow,
                id="stagehand",
                task_queue="stagehand-tq",
            ),
        ),
    )

if __name__ == "__main__":
    import asyncio 
    asyncio.run(main())
