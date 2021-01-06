#!/usr/bin/env python3
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = 10
z = 20
y = mc.getHeight(x, z)
mc.player.setPos(x, y, z)
