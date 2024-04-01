import json
import logging
import time
from datetime import datetime, timedelta, timezone
from typing import List

import requests

from coc_recruiter_bot.constants import COC_CHANNEL_ID, INITIAL_MESSAGE, MAX_NUMBER_OF_MESSAGES, MIN_TOWNHALL_LEVEL
from coc_recruiter_bot.funcs.send_message import create_dm_channel, send_message
from coc_recruiter_bot.schema.clash_user import ClashUser
from coc_recruiter_bot.settings import DISCORD_TOKEN, SEND_MESSAGE


def configure_logging(debug: bool = False):
    if debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    log_file = "logs.log"

    log_formatter = logging.Formatter("%(asctime)s: %(levelname)s: [%(name)s]: %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(log_level)

    app_logger = logging.getLogger("root")
    app_logger.setLevel(log_level)
    app_logger.addHandler(file_handler)
    app_logger.addHandler(stream_handler)


def extract_user_info(messages) -> List[ClashUser]:
    clash_users = []

    for message in messages:
        id = message["interaction"]["user"]["id"]
        username = message["interaction"]["user"]["username"]
        fields = message["embeds"][-1].get("fields", None)

        if not fields:
            continue

        townhall_level = int(fields[1]["value"].split(" ")[-1])
        # player tag is informat "[#QPCRY9CUJ](https://link.clashofclans.com)"
        player_tag = fields[0]["value"].split("]")[0][1:]

        if townhall_level >= MIN_TOWNHALL_LEVEL:
            clash_user = ClashUser(id=id, username=username, townhall_level=townhall_level, player_tag=player_tag)
            clash_users.append(clash_user)

    return clash_users


def filter_timestamps(timestamps: List, days: int):
    # Parse timestamp strings into datetime objects
    timestamps_datetime = [{**ts, "datatime_timestamp": datetime.fromisoformat(ts["timestamp"])} for ts in timestamps]

    # Get the current datetime
    current_datetime = datetime.now()

    # Get the current datetime in UTC timezone
    current_datetime = datetime.now(timezone.utc)

    # Define timedelta for one day
    one_day = timedelta(days=1)

    # Filter timestamps within the last day
    timestamps_within_last_day = [
        ts for ts in timestamps_datetime if current_datetime - ts.pop("datatime_timestamp") <= one_day
    ]

    return timestamps_within_last_day


def recieve_messages(channel_id: int) -> List:
    headers = {"authorization": DISCORD_TOKEN}
    res = requests.get(
        f"https://discord.com/api/v8/channels/{channel_id}/messages",
        headers=headers,
        timeout=10,
    )
    try:
        obj = json.loads(res.text)
    except Exception as e:
        logger.info(e)
        return []

    if len(obj) > MAX_NUMBER_OF_MESSAGES:
        return obj[:MAX_NUMBER_OF_MESSAGES]

    return obj


if __name__ == "__main__":
    configure_logging()
    logger = logging.getLogger()
    messages = recieve_messages(COC_CHANNEL_ID)
    logger.info(f"number of messages recieved: {len(messages)}")
    filtered_messages = filter_timestamps(messages, 1)
    logger.info(f"number of messages after filtering: {len(filtered_messages)}")
    clash_users = extract_user_info(filtered_messages)

    for clash_user in clash_users:
        user_id = clash_user.id

        channel_id = create_dm_channel(DISCORD_TOKEN, user_id)
        time.sleep(10)

        if SEND_MESSAGE:
            send_message(DISCORD_TOKEN, channel_id, INITIAL_MESSAGE)

    logger.info("Bot finished!!")
