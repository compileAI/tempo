import subprocess, sys
from temporalio import activity

@activity.defn
async def run_stagehand():
    subprocess.run(
        [sys.executable, "src/stagehand/two_step_stagehand.py"],
        cwd="/app/scroopy_agent",
        check=True,
    )