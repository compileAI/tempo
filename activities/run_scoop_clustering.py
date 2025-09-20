import subprocess
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_scoop_clustering():
    logger = get_activity_logger("scoop_clustering")
    logger.info("Starting Scoop Clustering subprocess")
    try:
        result = subprocess.run([
            "/usr/bin/python3", 
            "scripts/daily_clustering.py"
        ], cwd="/home/compile-dev/scoop", check=True, capture_output=True, text=True) 
        logger.info("Scoop Clustering subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scoop Clustering output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scoop Clustering subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scoop Clustering stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise