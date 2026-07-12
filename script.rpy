define s = Character("Lumina" , color = "59E8F7")
define b = Character("Lumes", color = "F7B059")
define scroll = Character("Scroll")

label start:

    play music "adv audio.mp3"
    scene forest
    
    show lumina:
         zoom 1.5
         ypos 300
         xpos 300
    
    show lumes:
        zoom 1.5
        ypos 300
        xpos 100

    b "Hey there! I'm Lumes, and this is my {i}sister{/i} Lumina. {w}{p}We were having fun playing in the garden when all of a sudden, Lumina fell asleep.{w=0.1}"

    $ renpy.movie_cutscene("download.webm", delay=5, loops=0)   
    hide lumes
    hide lumina
    scene under1
    show lumina:
         zoom 1.5
         ypos 300
         xpos 300
    b "Lumina has fallen beneath the ground..."
    s "What's in this red box?"

    show scroll1:
        ypos 200
        xpos 600

    s "Oh wait, there's something on the back of the scroll! Hints!"
    scroll "'Hint 1: Summer, Spring, ____, Winter' and 'Hint 2: Water, wind, earth and ____'"
    s "Hmm.. what could the answer be?"

    scene options
    with dissolve

    show scroll1:
        ypos 200
        xpos 600

    show lumina:
        ypos 600
        xpos 800

    b "Here lies 2 paths, which one should Lumina choose?"

    menu:
        "Fire":
            "Correct!"
            hide lumina
            hide scroll1
            $ renpy.movie_cutscene("falls in fire.webm", delay=3.5, loops=0)
            show lava with None 
            show lumina:
             zoom 1.5   
             ypos 400
             xpos 100
            show bottle:
             ypos 300
             xpos 1000
            
            s "Wait, where am I now? Did I just fall again? There's lava everywhere!"
            b "{i}Behold! Here's a bottle with a message in it.{/i}"

            show scroll2:
             ypos 200
             xpos 600
            
            s "Why are you speaking like that? {p}{i}goes towards the bottle.{/i} {p}Anyway, it says \'76 101 97 118 101 63\'. I wonder what that means."

            b "{i}Looketh at they right for aid in thou quest.{/i}"

            show scroll3:
             zoom 1.5
             ypos 200
             xpos 1300 
            
            s "Ooh, that's so much easier to understand now! So this scroll contains a message made up by letters, and one letter is repeated twice."

            s "76 is L, 101 is e, 97 is a, 118 is v, 101 is again e, and 63 is a question mark.. {w} what could that possibly mean? {w=0.8} {p}Oh, I know! LEAVE! It is asking me if I want to leave."

            b "{i}Thou desires to leaveth?{/i}"
            menu:
                "YES":
                    hide lumina
                    hide scroll3
                    hide scroll2
                    hide bottle
                    $ renpy.movie_cutscene("sleepy head.webm", delay=4, loops=0)
                    $ renpy.movie_cutscene("credits.webm", delay=2, loops=0)

                "NO":
                    $ renpy.movie_cutscene("game over.webm", delay=5, loops=0)
                    $ renpy.movie_cutscene("credits.webm", delay=2, loops=0)
        "Water":
            "Wrong!"
            $ renpy.movie_cutscene("game over.webm", delay=5, loops=0)
            $ renpy.movie_cutscene("credits.webm", delay=2, loops=0)
              

    return
