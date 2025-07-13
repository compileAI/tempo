## tempo <-> compile scheduling engine

*... this is where we replace all the cron stuff*

*... because the code we run is in multiple repos, this needs to be a repo*

## documentation

- to be honest, I don't really know how the scheduling part of it works (the main scripts - scheduler.py, worker.py)

- I just ran both the files and one threw an error saying it was already working

- I think you can also mess around in the UI or through the CLI and it's easy enough

- if you want to re-trigger it (because it failed and needs to be re-run), you can terminate it in the UI and then use `temporal schedule trigger --schedule-id daily-article-gen-workflow` (assuming that id is correct) in the CLI
