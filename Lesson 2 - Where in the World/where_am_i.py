#!/usr/bin/env python3
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
print("You are at {0}, {1}, {2}".format(x, y, z))
