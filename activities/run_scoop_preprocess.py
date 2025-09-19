import subprocess
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_scoop_preprocess():
    logger = get_activity_logger("scoop_preprocess")
    logger.info("Starting scoop preprocess subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_scoop_preprocess.sh"], check=True, capture_output=True, text=True)
        logger.info("Scoop preprocess subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scoop preprocess output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scoop preprocess subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scoop preprocess stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise
