#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   logger.py                                                                  #
#                                                                              #
#   Class to log in a fancy style.                                             #
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


from telegapi.TC import TC as TC
from telegapi import utils

from time import gmtime, strftime
import json


class logger:
    info = {'logLevel': 1, 'colorCode': TC.ICyan, 'prefix': " INFO "}
    out = {'logLevel': 2, 'colorCode': TC.IWhite, 'prefix': ""}
    debug = {'logLevel': 3, 'colorCode': TC.IBlue, 'prefix': " DEBUG"}
    warn = {'logLevel': 4, 'colorCode': TC.IYellow, 'prefix': " WARN "}
    error = {'logLevel': 5, 'colorCode': TC.Red, 'prefix': " ERROR"}

    def log(self, log_type, text):
        if log_type["logLevel"] < self.info["logLevel"] or log_type["logLevel"] > self.error["logLevel"]:
            self.log(self.error, "First parameter of \"logger.log\" is incorrect!")
            return False
        text = text.replace(TC.Rst, TC.Rst + TC.IWhite)
        prefix = ""
        if log_type["prefix"] != "":
            prefix = TC.IWhite + "[" + log_type["colorCode"] + log_type["prefix"] + TC.IWhite + "] "
        current_time = "[" + strftime("%H:%M", gmtime()) + "]"
        print_text = TC.IWhite + current_time + prefix + text + TC.Rst
        plain_text = current_time + "[" + log_type["prefix"] + "] " + text
        print(print_text)
        # print(plain_text)
        return

    def msg(self, msg):
        # return
        output = ""
        if "username" in msg["chat"]:
            output = output + TC.ICyan + msg["chat"]["username"]
        elif "title" in msg["chat"]:
            output = output + TC.Cyan + msg["chat"]["title"]
        elif "id" in msg["chat"]:
            output = output + TC.Cyan + msg["chat"]["id"]
        else:
            self.log(self.error, "msg[\"chat\"] doesn't have 'username', 'title', or 'id'. msg -> " + json.dump(msg))

        output = output + TC.IGreen + " <<< " + TC.ICyan + msg["from"]["first_name"] + TC.Rst + TC.Rst + ": "

        # if not syncFinished:
        # output = output+"("+"old"+") "
        if "fwd_src" in msg:
            output = output + TC.IPurple + "[fwd " + TC.ICyan + msg["fwd_src"]["username"] + TC.IPurple + "]" + TC.Rst
        if "reply" in msg:
            output = output + TC.IPurple + "[reply " + TC.ICyan + str(
                msg["reply"]["from"]["username"]) + TC.Rst + ": " + TC.Yellow + utils.msg_get_summary(msg["reply"],
                                                                                                    10) + TC.IPurple + "]" + TC.Rst
        if "reply_id" in msg:
            output = output + TC.IPurple + "[reply " + TC.ICyan + str(msg["reply_id"]) + TC.IPurple + "]" + TC.Rst
        output = output + TC.IYellow + utils.msg_get_summary(msg, 0) + TC.Rst
        output = output.replace('\n', ' ').replace('\r', '')
        self.log(self.info, output)
        return
