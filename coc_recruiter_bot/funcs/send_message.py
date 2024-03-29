import requests


def send_message(token, channel_id, message):
    url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header, timeout=10)
    print(r.status_code)


def create_dm_channel(token, user_id):
    data = {"recipient_id": user_id}
    headers = {"authorization": token}

    r = requests.post("https://discord.com/api/v9/users/@me/channels", json=data, headers=headers, timeout=10)
    print(r.status_code)

    channel_id = r.json()["id"]

    return channel_id
