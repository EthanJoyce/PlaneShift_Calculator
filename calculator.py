#!/usr/bin/env python3

# Copyright (C) 2015 Ethan Joyce
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math


triaPerPP = 30


startLevel = int(input("Enter your current level: "))
currentLevel = startLevel
newLevel = int(input("Enter the level you want: "))

requiredPP = 0
requiredTria = 0


if newLevel < startLevel:
    print("You can't go down in levels, silly!")
    exit(0);

for i in range(currentLevel, newLevel):
    requiredPP += math.ceil(currentLevel / 2)
    currentLevel += 1

requiredTria = requiredPP * 30

print("Start level: %d" % startLevel)
print("New level: %d" % newLevel)
print("Required PP: %d" % requiredPP)
print("Required Tria: %d" % requiredTria)
