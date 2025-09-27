import os, subprocess, sys
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_rss_scraper():
    logger = get_activity_logger("rss_scraper")
    logger.info("Starting RSS scraper subprocess")
    try:
        cmd = [sys.executable, "src/main/rss_main.py"]
        result = subprocess.run(cmd, cwd=os.path.expanduser("~/scroopy_agent"), check=True, capture_output=True, text=True)
        logger.info("RSS scraper subprocess completed successfully")
        if result.stdout:
            logger.info(f"RSS scraper output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"RSS scraper subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"RSS scraper stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise
