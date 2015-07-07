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
import json
import yaml

class telegbot:
    def __init__(self, token):
        self.token = token
        self.config = yaml.load(open("config.yml", 'r'))
        self.data = self.getBotData()
        self.on_receive_message = self.void_callback
        self.on_new_chat_participant = self.void_callback
        self.on_left_chat_participant = self.void_callback
        self.on_receive_audio = self.void_callback
        self.on_receive_document = self.void_callback
        self.on_receive_photo = self.void_callback
        self.on_receive_sticker = self.void_callback
        self.on_receive_video = self.void_callback
        self.on_receive_contact = self.void_callback
        self.on_receive_location = self.void_callback
        self.on_new_chat_title = self.void_callback
        self.on_new_chat_photo = self.void_callback
        self.on_delete_chat_photo = self.void_callback
        self.on_group_chat_created = self.void_callback

        self.quit = False
        print(self.data)

    def void_callback(self, data={}):
        return

    def apiRequest(self, method, parameters = {}, files=None):
        if not self.methodExists(method):
            return False
        url = self.config["telegramBotApi"]["api_url"]
        url = url.replace('{token}', self.getBotToken())
        url = url.replace('{method}', method)
        values = self.manageParameters(method, parameters, files)
        if values is None:
            return False

        http_method = self.config["telegramBotApi"]["methods"][method]['action']
        result = requests.request(http_method, url, params=parameters, files=files).json()
        print(result)

        if not result["ok"]:
            return None
        return result["result"]

    def manageParameters(self, method, parameters, files):
        managedParams = {}
        if not self.methodExists(method):
            return None
        if self.config["telegramBotApi"]["methods"][method]["parameters"] is None:
            return managedParams
        for methodParameter in self.config["telegramBotApi"]["methods"][method]["parameters"]:
            methodParameterData = self.config["telegramBotApi"]["methods"][method]["parameters"][methodParameter]
            if methodParameter in parameters:
                if (parameters[methodParameter] is None and not methodParameterData["required"]):
                    continue
                if not (methodParameterData["type"] == type(parameters[methodParameter]).__name__):
                    return None
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
                    return None
        return managedParams

    def methodExists(self, method):
        return method in self.config["telegramBotApi"]["methods"]

    def getBotToken(self):
        return self.token

    def getBotUsername(self):
        return self.data["username"]

    def getBotData(self):
        botData = self.apiRequest('getMe')
        if botData is None:
            return False
        return botData

    def sendMessage(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
        response = self.apiRequest('sendMessage', {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": disable_web_page_preview,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        })
        self.runEvent(response)

    def sendChatAction(self, chat_id, action):
        response = self.apiRequest('sendChatAction', {
            "chat_id": chat_id,
            "action": action
        })

    def sendImage(self, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None):
        response = self.apiRequest('sendPhoto', {
            "chat_id": chat_id,
            "caption": caption,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        }, files = {"photo": photo})
        self.runEvent(response)




    def runEvent(self, event):
        if "text" in event:
            self.on_receive_message(event)
        elif "new_chat_participant" in event:
            self.on_new_chat_participant(event)
        elif "left_chat_participant" in event:
            self.on_left_chat_participant(event)
        elif "audio" in event:
            self.on_receive_audio(event)
        elif "document" in event:
            self.on_receive_document(event)
        elif "photo" in event:
            self.on_receive_photo(event)
        elif "sticker" in event:
            self.on_receive_sticker(event)
        elif "video" in event:
            self.on_receive_video(event)
        elif "contact" in event:
            self.on_receive_contact(event)
        elif "location" in event:
            self.on_receive_location(event)
        elif "new_chat_title" in event:
            self.on_new_chat_title(event)
        elif "new_chat_photo" in event:
            self.on_new_chat_photo(event)
        elif "delete_chat_photo" in event:
            self.on_delete_chat_photo(event)
        elif "group_chat_created" in event:
            self.on_group_chat_created(event)
        else:
            print(response)

    def run(self):
        lastMessage_update_id = 0
        while (not self.quit):
            response = self.apiRequest('getUpdates', {
                "offset": lastMessage_update_id + 1,
                "limit": 100,
                "timeout": 20
            })
            for update in response:
                if update["update_id"] > lastMessage_update_id:
                    lastMessage_update_id = update["update_id"]
                self.runEvent(update["message"])

