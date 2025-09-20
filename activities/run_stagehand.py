import os, subprocess, sys
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_stagehand():
    logger = get_activity_logger("stagehand")
    logger.info("Starting Stagehand subprocess")
    try:
        cmd = ["xvfb-run", "-a", sys.executable, "src/main/stagehand_main.py"]
        result = subprocess.run(cmd, cwd=os.path.expanduser("~/scroopy_agent"), check=True, capture_output=True, text=True)
        logger.info("Stagehand subprocess completed successfully")
        if result.stdout:
            logger.info(f"Stagehand output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Stagehand subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Stagehand stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise