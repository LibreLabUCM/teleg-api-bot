#!/usr/bin/python
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
from logger import logger
import yaml

logger = logger()

LONG_POLLING_TIMEOUT=20
REQUEST_TIMEOUT=40    # must be greater than LONG_POLLING_TIMEOUT

class telegbot:
    def __init__(self, token):
        self.token = token
        self.config = yaml.load(open("config.yml", 'r'))
        self.data = self.__getBotData()

        if self.data is None:
            logger.log(logger.error, "Cannot get bot data, maybe a bad token")
            self.quit = True
            return      # Cannot get bot data, maybe a bad token
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

        self.quit = False
        print(self.data)

    def getBotToken(self):
        return self.token

    def getBotUsername(self):
        return self.data["username"]

    def run(self):
        lastMessage_update_id = 0
        while (not self.quit):
            response = self.__apiRequest('getUpdates', {
                "offset": lastMessage_update_id + 1,
                "limit": 100,
                "timeout": LONG_POLLING_TIMEOUT
            })
            for update in response:
                if update["update_id"] > lastMessage_update_id:
                    lastMessage_update_id = update["update_id"]
                self.__runEvent(update["message"])

    def sendMessage(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
        response = self.__apiRequest('sendMessage', {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": disable_web_page_preview,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        })
        self.__runEvent(response)

    def sendChatAction(self, chat_id, action):
        response = self.__apiRequest('sendChatAction', {
            "chat_id": chat_id,
            "action": action
        })

    def sendImage(self, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None):
        response = self.__apiRequest('sendPhoto', {
            "chat_id": chat_id,
            "caption": caption,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        }, files = {"photo": photo})
        self.__runEvent(response)


    def __void_callback(self, data={}):
        return

    def __apiRequest(self, method, parameters = {}, files=None):
        values = self.__manageParameters(method, parameters, files)
        if values is None:
            return None   # Param error or non-existent method

        url = self.config["telegramBotApi"]["api_url"]
        url = url.replace('{token}', self.getBotToken())
        url = url.replace('{method}', method)

        http_method = self.config["telegramBotApi"]["methods"][method]['action']
        
        try:
            result = requests.request(http_method, url, timeout=REQUEST_TIMEOUT, params=values, files=files)
        except requests.exceptions.RequestException as e:
            logger.log(logger.error, "Exception in requests")
            return None

        logger.log(logger.debug,result.url)
        logger.log(logger.debug,result.text)

        if not (result.status_code is requests.codes.ok):
            return None   # Server reported error
        
        result = result.json()

        if not result["ok"]:
            return None   # Telegram API reported error
        
        return result["result"]

    def __manageParameters(self, method, parameters, files):
        managedParams = {}
        if not self.__methodExists(method):
            logger.log(logger.debug, "call to non-existent method")
            return None   # non-existent method
        if self.config["telegramBotApi"]["methods"][method]["parameters"] is None:
            return managedParams
        for methodParameter in self.config["telegramBotApi"]["methods"][method]["parameters"]:
            methodParameterData = self.config["telegramBotApi"]["methods"][method]["parameters"][methodParameter]
            if methodParameter in parameters:
                if (parameters[methodParameter] is None and not methodParameterData["required"]):
                    continue
                if not (methodParameterData["type"] == type(parameters[methodParameter]).__name__):
                    logger.log(logger.debug, "Incorrect type in param")
                    return None   # incorrect type in param
                managedParams[methodParameterData["parameter"]] = parameters[methodParameter]
            #TODO: Find a better way to do this instead of having the code duplicated
            elif methodParameter in files:
                if (files[methodParameter] is None and not methodParameterData["required"]):
                    continue
                #if not (methodParameterData["type"] == type(files[methodParameter]).__name__):
                #    return None
                managedParams[methodParameterData["parameter"]] = files[methodParameter]
            else:
                if methodParameter["required"]:
                    logger.log(logger.debug, "Non-existent required param")
                    return None   # non-existent required param
        return managedParams

    def __methodExists(self, method):
        return method in self.config["telegramBotApi"]["methods"]

    def __getBotData(self):
        botData = self.__apiRequest('getMe')
        if botData is None:
            return None
        return botData

    def __runEvent(self, event):
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

