# Lesson 5 - Stairway To Heaven

We are now going to start to create items in our Minecradft world!

Present the code in `stairway.py` to the young coders. It is a good idea to have them type it in as you go.

As the code is presented to the young coders explain what each line does. Most of the code should already be familiar as it is the same as the previous examples.

Notice how we get the player position. This is because we want to place the stairs near to where they are so that we don't have to wonder around and find them.

We also have to find out how high the terrain is where we want to place the stairs, just is case we are not on a flat area.

Now the exciting part, we use a loop to create the stairs. Notice how each time we place the step block and a solid block for the next step up to be place upon.

Run the program. Check that it runs without any errors. If an error is displayed, do not panic, it just means that you need to fix the program and run it again.

Now have the coders find their stairs (they might need to turn around to face them). Now they should be able to walk up them. Explain how this might have taken a bit of time to create by hand, but we can run the program any time (and anywhere) we want and get more stairs instantly!

In the next lesson we will do a little bit more with Minecraft.

# Exercises

## Beginner

Create a taller flight of steps (Hint: each time we run the loop we get an extra step, what controls how many loop iterations there are?).

## Intermediate

Can you make the stairs two blocks wide so that they are easier to climb (Hint: The stairs go up in the 'X' direction, so the width of the stairs is controlled by the 'Z' direction).

## Advanced

Can you change the direction in which the stairs climb. Note that there are two aspects to this. Firstly you must consider how to increase the step in a different direction, then you must use the step that faces the correct way (Hint: the WOOD_STEP block also has a data value that is used for this).
