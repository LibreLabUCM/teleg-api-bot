#!/usr/bin/python
import urllib.request
import json
import yaml
import string

class telegbot:
    def __init__(self):
        self.config = yaml.load(open("config.yml", 'r'))
        self.data = self.getBotData()
        self.on_receive_message = self.void_callback
        self.on_new_chat_participant = self.void_callback
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
            #the_page = response.read().decode()
            #return json.dumps(json.loads(the_page))
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
    
    def sendMessage(self, chat_id)
        return
    