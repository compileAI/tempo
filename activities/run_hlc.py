import subprocess
from temporalio import activity

@activity.defn
async def run_hlc():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_hlc.sh"], check=True)