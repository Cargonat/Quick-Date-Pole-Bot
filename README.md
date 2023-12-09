# Quick Date Poll Bot

## How to get a Discord bot account

Follow the tutorial of discordpy to create a discord application with a bot
account: [Creating a Bot Account}(https://discordpy.readthedocs.io/en/stable/discord.html#creating-a-bot-account)

Export the discord token in the `QDPB_TOKEN` environment variable.

## Local development

### Setup

1. Install Python >= 3.11
2. Install [poetry](https://python-poetry.org/) for dependency management
3. Run `poetry install --with dev` to install all dependencies
4. Run `poetry run pre-commit install` to register git pre-commit hooks

### Execution

1. Export the `QDPB_TOKEN` environment variable
2. Run `poetry run bot`

## Docker

You can build the Dockerfile with

```bash
docker build -t qdpb .
```

You can then execute it with

```bash
docker run --rm -it -e QDPB_TOKEN=<token-here> qdpb
```
