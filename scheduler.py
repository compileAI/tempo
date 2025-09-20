from temporalio.client import (
    Client,
    Schedule,
    ScheduleSpec,
    ScheduleActionStartWorkflow,
)
from workflows.stagehand import StagehandWorkflow
from workflows.article_generation import ArticleGenWorkflow


async def main() -> None:
    client = await Client.connect("localhost:7233")

    await client.create_schedule(
        id="daily-article-gen-workflow",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["30 */4 * * *"]),
            action=ScheduleActionStartWorkflow(
                workflow=ArticleGenWorkflow,
                id="article-gen-instance",
                task_queue="default",
            ),
        ),
    )

    await client.create_schedule(
        id="daily-stagehand-workflow",
        schedule=Schedule(
            spec=ScheduleSpec(cron_expressions=["0 4 * * *"]),
            action=ScheduleActionStartWorkflow(
                workflow=StagehandWorkflow,
                id="stagehand-instance",
                task_queue="stagehand",
            ),
        ),
    )

if __name__ == "__main__":
    import asyncio 
    asyncio.run(main())
