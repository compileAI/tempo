import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_faq_batch():
    logger = get_activity_logger()
    logger.info("Starting Faq Batch subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_faq_batch.sh"], check=True, capture_output=True, text=True)
        logger.info("Faq Batch subprocess completed successfully")
        if result.stdout:
            logger.info(f"Faq Batch output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Faq Batch subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Faq Batch stderr: {e.stderr}")
        raise
