#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   utils.py                                                                   #
#                                                                              #
#   General utility module.                                                    #
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

from inspect import getmembers
import pprint
pp = pprint.PrettyPrinter(indent=4)


def msgGetSummary(msg, truncate = 0):
    if 'text' in msg:
        return (msg["text"][:truncate] + '...') if (len(msg["text"]) > truncate and truncate is not 0) else msg["text"]
    elif 'new_chat_participant' in msg:
        return msg["new_chat_participant"]["print_name"] + " was added to " + msg["chat"]["title"]
    elif 'left_chat_participant' in msg:
        return msg["left_chat_participant"]["print_name"] + " left " + msg["chat"]["title"]
    elif 'audio' in msg:
        return "Media: " + "Audio"
    elif 'document' in msg:
        return "Media: " + "Document"
    elif 'photo' in msg:
        return "Media: " + "Photo"
    elif 'sticker' in msg:
        return "Media: " + "Sticker"
    elif 'video' in msg:
        return "Media: " + "Video"
    elif 'contact' in msg:
        return "Media: " + "Contact"
    elif 'location' in msg:
        return "Media: " + "Location"
    elif 'new_chat_title' in msg:
        return "Chat title changed from " + msg["chat"]["title"] + " to " + msg["new_chat_title"]
    elif 'new_chat_photo' in msg:
        return "Chat photo changed"
    elif 'delete_chat_photo' in msg:
        return "Deleted chat photo"
    elif 'group_chat_created' in msg:
        return "Group chat " + msg["chat"]["title"] + " created"
    else:
        return ":O"
