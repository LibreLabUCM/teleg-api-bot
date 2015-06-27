#!/usr/bin/python

from inspect import getmembers
import pprint
pp = pprint.PrettyPrinter(indent=4)


def msgGetSummary(msg, truncate = 0):
    if not msg["text"] == None:
        return (msg["text"][:truncate] + '...') if (len(msg["text"]) > truncate and truncate is not 0) else msg["text"]
    if not msg["media"] == None:
        return "Media: " + str(msg["media"]["type"])
    if not msg["new_chat_participant"] == None:
        return msg["new_chat_participant"]["print_name"] + " was added to " + msg["chat"]["title"]
    else:
        return ":O"
