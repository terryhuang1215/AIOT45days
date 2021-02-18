from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage

import configparser


app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
#print("channel_token:" + config.get('line-bot', 'channel_token'))
#print("channel_secret:" + config.get('line-bot', 'channel_secret'))
line_bot_api = LineBotApi(config.get('line-bot', 'channel_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

@app.route("/")
def main():
    return "Terry Chat Bot Test!!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event message:" + event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
