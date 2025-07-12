import subprocess
from temporalio import activity

@activity.defn
async def run_scoop_clustering():
    subprocess.run([
        "/root/miniforge3/bin/python3", 
        "scripts/daily_clustering.py"
    ], cwd="/root/scoop", check=True) 