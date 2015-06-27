#!/usr/bin/python
from TC import TC as TC # And TC again
from time import gmtime, strftime
import utils
import json

class logger:
    info        = {'logLevel':1, 'colorCode':TC.ICyan,  'prefix':" INFO " }
    out         = {'logLevel':2, 'colorCode':TC.IWhite, 'prefix':""       }
    debug       = {'logLevel':3, 'colorCode':TC.IBlue,  'prefix':" DEBUG" }
    warn        = {'logLevel':4, 'colorCode':TC.IYellow,'prefix':" WARN " }
    error       = {'logLevel':5, 'colorCode':TC.Red,    'prefix':" ERROR" }
  
    def log(self, logType, text):
        if logType["logLevel"] < self.info["logLevel"] or logType["logLevel"] > self.error["logLevel"]:
            self.log(self.error, "First parameter of \"logger.log\" is incorrect!")
            return false
        text = text.replace(TC.Rst, TC.Rst+TC.IWhite)
        prefix = ""
        if logType["prefix"] != "":
            prefix = TC.IWhite+"["+logType["colorCode"]+logType["prefix"]+TC.IWhite+"] "
        currentTime = "["+strftime("%H:%M", gmtime())+"]"
        printText = TC.IWhite+currentTime+prefix+text+TC.Rst
        plainText = currentTime+"["+logType["prefix"]+"] "+text
        print(printText)
        # print(plainText)
        return
  
    def msg(self, msg):
        #return
        output = ""
        temp = ""
        msgDirection = "?"
        if "username" in msg["chat"]:
            output = output + TC.ICyan + msg["chat"]["username"]
        elif "title" in msg["chat"]:
            output = output + TC.Cyan + msg["chat"]["title"]
        elif "id" in msg["chat"]:
            output = output + TC.Cyan + msg["chat"]["id"]
        else:
            self.log(self.error, "msg[\"chat\"] doesn't have 'username', 'title', or 'id'. msg -> " + json.dump(msg))
        
        output = output + TC.IGreen + " <<< " + TC.ICyan + msg["from"]["username"] + TC.Rst+TC.Rst+": "
        
        # if not syncFinished:
            # output = output+"("+"old"+") "
        if "fwd_src" in msg:
            output = output+TC.IPurple+"[fwd "+TC.ICyan+msg["fwd_src"]["username"]+TC.IPurple+"]"+TC.Rst
        if "reply" in msg:
            output = output+TC.IPurple+"[reply "+TC.ICyan+str(msg["reply"]["from"]["username"])+TC.Rst+": "+TC.Yellow+utils.msgGetSummary(msg["reply"], 10)+TC.IPurple+"]"+TC.Rst
        if "reply_id" in msg:
            output = output+TC.IPurple+"[reply "+TC.ICyan+str(msg["reply_id"])+TC.IPurple+"]"+TC.Rst
        output = output+TC.IYellow+utils.msgGetSummary(msg, 0)+TC.Rst
        output = output.replace('\n', ' ').replace('\r', '')
        self.log(self.info, output)
        return
    
