import requests
import json

def send_slack_message(webhook_url, message: str) -> None:
    slack_data = {'text': message}

    response = requests.post(
        webhook_url,
        data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(f'Request to Slack returned an error {response.status_code}, the response is:\n{response.text}')

webhook_url = 'https://hooks.slack.com/services/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'
message = 'Xin chào! Đây là một tin nhắn từ Python bot của bạn.'

send_slack_message(webhook_url, message)