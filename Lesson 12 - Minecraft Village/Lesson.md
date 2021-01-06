# Lesson 12 - Village

In the last lesson we wrote a program to build a skyscraper in our Minecraft World, but why should we stop there?

Now we are going to create an entire village!

Have the young coders examine the `Village.py` program and explain how it works. By now most of the code should be starting to become very familiar to them.

The interesting things to notice in the code is how the shell of the house is create with just two commands; one to build a complete brick cube, and the other to hollow it out with air. Also the way that the two doors are created so that we get top and bottom halves of the doors correctly aligned to the exterior walls.

Finally, notice that the important lines are the three at the bottom, the first creates our Minecraft connection, the next one initializes our village area by creating the main road and the final line places a house on the road.

# Exercises

## Beginner

Copy the line of code that creates the house and add another line, modify this so that the house is built next to the existing one. Repeat this for more houses.

Replace the two lines with a loop that creates multiple houses.

## Intermediate

Duplicate the entire `makeHouse` function and rename it `makeShop`. Change the design so that it looks like a shop (perhaps by using glass for the front wall).

Place shops on the other side of the street to the houses.

## Advanced

Get creative with the village. Add several different building designs and have the loop randomly pick different buildings.
