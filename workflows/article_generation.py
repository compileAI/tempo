from datetime import timedelta
from temporalio.common import RetryPolicy
from temporalio import workflow
from activities import (
    run_scrape, run_dspy, run_vdb,
    run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch, run_enhanced_articles,
)

@workflow.defn
class ArticleGenWorkflow:
    @workflow.run
    async def run(self) -> None:
        await workflow.execute_activity(
            run_scrape,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
        await workflow.execute_activity(
            run_scoop_preprocess,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
        await workflow.execute_activity(
            run_scoop_clustering,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
        await workflow.execute_activity(
            run_cluster,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
        await workflow.execute_activity(
            run_faq_batch,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
        await workflow.execute_activity(
            run_enhanced_articles,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
