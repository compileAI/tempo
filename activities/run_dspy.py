import subprocess
from temporalio import activity
from activity_logging import get_activity_logger

@activity.defn
async def run_dspy():
    logger = get_activity_logger("dspy")
    logger.info("Starting Dspy subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_dspy.sh"], check=True, capture_output=True, text=True)
        logger.info("Dspy subprocess completed successfully")
        if result.stdout:
            logger.info(f"Dspy output: {result.stdout}")
        logger.info("EXECUTION COMPLETED SUCCESSFULLY")
    except subprocess.CalledProcessError as e:
        logger.error(f"Dspy subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Dspy stderr: {e.stderr}")
        logger.error("EXECUTION FAILED")
        raise
