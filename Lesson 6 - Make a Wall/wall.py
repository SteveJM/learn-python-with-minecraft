#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()
y = mc.getHeight(x - 4, z)

length = 6
height = 4

mc.setBlocks(x - 4, y, z + 4, x - 4 + length, y + height, z + 4, block.STONE_BRICK.id)
