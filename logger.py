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
  