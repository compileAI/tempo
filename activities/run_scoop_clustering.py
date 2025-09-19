import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_scoop_clustering():
    logger = get_activity_logger()
    logger.info("Starting Scoop Clustering subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_scoop_clustering.sh"], check=True, capture_output=True, text=True)
        logger.info("Scoop Clustering subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scoop Clustering output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scoop Clustering subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scoop Clustering stderr: {e.stderr}")
        raise
