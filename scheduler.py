import asyncio
from datetime import datetime, time
from temporalio.client import Client
from workflows.daily_master_workflow import DailyMasterWorkflow
from workflows.daily_scraping_workflow import DailyScrapingWorkflow
from workflows.daily_processing_workflow import DailyProcessingWorkflow
from workflows.daily_content_generation_workflow import DailyContentGenerationWorkflow
from workflows.daily_faq_workflow import DailyFAQWorkflow

async def start_daily_workflow(client: Client, workflow_class, workflow_id: str):
    """Start a workflow with a unique ID based on the date."""
    today = datetime.now().strftime("%Y-%m-%d")
    workflow_id = f"{workflow_id}-{today}"
    
    await client.start_workflow(
        workflow_class.run,
        id=workflow_id,
        task_queue="daily-tasks"
    )
    print(f"Started workflow: {workflow_id}")

async def schedule_daily_workflows():
    """Schedule all daily workflows based on the original cron timing."""
    client = await Client.connect("localhost:7233")
    
    # Start the master workflow that handles everything
    await start_daily_workflow(client, DailyMasterWorkflow, "daily-master")
    
    # Alternatively, you can start individual workflows at specific times:
    # await start_daily_workflow(client, DailyScrapingWorkflow, "daily-scraping")
    # await start_daily_workflow(client, DailyProcessingWorkflow, "daily-processing")
    # await start_daily_workflow(client, DailyContentGenerationWorkflow, "daily-content")
    # await start_daily_workflow(client, DailyFAQWorkflow, "daily-faq")

if __name__ == "__main__":
    asyncio.run(schedule_daily_workflows()) 