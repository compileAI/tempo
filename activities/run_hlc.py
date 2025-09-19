import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_hlc():
    logger = get_activity_logger()
    logger.info("Starting Hlc subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_hlc.sh"], check=True, capture_output=True, text=True)
        logger.info("Hlc subprocess completed successfully")
        if result.stdout:
            logger.info(f"Hlc output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Hlc subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Hlc stderr: {e.stderr}")
        raise
