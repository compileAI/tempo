import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_vdb():
    logger = get_activity_logger()
    logger.info("Starting Vdb subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_vdb.sh"], check=True, capture_output=True, text=True)
        logger.info("Vdb subprocess completed successfully")
        if result.stdout:
            logger.info(f"Vdb output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Vdb subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Vdb stderr: {e.stderr}")
        raise
