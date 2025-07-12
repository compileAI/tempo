import subprocess
from temporalio import activity

@activity.defn
async def run_scrape():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_scrape.sh"], check=True)
