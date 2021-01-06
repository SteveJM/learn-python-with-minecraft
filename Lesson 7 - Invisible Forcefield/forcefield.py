#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()
y = mc.getHeight(x + 10, z)

mc.setBlock(x + 10, y + 1, z, block.DIAMOND_BLOCK.id)
mc.postToChat("Destroy the Diamond Block!")

# The 'forcefield' is an area four blocks around the Diamond Block in both X and Z directions.
fx1 = x + 4
fx2 = x + 16
fz1 = z - 6
fz2 = z + 6

# Note the player's last "good" location.
lastX, lastY, lastZ = mc.player.getPos()

# We must now loop forever.
while True:
    x, y, z = mc.player.getPos()
    # Is the player within the forcefield area?
    if x > fx1 and x < fx2 and z > fz1 and z < fz2:
        # Yes, they are, move them back to where they were.
        mc.player.setPos(lastX, lastY, lastZ)
    else:
        # No they are not, remember their location as their last "good" position.
        lastX = x
        lastY = y
        lastZ = z
