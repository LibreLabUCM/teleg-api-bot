#!/usr/bin/env python3
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


from telegapi.telegbot import telegbot
from telegapi.logger import Logger

logger = Logger()
import time, json
import requests
from lxml import html
import os
import random


def receive_message(msg):
    if msg["date"] < time.time() - 2:
        return  # old
    logger.msg(msg)

    if msg["text"] == "/help" or msg["text"] == "/help@" + bot.get_bot_username():
        options = {"keyboard": [["/help"], ["/quit"], ["/test keyboard"], ["/mqm"]]}
        bot.send_message(msg["chat"]["id"], "Commands: (in custom keyboard)", reply_markup=json.dumps(options))

    elif msg["text"] == "/quit" or msg["text"] == "/quit@" + bot.get_bot_username():
        bot.send_message(msg["chat"]["id"], "Bye!")
        bot.quit = True

    elif msg["text"] == "/test keyboard":
        keyboard = {"keyboard": [["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "0⃣", "XD"],
                                 ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                                 ["/help", "/quit", "/test keyboard"]]}
        bot.send_message(msg["chat"]["id"], "Sending custom keyboard!", reply_markup=json.dumps(keyboard))

    elif msg["text"] == "/mqm":
        img_classes = None
        for i in range(1, 4500):
            request = requests.get('http://www.mequeme.com/page/' + str(i))
            tree = html.fromstring(request.content)
            img_classes = tree.xpath("//div[@class='media']//img")
            if len(img_classes) != 0:
                break
        img_class = img_classes[0]
        # Debug print (html.etree.tostring(img_class, pretty_print=True))
        img_url = img_class.attrib['src']
        # Not the best way to do this but...
        caption = img_class.attrib['alt']

        logger.log(logger.debug, caption)
        response = requests.get(img_url)
        f = open("sample.gif", 'wb')
        f.write(response.content)
        f.close()
        img = open('sample.gif', 'rb')
        bot.send_chat_action(msg["chat"]["id"], 'upload_photo')
        bot.send_image(msg["chat"]["id"], img, caption=caption)
        img.close()
        os.remove('sample.gif')

    elif msg["text"] == "/mqm random":
        img_classes = None
        while True:
            rand = random.randint(0, 4500)
            request = requests.get('http://www.mequeme.com/page/' + str(rand))
            tree = html.fromstring(request.content)
            img_classes = tree.xpath("//div[@class='media']//img")
            if len(img_classes) != 0:
                break
        img_class = img_classes[random.randint(0, len(img_classes) - 1)]
        # Debug print (html.etree.tostring(img_class, pretty_print=True))
        img_url = img_class.attrib['src']
        # Not the best way to do this but...
        caption = img_class.attrib['alt']

        print(caption)
        response = requests.get(img_url)
        f = open("sample.gif", 'wb')
        f.write(response.content)
        f.close()
        img = open('sample.gif', 'rb')
        bot.send_chat_action(msg["chat"]["id"], 'upload_photo')
        bot.send_image(msg["chat"]["id"], img, caption=caption)
        img.close()
        os.remove('sample.gif')


def new_chat_participant(msg):
    print("Welcome @" + msg["new_chat_participant"]["first_name"] + " to " + msg["chat"]["title"])


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


bot = telegbot('TOKEN')
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

try:
    bot.connect()
except Exception as e:
    logger.log(logger.error, str(e))

bot.run()
