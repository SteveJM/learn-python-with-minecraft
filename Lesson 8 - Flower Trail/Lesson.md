# Lesson 8 - Flower Trail

We are now going to write another program that interacts with the Player within the Minecraft World! This time, as the player moves around, they will leave a trail of flowers.

Just like in the previous lesson, we are going to monitor the position of the player within the Minecraft World, but this time our program will periodically drop a flower.

Present the code in `flowerTrail.py` to the young coders. It is a good idea to have them type it in as you go.

Explain to the young coders how the program works and explain how it periodically drops a flower, but only if their position has changed.

Notice that there are some comments within the code as it is now getting slightly more complicated. Also, it is important to realise that the flowers are only dropped whilst the program is running. Once it has stopped there will be nothing monitoring the players position and dropping flowers. This is why the program uses a loop that will keep it running forever (you will have to force it to stop).

In the next lesson we will do a little bit more with Minecraft.

# Exercises

## Beginner

Change the item that is dropped.

Change the delay between how often items are dropped.

## Intermediate

Notice how flowers are dropped even when we are over water, drop another object when we are over water (Hint: see the "getBlock()" function).

