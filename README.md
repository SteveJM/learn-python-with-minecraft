# Learn Python With Minecraft

This is a course that is aimed at teaching young coders the basics of Python Programming using Minecraft. It requires a Raspberry Pi with Python and Minecraft-Pi installed, both of these are included in the standard `Raspbian` installation.

The course is split into a series of lessons, it is expected that each lesson will be a teacher-led class. Each lessons should generally fit into an hour long session. The lessons should be progressed in sequence as they typically get more involved as they go.

## Warning

The programs created in these lessons typically make alterations to the Minecraft World. These may destroy anything already created within the World. It is *Highly Recommended* that new Worlds are created by the students for the purpose of these lessons so that no personal creations are destroyed.

## Using Minecraft

Before you start make sure that all of the students are familiar with Minecraft on the Raspberry Pi. They should be able to move around, place and destroy blocks. The will need to be able to use the mouse to look around, amd will need to knoow the following command keys:

* Move Forwards - 'w'
* Move backwards - 's'
* Move left - 'a'
* Move right - 'd'
* Quit - 'Esc'
* Free Mouse Pointer - 'Tab'

Have the students practice for a while and become familiar with the mouse and keyboard functions.

## Resources

Within the `Resources` directory there are three useful resource PDFs:

* Minecraft API
* Minecraft Blocks
* Python Basics

These resources are designed to be printed on double-sided A4 sheets as reference material for the young coders. I found it ideal to laminate them for re-use between lessons.

### Minecraft API

The Minecraft API Resource lists all of the Minecraft functions that are available. Note that every lesson in this series makes use of these functions.

### Minecraft Blocks

Lesson 4 onwards place blocks in the Minecraft World. The available blocks are listed on this sheet. Note that some blocks (marked with a *) take a 'data' value that is used for some aspect of the rendered block.

### Python Basics

Throughout this course the young coders will be using the Python Programming Language. This resource summarizes the core features of Python for ease of reference.

## Maximum Coordinates

The Minecraft world in Minecraft-Pi is actually quite small and limited. You might not notice this when "playing" with the game because it takes time to build and move around. However, when writing programs is is much easier to use larger numbers and reach the boundaries.

X and Z are limited to values between -128 and +127, with 0, 0 being the central point. Therefore the "World" is an area 256 blocks by 256 blocks. Y is limited to values between -64 and +63 (with zero being "sea level").
