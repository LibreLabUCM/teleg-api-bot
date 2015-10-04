# teleg-api-bot

Telegram Api for new bot system

## Getting started

This project uses Python 3, so you should probably install that, if you haven't already.

For an introduction to the Telegram Bot API, take a look at our [Getting Started](https://github.com/LibreLabUCM/teleg-api-bot/wiki/Getting-started-with-the-Telegram-Bot-API) wiki page.

## Installation

You can get it from pip:

```
$ pip install teleg-api-bot
```

Or you can go ahead and clone this repo, and install it:

```
$ python setup.py install
```

## Usage

Dependencies: Python 3.4, py-yaml, requests (see [requirements-dev](./requirements-dev.txt))

Example bot:

```python
#!/usr/bin/env python3

from telegapi.telegbot import TelegBot
from telegapi.logger import Logger

logger = Logger()
import time, json

def receive_message(msg):
    logger.msg(msg)
    if msg["text"] == "/help":
        bot.send_message(msg["chat"]["id"], "Text")


bot = TelegBot('TOKEN')
bot.on_receive_message = receive_message
bot.connect()
bot.run()
```
