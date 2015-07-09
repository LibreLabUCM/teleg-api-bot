#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   TC.py                                                                      #
#                                                                              #
#   Text format definitions.                                                   #
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

class TC:
    TC='\033['
    CLR_LINE_START=TC+"1K"
    CLR_LINE_END=TC+"K"
    CLR_LINE=TC+"2K"
    # Hope no terminal is greater than 1k columns
    RESET_LINE=CLR_LINE+TC+"1000D"

    # Colors and styles (based on https://github.com/demure/dotfiles/blob/master/subbash/prompt)

    Bold=TC+"1m"    # Bold text only, keep colors
    Undr=TC+"4m"    # Underline text only, keep colors
    Inv=TC+"7m"     # Inverse: swap background and foreground colors
    Reg=TC+"22;24m" # Regular text only, keep colors
    RegF=TC+"39m"   # Regular foreground coloring
    RegB=TC+"49m"   # Regular background coloring
    Rst=TC+"0m"     # Reset all coloring and style

    # Basic
    Black=TC+"30m";
    Red=TC+"31m";
    Green=TC+"32m";
    Yellow=TC+"33m";
    Blue=TC+"34m";
    Purple=TC+"35m";
    Cyan=TC+"36m";
    White=TC+"37m";

    # High Intensity
    IBlack=TC+"90m";
    IRed=TC+"91m";
    IGreen=TC+"92m";
    IYellow=TC+"93m";
    IBlue=TC+"94m";
    IPurple=TC+"95m";
    ICyan=TC+"96m";
    IWhite=TC+"97m";

    # Background
    OnBlack=TC+"40m";
    OnRed=TC+"41m";
    OnGreen=TC+"42m";
    OnYellow=TC+"43m";
    OnBlue=TC+"44m";
    OnPurple=TC+"45m";
    OnCyan=TC+"46m";
    OnWhite=TC+"47m";

    # High Intensity Background
    OnIBlack=TC+"100m";
    OnIRed=TC+"101m";
    OnIGreen=TC+"102m";
    OnIYellow=TC+"103m";
    OnIBlue=TC+"104m";
    OnIPurple=TC+"105m";
    OnICyan=TC+"106m";
    OnIWhite=TC+"107m";
