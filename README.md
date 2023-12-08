# Quick Date Poll Bot

## How to get a Discord bot account

Follow the tutorial of discordpy to create a discord application with a bot
account: [Creating a Bot Account}(https://discordpy.readthedocs.io/en/stable/discord.html#creating-a-bot-account)

Export the discord token in the `QDPB_TOKEN` environment variable.

## How to run the bot locally

1. Install Python (at least 3.9)
2. Install the requirements in `requirements.txt` via `pip install -r requirements.txt`. 
   Note: You might want to do this in a [virtual environment](https://docs.python.org/3/tutorial/venv.html).
3. Run `bot.py` with Python, e.g. via `python bot.py` or `python3 bot.py`.

## How to run the bot via Docker

1. Install Docker
2. Run `docker image build -t qdpb .` (including the dot `.`)
3. Run the docker image via `docker run qdpb`. You might want to add
   `--restart always` for the container to automatically restart.
