import logging
import os
import time
from temporalio import activity

def get_activity_logger(activity_name):
    """Get a logger for a specific activity type that logs to its own file."""
    try:
        # Get activity info for run context
        activity_info = activity.info()
        workflow_run_id = activity_info.workflow_run_id
        workflow_id = activity_info.workflow_id
        
        # Create logger name based on activity
        logger_name = f"activity_{activity_name}"
        logger = logging.getLogger(logger_name)
        
        # Set up logger if not already configured
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            # Create logs directory
            os.makedirs("logs", exist_ok=True)
            
            # Create log file for this activity type
            log_file = f"logs/{activity_name}.log"
            
            # File handler that appends
            file_handler = logging.FileHandler(log_file, mode='a')
            file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter(f'{activity_name} - %(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)
        
        # Log execution separator with run info
        separator = "-" * 80
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"\n{separator}")
        logger.info(f"NEW EXECUTION STARTED - {timestamp}")
        logger.info(f"Workflow ID: {workflow_id}")
        logger.info(f"Run ID: {workflow_run_id}")
        logger.info(f"{separator}")
        
        return logger
        
    except Exception as e:
        # Fallback logger
        logger = logging.getLogger(f"fallback_{activity_name}")
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(f'{activity_name} - %(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        logger.error(f"Failed to create activity logger: {e}")
        return logger
