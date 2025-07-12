import subprocess
from temporalio import activity

@activity.defn
async def run_vdb():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_vdb.sh"], check=True) 