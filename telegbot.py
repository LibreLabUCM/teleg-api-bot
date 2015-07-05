#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import json
import yaml
import string

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
    
    def apiRequest(self, method, parameters = {}):
        if not self.methodExists(method):
            return False
        url = self.config["telegramBotApi"]["api_url"]
        url = url.replace('{token}', self.getBotToken())
        url = url.replace('{method}', method)
        values = self.manageParameters(method, parameters)
        if values == None:
            return False
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
        return False
    
    def manageParameters(self, method, parameters):
        managedParams = {}
        if not self.methodExists(method):
            return False
        if self.config["telegramBotApi"]["methods"][method]["parameters"] == None:
            return managedParams
        for methodParameter in self.config["telegramBotApi"]["methods"][method]["parameters"]:
            methodParameterData = self.config["telegramBotApi"]["methods"][method]["parameters"][methodParameter]
            if methodParameter in parameters:
                if (parameters[methodParameter] == None and not methodParameterData["required"]):
                    continue
                if not (methodParameterData["type"] == type(parameters[methodParameter]).__name__):
                    return False
                managedParams[methodParameterData["parameter"]] = parameters[methodParameter]
            else:
                if methodParameter["required"]:
                    return False
        return managedParams
    
    def methodExists(self, method):
        return method in self.config["telegramBotApi"]["methods"]
    
    def getBotToken(self):
        return self.token
    
    def getBotUsername(self):
        return self.data["username"]
    
    def getBotData(self):
        botData = self.apiRequest('getMe')
        if not botData:
            return False
        return botData["result"]
    
    def sendMessage(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
        response = self.apiRequest('sendMessage', {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": disable_web_page_preview,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": reply_markup
        })
        if response["ok"]:
            self.runEvent(response["result"])

    def runEvent(self, event):
        if "text" in event:
            self.on_receive_message(event)
        elif "new_chat_participant" in event:
            self.on_new_chat_participant(event)
        elif "left_chat_participant" in event:
            self.on_left_chat_participant(event)
        elif "audio" in event:
            self.on_receive_audio(event)
        elif "photo" in event:
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
            if response["ok"]:
                for update in response["result"]:
                    if update["update_id"] > lastMessage_update_id:
                        lastMessage_update_id = update["update_id"]
                    self.runEvent(update["message"])
    
