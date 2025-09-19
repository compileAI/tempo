## tempo <-> compile scheduling engine

*... this is where we replace all the cron stuff*

*... because the code we run is in multiple repos, this needs to be a repo*

note: we will be moving to `compile-dev@100.87.99.101` instead of root

- currently stagehand and hf papers scraping is on compile-dev, the rest is on root

## documentation

if you want to add a new activity to the workflow, you need to update the worker and schedule:

- you can list the existing workers running by doing `ps aux | grep worker` (assuming it is still called worker.py)
- you can then kill the existing ones through: `pkill -SIGTERM -f "python worker.py"` to kill all, or `kill -SIGTERM <pid>` for specific
- finally, schedule the new one through: `nohup python worker.py >> logs/worker.log 2>&1 &`
- you can delete the old schedule with `temporal schedule delete -s daily-article-gen-workflow-v2`
- then, recreate the new schedule with `python scheduler.py`

to view the UI on local you can run this: `ssh -N -L localhost:8080:localhost:8080 root@100.87.99.101`, and then open localhost:8080 on your computer

if you want to re-trigger it (because it failed and needs to be re-run), you can terminate it in the UI and then use `temporal schedule trigger --schedule-id daily-article-gen-workflow` (assuming that id is correct) in the CLI

to execute an already existing workflow use `temporal workflow execute --workflow-id article-gen-instance-2025-07-25T09:00:00Z --type ArticleGenWorkflow --task-queue default` in the CLI where the workflow id is the workflow id of the already scheduled run

if you need to re-start temporal: `cd ~/docker-compose`, then `docker compose down` to kill it, then `docker-compose up -d` to restart detached. this will run `docker-compose.yml` (I think)
