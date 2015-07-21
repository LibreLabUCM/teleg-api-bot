#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   telegbot.py                                                                #
#                                                                              #
#   Main teleg-api-bot class, it represents a bot.                             #
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

import requests
import yaml
from pkg_resources import resource_stream

from telegapi.exceptions import ConnectionFailedException as ConnectionFailedException
from telegapi.exceptions import BadServerResponseException as BadServerResponseException
from telegapi.exceptions import BadTelegAPIResponseException as BadTelegAPIResponseException
from telegapi.exceptions import BadParamException as BadParamException
from telegapi.exceptions import InvalidAPICallException as InvalidAPICallException

from telegapi.logger import logger

logger = logger()

LONG_POLLING_TIMEOUT = 20
REQUEST_TIMEOUT = 40  # must be greater than LONG_POLLING_TIMEOUT


class telegbot:
    def __init__(self, token):
        self.token = token
        self.config = yaml.load(resource_stream(__name__, "config.yml"))

        self.on_receive_message = self.__void_callback
        self.on_new_chat_participant = self.__void_callback
        self.on_left_chat_participant = self.__void_callback
        self.on_receive_audio = self.__void_callback
        self.on_receive_document = self.__void_callback
        self.on_receive_photo = self.__void_callback
        self.on_receive_sticker = self.__void_callback
        self.on_receive_video = self.__void_callback
        self.on_receive_contact = self.__void_callback
        self.on_receive_location = self.__void_callback
        self.on_new_chat_title = self.__void_callback
        self.on_new_chat_photo = self.__void_callback
        self.on_delete_chat_photo = self.__void_callback
        self.on_group_chat_created = self.__void_callback
        self.quit = True

    def connect(self):
        self.data = self.__api_request('getMe')
        self.quit = False

    def get_bot_token(self):
        return self.token

    def get_bot_username(self):
        return self.data["username"]

    def run(self):
        last_message_update_id = 0
        while not self.quit:
            response = self.__api_request('getUpdates', {
                "offset": last_message_update_id + 1,
                "limit": 100,
                "timeout": LONG_POLLING_TIMEOUT
            })
            for update in response:
                if update["update_id"] > last_message_update_id:
                    last_message_update_id = update["update_id"]
                self.__run_event(update["message"])

    def send_message(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
        response = self.__api_request('send_message', {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": disable_web_page_preview,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        })
        self.__run_event(response)

    def sen_chat_action(self, chat_id, action):
        response = self.__api_request('send_chat_action', {
            "chat_id": chat_id,
            "action": action
        })

    def send_image(self, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None):
        response = self.__api_request('sendPhoto', {
            "chat_id": chat_id,
            "caption": caption,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        }, files={"photo": photo})
        self.__run_event(response)

    def __void_callback(self, data={}):
        return

    def __api_request(self, method, parameters={}, files=None):
        url = self.config["telegramBotApi"]["api_url"].format(token=self.get_bot_token(), method=method)

        http_method = self.config["telegramBotApi"]["methods"][method]['action']

        try:
            result = requests.request(http_method, url, timeout=REQUEST_TIMEOUT, params=parameters, files=files)
        except requests.exceptions.RequestException as e:
            logger.log(logger.error, "Exception in requests")
            raise ConnectionFailedException(str(e))

        logger.log(logger.debug, result.url)
        logger.log(logger.debug, result.text)

        if not (result.status_code is requests.codes.ok):
            raise BadServerResponseException("Bad HTTP status code", result.status_code)  # Server reported error

        result = result.json()

        if not result["ok"]:
            raise BadtelegAPIResponseException("Telegram API sent a non OK response")  # Telegram API reported error

        return result["result"]

    def __method_exists(self, method):
        return method in self.config["telegramBotApi"]["methods"]

    def __run_event(self, event):
        if "text" in event:
            self.on_receive_message(event)
        if "new_chat_participant" in event:
            self.on_new_chat_participant(event)
        if "left_chat_participant" in event:
            self.on_left_chat_participant(event)
        if "audio" in event:
            self.on_receive_audio(event)
        if "document" in event:
            self.on_receive_document(event)
        if "photo" in event:
            self.on_receive_photo(event)
        if "sticker" in event:
            self.on_receive_sticker(event)
        if "video" in event:
            self.on_receive_video(event)
        if "contact" in event:
            self.on_receive_contact(event)
        if "location" in event:
            self.on_receive_location(event)
        if "new_chat_title" in event:
            self.on_new_chat_title(event)
        if "new_chat_photo" in event:
            self.on_new_chat_photo(event)
        if "delete_chat_photo" in event:
            self.on_delete_chat_photo(event)
        if "group_chat_created" in event:
            self.on_group_chat_created(event)
