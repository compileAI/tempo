import logging
import os
from datetime import datetime
from temporalio import workflow, activity

def setup_execution_logger():
    """Set up a logger specific to the current workflow execution."""
    try:
        # Get the unique workflow execution info
        workflow_info = workflow.info()
        run_id = workflow_info.workflow_execution.run_id
        workflow_id = workflow_info.workflow_execution.workflow_id
        
        # Create unique log file name
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        
        # Use timestamp and run_id for unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"{workflow_id}_{timestamp}_{run_id[:8]}.log"
        log_path = os.path.join(log_dir, log_filename)
        
        # Set up logger with unique name per execution
        logger_name = f"temporal_execution_{run_id}"
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        
        # Clear any existing handlers to avoid conflicts
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        # Add file handler for this specific execution
        file_handler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Also add console handler for immediate feedback
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        logger.info(f"Execution-specific logging initialized: {log_path}")
        return logger, run_id
        
    except Exception as e:
        # Fallback to basic logging if workflow context not available
        logger = logging.getLogger("temporal_fallback")
        logger.error(f"Failed to set up execution-specific logging: {e}")
        return logger, "unknown"

def get_activity_logger():
    """Get the logger for the current activity, matching the workflow execution."""
    try:
        # Get activity info to match with workflow
        activity_info = activity.info()
        workflow_run_id = activity_info.workflow_execution.run_id
        
        # Use the same logger name as the workflow
        logger_name = f"temporal_execution_{workflow_run_id}"
        logger = logging.getLogger(logger_name)
        
        # If logger doesn't exist, create a basic one
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        return logger
        
    except Exception as e:
        # Fallback to basic logging if activity context not available
        logger = logging.getLogger("temporal_activity_fallback")
        logger.error(f"Failed to get activity logger: {e}")
        return logger
