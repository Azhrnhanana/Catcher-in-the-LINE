from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

import configparser

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(OsH7XLAEZ4QPNlLlcjsQeegLJigfbU9mHUqBRL30TiOc2CJWpcfMiSDyYLG8CrKOJ6ik9lBwS14CWZjCKnytkw7gkFbpzxqDNtQvjYTxRMLJDfEyddXDQYYB1YDWYB1YDQY1DQY1Y1DWYB1QY1DW1B1D9DQY1DQ1Y1E0DQY1Y1D0Y1B1D0Y1B1B1B1B)

handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
