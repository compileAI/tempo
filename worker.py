from temporalio.client import Client
from temporalio.worker import Worker
from workflows.article_generation import ArticleGenWorkflow
from activities import (
    run_scrape, run_dspy, run_vdb,
    run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch, run_enhanced_articles,
    run_automations, run_hlc
)

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="default",  # task queue used by the workflow
        workflows=[ArticleGenWorkflow],
        activities=[
            run_scrape, run_dspy, run_vdb,
            run_scoop_preprocess, run_scoop_clustering,
            run_cluster, run_faq_batch, run_enhanced_articles,
            run_automations, run_hlc,
        ],
    )
    await worker.run()

import asyncio
asyncio.run(main())
