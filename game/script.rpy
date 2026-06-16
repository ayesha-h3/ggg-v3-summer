# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Isabelle", color="#b193bf")
define mom = Character("Mother")


# The game starts here.

label start:

    scene bg room

   "It's a warm summer day. You're outside, reading a book on a picnic blanket."

    mom "Isabelle! I'm bringing you some cookies."

    y "Yay! Cookies!"

    mom "Do you want me to bring some juice as well? It's hot out, it'll be refreshing."

    menu:
        "Apple juice, please!"
            jump apple
        "I'll come in and get it!"
            jump inside

    label apple:
        mom "Ok!"
    jump inside:
        mom "While you're at it, can you tell your sister to come inside too?"
        "You get up and start walking towards the front door. Oblivious to your surroundings, you trip on a rock."
        y "Oww...."
        "While you're on the floor, you notice something poking out from behind a tree."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
