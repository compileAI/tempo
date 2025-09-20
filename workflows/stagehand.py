from datetime import timedelta
from temporalio.common import RetryPolicy
from temporalio import workflow
from activities import (
    run_stagehand, run_scroopy_custom
)

@workflow.defn
class StagehandWorkflow: #THIS IS ACTUALLY THE STAGEHAND WORKFLOW
    @workflow.run
    async def run(self) -> None:
        await workflow.execute_activity(
            run_stagehand,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )
        await workflow.execute_activity(
            run_scroopy_custom,
            start_to_close_timeout=timedelta(hours=2),
            retry_policy=RetryPolicy(
                maximum_attempts=3,
            )
        )