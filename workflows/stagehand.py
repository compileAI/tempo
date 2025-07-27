from datetime import timedelta
from temporalio import workflow

from activities import run_stagehand

@workflow.defn
class StagehandWorkflow:
    @workflow.run
    async def run(self) -> None:
        # Keep the activity on the dedicated queue so it
        # can run in the Playwright‑ready container
        return await workflow.execute_activity(
            run_stagehand,
            start_to_close_timeout=timedelta(minutes=30),
            task_queue="stagehand-tq",
        )
