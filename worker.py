import asyncio
from temporalio.worker import Worker
from temporalio.client import Client

# Import all activities
from activities.run_scrape import run_scrape
from activities.run_vdb import run_vdb
from activities.run_dspy import run_dspy
from activities.run_cluster import run_cluster
from activities.run_faq_batch import run_faq_batch
from activities.run_scoop_preprocess import run_scoop_preprocess
from activities.run_scoop_clustering import run_scoop_clustering
from activities.run_enhanced_articles import run_enhanced_articles

# Import all workflows
from workflows.daily_master_workflow import DailyMasterWorkflow
from workflows.daily_scraping_workflow import DailyScrapingWorkflow
from workflows.daily_processing_workflow import DailyProcessingWorkflow
from workflows.daily_content_generation_workflow import DailyContentGenerationWorkflow
from workflows.daily_faq_workflow import DailyFAQWorkflow
from workflows.article_generation import ArticleGenWorkflow

async def main():
    client = await Client.connect("localhost:7233")
    
    # Run the worker
    worker = Worker(
        client,
        task_queue="daily-tasks",
        workflows=[
            DailyMasterWorkflow,
            DailyScrapingWorkflow,
            DailyProcessingWorkflow,
            DailyContentGenerationWorkflow,
            DailyFAQWorkflow,
            ArticleGenWorkflow,
        ],
        activities=[
            run_scrape,
            run_vdb,
            run_dspy,
            run_cluster,
            run_faq_batch,
            run_scoop_preprocess,
            run_scoop_clustering,
            run_enhanced_articles,
        ],
    )
    
    print("Starting Temporal worker...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main()) 