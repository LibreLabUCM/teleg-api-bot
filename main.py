#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   main.py                                                                    #
#                                                                              #
#   Example bot to test teleg-api-bot.                                         #
#                                                                              #
#                                                                              #
#                                                                              #
#   Copyright (C) 2015 LibreLabUCM All Rights Reserved.                        #
#                                                                              #
#   This file is part of teleg-api-bot.                                        #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU General Public License as published by       #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                              #
################################################################################


from telegbot import telegbot
from logger import logger
logger = logger()
import time,json

def receive_message(msg):
    if msg["date"] < time.time() - 2:
        return # old
    logger.msg(msg)
    if msg["text"] == "/help" or msg["text"] == "/help@" + bot.getBotUsername():
        keyboard = {"keyboard":[["/help"], ["/quit"], ["/test keyboard"]]}
        bot.sendMessage(msg["chat"]["id"], "Commands: (in custom keyboard)", reply_markup=json.dumps(keyboard))
    if msg["text"] == "/quit" or msg["text"] == "/quit@" + bot.getBotUsername():
        if msg["from"]["id"] == 43804645:
            bot.sendMessage(msg["chat"]["id"], "Bye!")
            bot.quit = True
        else:
            bot.sendMessage(msg["chat"]["id"], "You don't have permission!")
    if msg["text"] == "/test keyboard":
        keyboard = {"keyboard":[["1⃣","2⃣","3⃣","4⃣","5⃣","6⃣","7⃣","8⃣","9⃣","0⃣", "XD"],["q","w","e","r","t","y","u","i","o","p"],["/help", "/quit", "/test keyboard"]]}
        bot.sendMessage(msg["chat"]["id"], "Sending custom keyboard!", reply_markup=json.dumps(keyboard))

def new_chat_participant(msg):
    print("Welcome @" + msg["new_chat_participant"]["username"] + " to " + msg["chat"]["title"])


def left_chat_participant(msg):
    logger.msg(msg)

def receive_audio(msg):
    logger.msg(msg)

def receive_document(msg):
    logger.msg(msg)

def receive_photo(msg):
    logger.msg(msg)

def receive_sticker(msg):
    logger.msg(msg)

def receive_video(msg):
    logger.msg(msg)

def receive_contact(msg):
    logger.msg(msg)

def receive_location(msg):
    logger.msg(msg)

def new_chat_title(msg):
    logger.msg(msg)

def new_chat_photo(msg):
    logger.msg(msg)

def delete_chat_photo(msg):
    logger.msg(msg)

def group_chat_created(msg):
    logger.msg(msg)



bot = telegbot('92725317:AAHH8KRReReE_gKVzwHwrki7gvAXBGM__0Q')

bot.on_receive_message = receive_message
bot.on_new_chat_participant = new_chat_participant
bot.on_left_chat_participant = left_chat_participant
bot.on_receive_audio = receive_audio
bot.on_receive_document = receive_document
bot.on_receive_photo = receive_photo
bot.on_receive_sticker = receive_sticker
bot.on_receive_video = receive_video
bot.on_receive_contact = receive_contact
bot.on_receive_location = receive_location
bot.on_new_chat_title = new_chat_title
bot.on_new_chat_photo = new_chat_photo
bot.on_delete_chat_photo = delete_chat_photo
bot.on_group_chat_created = group_chat_created

bot.run()