#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()
y = mc.getHeight(x + 3, z)
mc.setBlock(x + 3, y, z, block.TNT.id, 1)
