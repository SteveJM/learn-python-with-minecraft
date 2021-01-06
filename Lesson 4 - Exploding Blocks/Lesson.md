# Lesson 4 - Exploding Blocks

This is a very exciting lesson. We are going to write a program to do something that is not possible with the Minecraft-Pi game itself.

Have the young coders manually place a block of TNT in their Minecraft world. Get them to notice how they can destroy it, but that is all. It is "inactive" TNT. That is not much fun, so let's spice it up.

Present the code in `exploding_blocks.py` to the young coders. It is a good idea to have them type it in as you go.

As the code is presented to the young coders explain what each line does. Most of the code should already be familiar as it is the same as the previous examples.

Notice how we get the player position. This is because we want to place the TNT near to where they are so that we don't have to wonder around and find it.

We also have to find out how high the terrain is where we want to place the block, just is case we are not on a flat area.

Now the exciting line, we place a block of TNT near the player. But, not just that, we supply an extra argument, in this case a "1". Some blocks have a "data" value that can be set, TNT is such a block. Setting the data value to "1" makes it "Active" TNT.

Run the program. Check that it runs without any errors. If an error is displayed, do not panic, it just means that you need to fix the program and run it again.

Now have the coders find their block of TNT (they might need to turn around to face it). Now they should be able to "hit" it, this must be done using the left-mouse button. This will trigger the TNT which will explode soon after!

In the next lesson we will do a little bit more with Minecraft.

# Exercises

## Beginner

Can put other Blocks in your Minecraft world.

## Intermediate

Can you place several blocks of TNT close together for a larger explosion.

## Advanced

Can you see how to use "setBlocks" (notice the "s") to create a larger amount of TNT. Warning: Don't get too carried away, event a 4 x 4 x 4 lump of TNT is 64 blocks of TNT - that is a large explosion!