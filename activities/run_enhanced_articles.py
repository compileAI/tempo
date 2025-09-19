import subprocess
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_enhanced_articles():
    logger = get_activity_logger("enhanced_articles")
    logger.info("Starting Enhanced Articles subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_enhanced_articles.sh"], check=True, capture_output=True, text=True)
        logger.info("Enhanced Articles subprocess completed successfully")
        if result.stdout:
            logger.info(f"Enhanced Articles output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Enhanced Articles subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Enhanced Articles stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise
