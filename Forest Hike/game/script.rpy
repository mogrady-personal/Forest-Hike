# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define laura = Character('Laura')
define tom = Character('Tom')
#define music = "Music/mozart.ogg"
#define sound = "Sound/woof.mp3"


# The game starts here.
label start:
play music "Music/mozart.ogg"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene bg forest day with fade

# Play Music
#play music "mozart.ogg"
# play sound "woof.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
show laura angry
laura "Wait up, Tom!"
laura "Tom!"
laura "I said wait up!"
laura "...Tom?"

hide laura
scene bg forest day with vpunch
show tom happy at right with moveinbottom

tom "Boo!"

show laura angry at left with moveinleft

laura "Yikes... not again."
tom "Are you scared?"
laura "Not at all."

show laura sad


laura "Running off like that is dangerous, you know."
laura "We are in the forest. We could get lost."
tom "Okay okay mom. I won't do it again."

menu:
    "Which way should we go?"

    "Left":
        tom "Let's check out the trail on the left!"
        $ is_lost = True
    "Right":
        tom "Right is always the right way to go!"
        $ is_lost = False
scene bg forest noon with Dissolve(3.0)
scene bg forest dusk with Dissolve(3.0)
show laura sad at left with moveinleft
laura "It's getting late. Are you sure we aren't lost?"
if is_lost:
    show tom sad at right with moveinleft
    tom "I hope not, but I have a bad feeling about this."
else:
    show tom happy at right with moveinleft
    tom "We are fine. Look! There's the end of the trail."
    tom "I'm the best scout around."
    play sound "Sound/woof.mp3"

    # These display lines of dialogue.

# e "You've created a new Ren'Py game."

# e "Once you add a story, pictures, and music, you can release it to the world!"

# This ends the game.
return
