import subprocess
from temporalio import activity

@activity.defn
async def run_automations():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_automations.sh"], check=True) 