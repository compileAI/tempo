import os
import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflows.stagehand import StagehandWorkflow
from workflows.article_generation import ArticleGenWorkflow
from activities import (
    run_scrape,
    run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch,
    run_automations, run_hlc, run_stagehand, run_scroopy_custom
)

async def main():
    client = await Client.connect(os.getenv("TEMPORAL_ADDRESS", "localhost:7233"))
    stagehand_worker = Worker(
        client,
        task_queue="stagehand",  # dedicated task queue for stagehand-only worker
        workflows=[StagehandWorkflow],
        activities=[
            run_stagehand,
            run_scroopy_custom,
        ],
    )

    article_gen_worker = Worker(
        client,
        task_queue="default",
        workflows=[ArticleGenWorkflow],
        activities=[
            run_scrape,
            run_scoop_preprocess,
            run_scoop_clustering,
            run_cluster,
            run_faq_batch,
            run_automations,
            run_hlc,
        ],
    )

    await asyncio.gather(
        stagehand_worker.run(),
        article_gen_worker.run(),
    )

asyncio.run(main())
