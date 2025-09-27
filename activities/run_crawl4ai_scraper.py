import os, subprocess, sys
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_crawl4ai_scraper():
    logger = get_activity_logger("crawl4ai_scraper")
    logger.info("Starting Crawl4AI scraper subprocess")
    try:
        cmd = [sys.executable, "src/main/crawl4ai_main.py"]
        result = subprocess.run(cmd, cwd=os.path.expanduser("~/scroopy_agent"), check=True, capture_output=True, text=True)
        logger.info("Crawl4AI scraper subprocess completed successfully")
        if result.stdout:
            logger.info(f"Crawl4AI scraper output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Crawl4AI scraper subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Crawl4AI scraper stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise
