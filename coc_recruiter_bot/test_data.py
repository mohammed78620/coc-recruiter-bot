from coc_recruiter_bot.schema.clash_user import ClashUser

mock_data = [
    {
        "id": "1222696561163632752",
        "type": 20,
        "content": "",
        "channel_id": "1058589660798013440",
        "author": {
            "id": "1058585810355622048",
            "username": "Clan Castle",
            "avatar": "60deab35c23c1d22eb8869875c60ecb9",
            "discriminator": "6971",
            "public_flags": 0,
            "premium_type": 0,
            "flags": 0,
            "bot": True,
            "banner": None,
            "accent_color": None,
            "global_name": None,
            "avatar_decoration_data": None,
            "banner_color": None,
        },
        "attachments": [],
        "embeds": [
            {
                "type": "rich",
                "title": "juanito5152 is looking for a clan!",
                "description": "**Discord ID:** <@755584227113697291>",
                "color": 3458795,
                "timestamp": "2024-03-27T23:59:36.711000+00:00",
                "fields": [
                    {
                        "name": "Player tag",
                        "value": "[#QPCRY9CUJ](url)",
                        "inline": True,
                    },
                    {
                        "name": "Townhall level",
                        "value": "<:th12:451408476426469387> 12",
                        "inline": True,
                    },
                    {
                        "name": "Hero levels",
                        "value": "<:BK:288380851111329792>",
                        "inline": True,
                    },
                    {
                        "name": "Description",
                        "value": "looking for active clan",
                        "inline": False,
                    },
                ],
                "thumbnail": {
                    "url": "https://api-assets.clashofclans",
                    "proxy_url": "https://images-ext-1.discordapp.net/external",
                    "width": 288,
                    "height": 288,
                },
                "content_scan_version": 1,
            }
        ],
        "mentions": [],
        "mention_roles": [],
        "pinned": False,
        "mention_everyone": False,
        "tts": False,
        "timestamp": "2024-03-27T23:59:36.785000+00:00",
        "edited_timestamp": None,
        "flags": 0,
        "components": [],
        "application_id": "1058585810355622048",
        "interaction": {
            "id": "1222696434214637629",
            "type": 2,
            "name": "post",
            "user": {
                "id": "755584227113697291",
                "username": "juanito5152",
                "avatar": "095ba76eba4e5feea207c75996a62957",
                "discriminator": "0",
                "public_flags": 0,
                "premium_type": 0,
                "flags": 0,
                "banner": None,
                "accent_color": None,
                "global_name": "juanito",
                "avatar_decoration_data": None,
                "banner_color": None,
            },
        },
        "webhook_id": "1058585810355622048",
        "position": 0,
        "interaction_metadata": {
            "id": "1222696559469400155",
            "type": 5,
            "user_id": "755584227113697291",
            "authorizing_integration_owners": {
                "0": "236523452230533121",
                "1": "755584227113697291",
            },
            "triggering_interaction_metadata": {
                "id": "1222696434214637629",
                "type": 2,
                "user_id": "755584227113697291",
                "authorizing_integration_owners": {
                    "0": "236523452230533121",
                    "1": "755584227113697291",
                },
                "name": "post",
            },
        },
    },
    {
        "timestamp": "2024-03-28T23:59:36.785000+00:00",
        "embeds": [
            {
                "type": "rich",
                "title": "juanito5152 is looking for a clan!",
                "description": "**Discord ID:** <@755584227113697291>",
                "color": 3458795,
                "timestamp": "2024-03-27T23:59:36.711000+00:00",
                "fields": [
                    {
                        "name": "Player tag",
                        "value": "[#QPCRY9CUJ](https://link.clashofclans.com)",
                        "inline": True,
                    },
                    {
                        "name": "Townhall level",
                        "value": "<:th12:451408476426469387> 14",
                        "inline": True,
                    },
                    {
                        "name": "Hero levels",
                        "value": "<:BK:288380851111329792>56",
                        "inline": True,
                    },
                    {
                        "name": "Description",
                        "value": "looking for active clan",
                        "inline": False,
                    },
                ],
                "thumbnail": {
                    "url": "https://api-assets.clashofclans.com/",
                    "proxy_url": "https://images-ext-1.discordapp.net/external/",
                    "width": 288,
                    "height": 288,
                },
                "content_scan_version": 1,
            }
        ],
        "interaction": {
            "id": "1222696434214637629",
            "type": 2,
            "name": "post",
            "user": {
                "id": "5",
                "username": "ak",
                "avatar": "095ba76eba4e5feea207c75996a62957",
                "discriminator": "0",
                "public_flags": 0,
                "premium_type": 0,
                "flags": 0,
                "banner": None,
                "accent_color": None,
                "global_name": "juanito",
                "avatar_decoration_data": None,
                "banner_color": None,
            },
        },
    },
    # {"timestamp": "2024-03-29T23:59:36.785000+00:00"},
]


clash_user_instance_1 = ClashUser(
    id="660862690411151361", username=".gameitup", townhall_level=12, player_tag="#QRURPV2RC"
)
