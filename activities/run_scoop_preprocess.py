import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_scoop_preprocess():
    logger = get_activity_logger()
    logger.info("Starting Scoop Preprocess subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_scoop_preprocess.sh"], check=True, capture_output=True, text=True)
        logger.info("Scoop Preprocess subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scoop Preprocess output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scoop Preprocess subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scoop Preprocess stderr: {e.stderr}")
        raise
