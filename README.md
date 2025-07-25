## tempo <-> compile scheduling engine

*... this is where we replace all the cron stuff*

*... because the code we run is in multiple repos, this needs to be a repo*

## documentation

if you want to add a new activity to the workflow, you need to update the worker:

- you can list the existing workers running by doing `ps aux | grep worker` (assuming it is still called worker.py)
- you can then kill the existing ones through: `pkill -SIGTERM -f "python worker.py"`
- finally, schedule the new one through: `nohup python worker.py >> logs/worker.log 2>&1 &`

to view the UI on local you can run this: `ssh -N -L localhost:8080:localhost:8080 root@100.87.99.101`, and then open localhost:8080 on your computer

if you want to re-trigger it (because it failed and needs to be re-run), you can terminate it in the UI and then use `temporal schedule trigger --schedule-id daily-article-gen-workflow` (assuming that id is correct) in the CLI

to execute an already existing workflow use `temporal workflow execute --workflow-id article-gen-instance-2025-07-25T09:00:00Z --type ArticleGenWorkflow --task-queue default` in the CLI where the workflow id is the workflow id of the already scheduled run

if you need to re-start the whole server, you have to run the `docker-compose.yml` file at `~/docker-compose/docker-compose.yml` with `docker compose up`

## misc info

stagehand uses playwright which launches a headless browser. this freaks out if you attempt to run as root. because of this, there's a service in `docker-compose.yml` called `article-worker` (I know... bad name lol). `article-worker` spins up a docker container that demotes itself and run the worker for stagehand (to make this all work). 
