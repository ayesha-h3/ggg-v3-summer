# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Isabelle", color="#b193bf")
define f = Character("unnamed friend")



# The game starts here.

label start:

    f "Come on! We don't have all day."
    y "I'm coming!"

    "It's a warm summer day. Your friend has dragged you along on a hike."

    y "Where are we even going again?"
    f "The peak of the mountain has an AMAZING view of the waterfall!"

    "It's been five hours. You have no idea how friend has so much stamina, because you're exhausted."

    menu:
        "can we take a break or something? im so tired":
            $tired = True
            jump break
        "Let's keep going":
            jump continue
    
    label continue:
        f "ok, whatever you say..."
        "You're still lagging behind, but you continue with renewed resolve."

    label break:
        f "luckily I brought some snacks!"
        $honesty +=1
        "a few minutes later..."
        f "let's get going again!"

    "You keep walking."

    if tired:
        "Your legs are starting to feel like jelly with how long you've been walking."
        y "Seriously, how do you do this?"
        f "Years of practice. Hey, watch out---!"
        "You spectacularly trip over a rock and fall flat on your face."
        f "Hey! Hey! Are you ok? Look at me! Say something? Hello?"
    
    else:
        y "Hey, this isn't so bad."
        f "Watch you jinx yourself or something."
        y "What do you mean--"
        f "lol i'm just messing with you!"
        "You keep walking, when you suddenly hear a faint rumbling noise."
        f "Do you hear that?"
        y "Yeah--"
        "On the edge of the trail, the ground starts giving underneath you."
        f "ISABELLE--"
        "You try to jump over, but it seems like your movement made it worse. You start slipping uncontrollably down the side of the mountain."
        f "GRAB ONTO SOMETHING!"
        "It's too late. You can only wonder when you'll hit the ground now."
        "THUD!"
        "There's dust everywhere. You try to get up, but your head starts pounding. You decide to lie back down, and close your eyes for just a second..."

    
    

        







    # This ends the game.

    return
