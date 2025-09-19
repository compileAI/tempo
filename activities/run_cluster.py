import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_cluster():
    logger = get_activity_logger()
    logger.info("Starting cluster subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_cluster.sh"], check=True, capture_output=True, text=True)
        logger.info("Cluster subprocess completed successfully")
        if result.stdout:
            logger.info(f"Cluster output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Cluster subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Cluster stderr: {e.stderr}")
        raise