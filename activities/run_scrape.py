import subprocess
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_scrape():
    logger = get_activity_logger("scrape")
    logger.info("Starting scrape subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_scrape.sh"], check=True, capture_output=True, text=True)
        logger.info("Scrape subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scrape output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scrape subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scrape stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise
