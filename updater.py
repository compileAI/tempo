from temporalio.client import Client, ScheduleSpec

def main():
    client = Client.connect("localhost:7233")
    
    # update daily article gen workflow
    handle = client.get_schedule_handle("daily-article-gen-workflow")
    handle.spec.time_zone_name = "America/Toronto"

    # update daily stagehand workflow
    handle = client.get_schedule_handle("daily-stagehand-workflow")
    handle.spec.time_zone_name = "America/Toronto"

if __name__ == "__main__":
    main()
