from flask import Flask, request, abort
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print('hello2')
        data = request.json
        param = {"sid" : data["sid"],
        "search_name" : data["search_name"],
        "owner" : data["owner"],
        "results_link" : data["results_link"],
        "result" : data["result"]}
        webhook_url = "https://hooks.slack.com/services/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"
        # r = requests.post(webhook_url, data = {"text":param["owner"]}, headers={'Content-Type': 'application/json'})  # Sending data using Post() request as webhook
        print(param)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
