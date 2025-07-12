import subprocess
from temporalio import activity

@activity.defn
async def run_enhanced_articles():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_enhanced_articles.sh"], check=True) 