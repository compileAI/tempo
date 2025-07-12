import subprocess
from temporalio import activity

@activity.defn
async def run_scoop_preprocess():
    subprocess.run([
        "/root/miniforge3/bin/python3", 
        "scripts/daily_preprocess.py"
    ], cwd="/root/scoop", check=True) 