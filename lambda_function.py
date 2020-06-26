from slack import RTMClient
import os
import time
import boto3

token = os.environ.get('SLACKBOT_MYSHIP_TOKEN')
client = RTMClient(token=slack_token)

link = '<https://myShipPicture>'

if client.rtm_connect():
    while True:
        events = client.rtm_read()
        for event in events:
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']
                if 'ship' in text.lower() and link not in text:
                    client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=link,
                        as_user='true:'
                    )
                elif 'cheap' in text.lower() and link not in text:
                    client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=link,
                        as_user='true:'
                    )
                elif 'sheep' in text.lower() and link not in text:
                    client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=link,
                        as_user='true:'
                    )
        time.sleep(1)
else:
    print('Connection failed, invalid token?')
