import subprocess
from temporalio import activity

@activity.defn
async def run_faq_batch():
    subprocess.run(["/bin/bash", "/root/compile/scripts/run_faq_batch.sh"], check=True) 