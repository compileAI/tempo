import os, subprocess, sys
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_scroopy_custom():
    logger = get_activity_logger("scroopy_custom")
    logger.info("Starting Scroopy Custom subprocess")
    try:
        cmd = ["xvfb-run", "-a", sys.executable, "src/main/custom_main.py"]
        result = subprocess.run(cmd, cwd=os.path.expanduser("~/scroopy_agent"), check=True, capture_output=True, text=True)
        logger.info("Scroopy Custom subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scroopy Custom output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scroopy Custom subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scroopy Custom stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise