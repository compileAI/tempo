import subprocess
from temporalio import activity
from logging_utils import get_activity_logger

@activity.defn
async def run_automations():
    logger = get_activity_logger()
    logger.info("Starting Automations subprocess")
    try:
        result = subprocess.run(["/bin/bash", "/root/compile/scripts/run_automations.sh"], check=True, capture_output=True, text=True)
        logger.info("Automations subprocess completed successfully")
        if result.stdout:
            logger.info(f"Automations output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Automations subprocess failed with error: {e}")
        if e.stderr:
            logger.error(f"Automations stderr: {e.stderr}")
        raise
