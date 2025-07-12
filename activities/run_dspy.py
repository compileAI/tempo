import subprocess
from temporalio import activity

@activity.defn
async def run_dspy():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_dspy.sh"], check=True) 