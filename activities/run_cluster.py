import subprocess
from temporalio import activity

@activity.defn
async def run_cluster():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_cluster.sh"], check=True) 