import subprocess
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_cluster():
    logger = get_activity_logger("cluster")
    logger.info("Starting Cluster subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/home/compile-dev/compile/scripts/run_cluster.sh"], check=True, capture_output=True, text=True)
        logger.info("Cluster subprocess completed successfully")
        if result.stdout:
            logger.info(f"Cluster output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Cluster subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Cluster stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise