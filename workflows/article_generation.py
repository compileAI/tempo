from datetime import timedelta
from temporalio.common import RetryPolicy
from temporalio import workflow
from logging_utils import setup_execution_logger
from activities import (
    run_scrape, run_scoop_preprocess, run_scoop_clustering,
    run_cluster, run_faq_batch, run_enhanced_articles,
    run_automations, run_hlc
)

@workflow.defn
class ArticleGenWorkflow:
    @workflow.run
    async def run(self) -> None:
        # Set up execution-specific logging
        logger, run_id = setup_execution_logger()
        logger.info(f"Article generation workflow started - Run ID: {run_id}")
        
        try:
            logger.info("Starting scrape activity")
            await workflow.execute_activity(
                run_scrape,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("Scrape activity completed successfully")
            
            logger.info("Starting scoop preprocess activity")
            await workflow.execute_activity(
                run_scoop_preprocess,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("Scoop preprocess activity completed successfully")
            
            logger.info("Starting scoop clustering activity")
            await workflow.execute_activity(
                run_scoop_clustering,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("Scoop clustering activity completed successfully")
            
            logger.info("Starting cluster activity")
            await workflow.execute_activity(
                run_cluster,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("Cluster activity completed successfully")
            
            logger.info("Starting HLC activity")
            await workflow.execute_activity(
                run_hlc,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("HLC activity completed successfully")
            
            logger.info("Starting automations activity")
            await workflow.execute_activity(
                run_automations,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("Automations activity completed successfully")
            
            logger.info("Starting FAQ batch activity")
            await workflow.execute_activity(
                run_faq_batch,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("FAQ batch activity completed successfully")
            
            logger.info("Starting enhanced articles activity")
            await workflow.execute_activity(
                run_enhanced_articles,
                start_to_close_timeout=timedelta(hours=2),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                )
            )
            logger.info("Enhanced articles activity completed successfully")
            
            logger.info("Article generation workflow completed successfully")
            
        except Exception as e:
            logger.error(f"Workflow failed with error: {str(e)}")
            raise
