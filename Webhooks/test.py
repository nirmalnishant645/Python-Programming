from flask import Flask, request, abort
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = {
        "blocks": [
        {
        "type": "section",
        "text": {
        "type": "plain_text",
        "text": "Alwin",
        "emoji": True
        }
        },
        {
        "type": "section",
        "text": {
        "type": "plain_text",
        "text": "Search id is 123456",
        "emoji": True
        }
        },
        {
        "type": "section",
        "text": {
        "type": "plain_text",
        "text": "found vulnerablities in system performence",
        "emoji": True
        }
        }
        ]
        }
        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
        webhook_url = "https://hooks.slack.com/services/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"
        response = requests.request("POST", webhook_url, data=json.dumps(data), headers=headers)
        print("result:- ", response.text)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()