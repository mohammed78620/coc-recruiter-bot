# Clash of Clans Discord Bot

This repository contains Python scripts for a Discord bot tailored for Clash of Clans recruitment purposes. The bot is designed to extract relevant user information from Discord messages, filter messages based on timestamps, and interact with users through direct messages.

## Dependencies

Ensure you have Python installed on your system. This project requires the following dependencies managed via Poetry:

- `requests`: for making HTTP requests to the Discord API.
- `python-dotenv`: for loading environment variables from a `.env` file.
- `poetry`: for managing Python dependencies.

You can install Poetry using the following command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Once Poetry is installed, navigate to the project directory and run:

```bash
poetry install
```

## Installation
Create a .env file in the root directory of the project and set the following environment variables:

```bash
DISCORD_TOKEN=<your_discord_token>
CLAN_TAG=<your_clan_tag>
```

## Running script

run the following command
```bash
poetry run python coc_recruiter_bot/main.py
```