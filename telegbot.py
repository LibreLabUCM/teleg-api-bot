#!/usr/bin/python

import urllib.request
import json
import yaml
import string


class telegbot:
    def __init__(self):
        self.config = yaml.load(open("config.yml", 'r'))
        return
    
    def apiRequest(self, method, parameters = {}):
        if not self.methodExists(method):
            return False
        url = self.config["telegramBotApi"]["api_url"]
        url = url.replace('{token}', self.getBotToken())
        url = url.replace('{method}', method)
        values = parameters
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
    
    
    def sendMessage(self, chat_id)
        return
    