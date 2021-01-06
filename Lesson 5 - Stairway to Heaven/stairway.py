#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()
y = mc.getHeight(x + 3, z)

for i in range(10):
    mc.setBlock(x + 3 + i, y + i, z, block.STAIRS_WOOD.id)
    mc.setBlock(x + 4 + i, y + i, z, block.STONE.id)
