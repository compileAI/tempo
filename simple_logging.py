import logging
import os
import time
from temporalio import activity

def get_simple_logger():
    """Get a simple logger for activities that creates execution-specific log files."""
    try:
        # Get activity info
        activity_info = activity.info()
        workflow_run_id = activity_info.workflow_run_id
        workflow_id = activity_info.workflow_id
        
        # Create unique logger per execution
        logger_name = f"temporal_{workflow_run_id}"
        logger = logging.getLogger(logger_name)
        
        # Set up logger if not already configured
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            # Create logs directory
            os.makedirs("logs", exist_ok=True)
            
            # Create log file with timestamp and run ID
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            log_file = f"logs/{workflow_id}_{timestamp}_{workflow_run_id[:8]}.log"
            
            # File handler
            file_handler = logging.FileHandler(log_file)
            file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)
            
            logger.info(f"Logging initialized for execution {workflow_run_id[:8]} -> {log_file}")
        
        return logger
        
    except Exception as e:
        # Fallback logger
        logger = logging.getLogger("temporal_fallback")
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        logger.error(f"Failed to create execution logger: {e}")
        return logger
