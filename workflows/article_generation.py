from datetime import timedelta
from temporalio.common import RetryPolicy
from temporalio import workflow
from activities import (
    run_scrape, run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch,
    run_automations, run_hlc
)

@workflow.defn
class ArticleGenWorkflow:
    @workflow.run
    async def run(self) -> None:
        # Execute activities sequentially - each activity handles its own logging
        await workflow.execute_activity(
            run_scrape,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        
        await workflow.execute_activity(
            run_scoop_preprocess,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        
        await workflow.execute_activity(
            run_scoop_clustering,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        
        await workflow.execute_activity(
            run_cluster,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        
        await workflow.execute_activity(
            run_hlc,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        
        await workflow.execute_activity(
            run_automations,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        
        await workflow.execute_activity(
            run_faq_batch,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(maximum_attempts=3)
        )