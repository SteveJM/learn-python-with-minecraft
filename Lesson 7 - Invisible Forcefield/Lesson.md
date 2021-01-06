# Lesson 7 - Invisible Force-field

We are now going to write a program that interacts with the Player within the Minecraft World!

We are able to both monitor the position of the player within the Minecraft World and change their position. Our program will create an invisible force-field. This will be achieved by monitoring the location of the Player, if they enter a specific 'Zone' then it will adjust their position back to where they came from. To make this more enticing our program will place a diamond block just out of reach and ask the player to destroy it.

Present the code in `forcefield.py` to the young coders. It is a good idea to have them type it in as you go.

Explain to the young coders how the force-field works by marking it out on the room you are in, place an object representing the Diamond block and explain how it is necessary to check if the player is close to it by checking the X and Z coordinates (the force-field will extend all the up to the Sky).

Notice that there are some comments within the code as it is now getting slightly more complicated. Also, it is important to realise that the force-field is only in effect whilst the program is running. Once it has stopped there will be nothing to prevent the player moving anywhere they want. This is why the program uses a loop that will keep it running forever (you will have to force it to stop).

In the next lesson we will do a little bit more with Minecraft.

# Exercises

## Beginner

Change the size of the force-field.

Change the material of the item to be destroyed.

## Intermediate

Have the program display a message when you try and enter the force-field.

Create an invisible wall that will not let you walk through it, no matter how far along it you try and go.

## Advanced

Can you make the force-field only extend for a short space above and below Diamond block? Test this by flying over it and tunnelling underneath it.
