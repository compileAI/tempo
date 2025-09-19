import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_enhanced_articles():
    logger = get_activity_logger()
    logger.info("Starting Enhanced Articles subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_enhanced_articles.sh"], check=True, capture_output=True, text=True)
        logger.info("Enhanced Articles subprocess completed successfully")
        if result.stdout:
            logger.info(f"Enhanced Articles output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Enhanced Articles subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Enhanced Articles stderr: {e.stderr}")
        raise
