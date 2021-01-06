#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

# Drop a block of lava and wait for it to flow.
mc.setBlock(x+3, y+3, z, block.LAVA.id)
sleep(20)

# Now drop a block of water above the lava, notice that it flows faster
mc.setBlock(x+3, y+5, z, block.WATER.id)
sleep(4)

# Now stop the water flow.
mc.setBlock(x+3, y+5, z, block.AIR.id)
