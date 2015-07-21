# teleg-api-bot

Telegram Api for new bot system

## Getting started

This project uses Python 3, so you should probably install that, if you haven't already.

You should probably take a look at our [Getting Started](https://github.com/LibreLabUCM/teleg-api-bot/wiki/Getting-started-with-the-Telegram-Bot-API) wiki page.

## Usage

Dependencies: Python 3.4, py-yaml

"main.py" is the main file to run. It is an example of a bot.

Example bot:

```python

#!/usr/bin/env python3
from telegbot import telegbot
from logger import Logger
logger = Logger()
import time,json

def receive_message(msg):
    if msg["date"] < time.time() - 2:
        return # old
    logger.msg(msg)
    if msg["text"] == "/help":
        bot.send_message(msg["chat"]["id"], "Text")


bot = telegbot('TOKEN')
bot.on_receive_message = receive_message
bot.run()

```

