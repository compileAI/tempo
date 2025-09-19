import logging
import os
from datetime import datetime
from temporalio import workflow, activity

def setup_execution_logger():
    """Set up a simple logger for workflow execution - activities will handle file creation."""
    try:
        # Get the unique workflow execution info
        workflow_info = workflow.info()
        run_id = workflow_info.run_id
        
        # Create a simple logger for workflow-level messages
        logger_name = f"temporal_workflow_{run_id}"
        logger = logging.getLogger(logger_name)
        
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            # Only console logging from workflow (file creation happens in activities)
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - WORKFLOW - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        return logger, run_id
        
    except Exception as e:
        # Fallback to basic logging if workflow context not available
        logger = logging.getLogger("temporal_fallback")
        logger.error(f"Failed to set up execution-specific logging: {e}")
        return logger, "unknown"

def get_activity_logger():
    """Get the logger for the current activity, with file logging setup."""
    try:
        # Get activity info to match with workflow
        activity_info = activity.info()
        workflow_run_id = activity_info.workflow_run_id
        workflow_id = activity_info.workflow_id
        
        # Create unique logger name
        logger_name = f"temporal_execution_{workflow_run_id}"
        logger = logging.getLogger(logger_name)
        
        # If logger doesn't have handlers, set them up
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            # Create logs directory from activity (allowed, unlike from workflow)
            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)
            
            # Create log file using activity start time
            import time
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            log_filename = f"{workflow_id}_{timestamp}_{workflow_run_id[:8]}.log"
            log_path = os.path.join(log_dir, log_filename)
            
            # Add file handler
            file_handler = logging.FileHandler(log_path)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            
            # Add console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            
            logger.info(f"Activity-level logging initialized: {log_path}")
        
        return logger
        
    except Exception as e:
        # Fallback to basic logging if activity context not available
        logger = logging.getLogger("temporal_activity_fallback")
        logger.error(f"Failed to get activity logger: {e}")
        return logger
