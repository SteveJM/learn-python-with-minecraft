#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

# Note the place where the last flower was dropped.
lastX, lastY, lastZ = mc.player.getTilePos()

# We must now loop forever.
while True:
    x, y, z = mc.player.getTilePos()
    # Is the player still in the same location?
    if x != lastX or z != lastZ:
        # No, then we can drop a new flower.
        h = mc.getHeight(x, z)
        mc.setBlock(x, h, z, block.FLOWER_YELLOW.id)

        # Now update where the last flower was dropped.
        lastX = x
        lastZ = z

        # Wait for a short while between drops.
        sleep(2)
