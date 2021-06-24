from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return '<h1>Success!<h1>'
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()