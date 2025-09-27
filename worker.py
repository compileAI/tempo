import os
import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflows.scrape import DailyScrapeWorkflow
from workflows.article_generation import ArticleGenWorkflow
from activities import (
    run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch,
    run_automations, run_hlc, run_stagehand, run_scroopy_custom,
    run_rss_scraper, run_crawl4ai_scraper
)

async def main():
    client = await Client.connect(os.getenv("TEMPORAL_ADDRESS", "localhost:7233"))
    
    # Scraping worker - handles all scraping activities
    scrape_worker = Worker(
        client,
        task_queue="scrape",  # dedicated task queue for scraping activities
        workflows=[DailyScrapeWorkflow],
        activities=[
            run_stagehand,
            run_scroopy_custom,
            run_rss_scraper,
            run_crawl4ai_scraper,
        ],
    )

    # Article generation worker - handles content generation pipeline
    article_gen_worker = Worker(
        client,
        task_queue="default",
        workflows=[ArticleGenWorkflow],
        activities=[
            run_scoop_preprocess,
            run_scoop_clustering,
            run_cluster,
            run_faq_batch,
            run_automations,
            run_hlc,
        ],
    )

    await asyncio.gather(
        scrape_worker.run(),
        article_gen_worker.run(),
    )

asyncio.run(main())
