#!/usr/bin/env python3
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


def msgGetSummary(msg, truncate = 0):
    summary = ""

    if 'text' in msg:
        summary += "[Text: " + ( (msg["text"][:truncate] + '...') if (len(msg["text"]) > truncate and truncate is not 0) else msg["text"] ) + "] "
    if 'new_chat_participant' in msg:
        summary += msg["new_chat_participant"]["print_name"] + " was added to " + msg["chat"]["title"]  + " "
    if 'left_chat_participant' in msg:
        summary += msg["left_chat_participant"]["print_name"] + " left " + msg["chat"]["title"]  + " "
    if 'audio' in msg:
        summary += "[Media: " + "Audio"  + "] "
    if 'document' in msg:
        summary += "[Media: " + "Document"  + "] "
    if 'photo' in msg:
        summary += "[Media: " + "Photo"  + "] "
    if 'sticker' in msg:
        summary += "[Media: " + "Sticker"  + "] "
    if 'video' in msg:
        summary += "[Media: " + "Video"  + "] "
    if 'contact' in msg:
        summary += "[Media: " + "Contact" + "] "
    if 'location' in msg:
        summary += "[Media: " + "Location"  + "] "
    if 'new_chat_title' in msg:
        summary += "[Chat title changed from " + msg["chat"]["title"] + " to " + msg["new_chat_title"]  + "] "
    if 'new_chat_photo' in msg:
        summary += "[Chat photo changed"  + "] "
    if 'delete_chat_photo' in msg:
        summary += "[Deleted chat photo"  + "] "
    if 'group_chat_created' in msg:
        summary += "[Group chat " + msg["chat"]["title"] + " created"  + "] "
    
    return summary
