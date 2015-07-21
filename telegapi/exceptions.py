#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   exceptions.py                                                              #
#                                                                              #
#   teleg-api-bot exceptions.                                                  #
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


class ConexionFailedException(Exception):
    def __init__(self, text):
        self.description = text


class BadServerResponseException(Exception):
    def __init__(self, text, errorcode):
        self.description = text
        self.code = errorcode


class BadTelegAPIResponseException(Exception):
    def __init__(self, text):
        self.description = text


class BadParamException(Exception):
    def __init__(self, text):
        self.description = text


class InvalidAPICallException(Exception):
    def __init__(self, text):
        self.description = text
