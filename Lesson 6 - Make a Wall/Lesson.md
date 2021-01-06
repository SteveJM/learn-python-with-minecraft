# Lesson 6 - Build A Wall

We are now going to create more advanced items in our Minecradft world!

Rather than placing a single block, we can place many blocks with a single command. To do this we need to calculate the two diaonally opposite corners for the area that we want to create. This area can be a complete cube of blocks, a floor area, a wall, or a ceiling.

Use the environment around you as examples of these shapes, illustrating the diagonally opposite points that would be used to create each one.

Now lets put that into practice...

Present the code in `wall.py` to the young coders. It is a good idea to have them type it in as you go. Notice that we are using variables for the wall length and height. We don't have to do this, but doing so makes the code more readable.

As the code is presented to the young coders explain what each line does. Most of the code should already be familiar as it is the same as the previous examples.

Notice how we get the player position. This is because we want to place the wall near to where they are so that we don't have to wonder around and find them.

Notice that there is only a single command (`mc.setBlocks`) to create the entire wall. The wall is built along the 'Z' axis, therefore the 'Z' coordinate is the same at both ends of the wall. The length of the wall is determined by the difference in the two 'X' values and the height of the wall is determined by the difference in the two 'Y values. It will be very useful to refer to the Minecraft API resource to see the meaning of each value given to the `setBlocks` function.

In the next lesson we will do a little bit more with Minecraft.

# Exercises

## Beginner

Change the size of the wall, can you make it longer? taller?

Change the material of the wall.

## Intermediate

Build the wall along the 'X' axis.

Build a floor, by having it built in a area of the 'Y' axis.

## Advanced

Can you create a room by building four walls?

Actually you can build a room with just *two* function calls, can you think how to do this? (Hint: one of the block types is `Air`, can you build a large block of Brick filled with a slightly small block of Air?)
