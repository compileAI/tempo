import subprocess
from temporalio import activity
from simple_logging import get_simple_logger

@activity.defn
async def run_scrape():
    logger = get_simple_logger()
    logger.info("Starting scrape subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_scrape.sh"], check=True, capture_output=True, text=True)
        logger.info("Scrape subprocess completed successfully")
        if result.stdout:
            logger.info(f"Scrape output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scrape subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Scrape stderr: {e.stderr}")
        raise
