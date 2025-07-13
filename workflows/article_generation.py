from temporalio import workflow
from activities.run_scrape import run_scrape
from activities.run_dspy import run_dspy
from activities.run_vdb import run_vdb
from activities.run_scoop_preprocess import run_scoop_preprocess
from activities.run_scoop_clustering import run_scoop_clustering
from activities.run_cluster import run_cluster
from activities.run_faq_batch import run_faq_batch
from activities.run_enhanced_articles import run_enhanced_articles
from activities import (
    run_scrape, run_dspy, run_vdb,
    run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch, run_enhanced_articles,
)

@workflow.defn
class ArticleGenWorkflow:
    @workflow.run
    async def run(self) -> None:
        await workflow.execute_activity(run_scrape)
        await workflow.execute_activity(run_dspy)
        await workflow.execute_activity(run_vdb)
        await workflow.execute_activity(run_scoop_preprocess)
        await workflow.execute_activity(run_scoop_clustering)
        await workflow.execute_activity(run_cluster)
        await workflow.execute_activity(run_faq_batch)
        await workflow.execute_activity(run_enhanced_articles)
