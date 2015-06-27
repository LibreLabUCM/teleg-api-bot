# teleg-api-bot
Telegram Api for new bot system

Dependencies: py-yaml


"main.py" is the main file to run. It is an example of a bot.

Example bot:

```python

#!/usr/bin/python
from telegbot import telegbot
from logger import logger
logger = logger()
import time,json

def receive_message(msg):
    if msg["date"] < time.time() - 2:
        return # old
    logger.msg(msg)
    if msg["text"] == "/help":
        bot.sendMessage(msg["chat"]["id"], "Text")


bot = telegbot()
bot.on_receive_message = receive_message
bot.run()

```

