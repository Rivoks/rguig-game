# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define adamu = Character("Adamu")
define noname = Character("???")

define characterSize = .8

init:

    # Custom transitions

    $ flash = Fade(.25, 0, .75, color="#fff")

    # Background Env

    image adamuRoom:
        "background/env/adamu_room.png"

    image schoolPath1:
        "background/env/school_path1.jpg"

    image frontSchool:
        "background/env/front_school.png"

    image corridorsSchool:
        "background/env/corridors_school.png"   
    
    image amphiSchool:
        "background/env/amphi_school.png"        
    
    image stairsSchool:
        "background/env/stairs_school.png"    
    
    # Background Phone

    image msgAdmissL2:
        "background/phone/admission_L2.png"


    # Characters

    image adamuChill:
        "characters/adamu/chill.png"
        zoom characterSize

    image adamuChillJoy:
        "characters/adamu/chill_joy.png"
        zoom characterSize

    image adamuSleeping:
        "characters/adamu/sleeping.png"
        zoom characterSize

    image adamuSurprise:
        "characters/adamu/surprised.png"
        zoom characterSize
    
    image adamuSurprisedSchool:
        "characters/adamu/surprised2.png"
        zoom characterSize

    image adamuSmileSchool:
        "characters/adamu/smile_school.png"
        zoom characterSize
    
    image adamuSpeakingSerious:
        "characters/adamu/speaking_serious.png"
        zoom characterSize

    image adamuStun:
        "characters/adamu/stun.png"
        zoom characterSize

    image adamuConfident:
        "characters/adamu/confident.png"
        zoom characterSize

    image adamuSorry:
        "characters/adamu/sorry.png"
        zoom characterSize

    image adamuSorry2:
        "characters/adamu/sorry2.png"
        zoom characterSize

    image ayaHurt:
        "characters/aya/hurt.png"
        zoom characterSize

    image ayaSurprise:
        "characters/aya/surprised.png"
        zoom characterSize

    image ayaCalm:
        "characters/aya/calm.png"
        zoom characterSize

    image ayaSorry:
        "characters/aya/sorry.png"
        zoom characterSize
    
    image ayaBlushed:
        "characters/aya/blushed.png"
        zoom characterSize
    
    image ayaBlushed2:
        "characters/aya/blushed2.png"
        zoom characterSize


# The game starts here.

label start:

    scene adamuRoom

    "{i}Montmorency, dans les tréfons du 95.{/i}"
    "{i}Dans la pénombre de sa chambre miteuse, c’est à la lumière bleutée de son téléphone qu’un jeune homme allait apprendre la nouvelle qui allait tout changer...{/i}"

    play music "audio/ost/violet_sky.mp3" volume 0.1 loop fadein 1.0
    show adamuChill with dissolve


    adamu "{i}*Clic clic clic*{/i}"
    adamu "Bordel de cul..."
    adamu "{i}*Clic clic clic*{/i}"
    adamu "Putain de Teemo de merde, on m'a mis mal."

    play sound "audio/fx/notification.mp3" volume 0.2

    "{i}*Téléphone vibre, Adam reçoit une notification*{/i}"

    scene msgAdmissL2 with dissolve
    pause 2

    adamu "Hmm..."
    adamu "Hein ? Mais non ?"
    adamu "..."

    scene adamuRoom with dissolve

    play sound "audio/fx/swoosh1.mp3" volume 0.2

    show adamuChillJoy with hpunch

    adamu "Ololo c'est trop, c'est trop !"
    adamu "J'AI VALIDÉ, JE SUIS PLUS STUCK L1 !"
    adamu "Mimi ne me rattrapera pas d'aussitôt héhé..."
    
    hide adamuChillJoy with dissolve

    "{i}Incroyable ! Pour la première fois en trois ans, cet ignoble individu valida sa première année universitaire.{/i}"
    "{i}Si jusqu’ici toutes les portes lui paraissaient fermées, désormais plus rien ne semblait arrêter celui que l’on nommait « Venturu-en-kokoro ».{/i}"
    "{i}Cette première réussite marqua le début d'une nouvelle ère. Bien conscient qu'il devra faire face à la dure réalité du monde étudiant universitaire, l'heure n'était pas aux inquiétudes.{/i}"
    "{i}En effet, celui-ci ne rêvait que d’une seule chose : réussir à trouver sa première copine.{/i}"
    "{i}En plus de 20 ans d'existence, il n'avait jamais établi le moindre contact physique avec une fille.{/i}"
    "{i}C'est alors que rongé par le désespoir, le calbute rempli de mayonnaise, il décida de rejoindre l’organisation PALM pour changer le cours de son sinistre destin.{/i}"

    scene black with fade

    stop music fadeout 1.0

    "{i}Trois mois plus tard. Le jour de la rentrée.{/i}"
    
    adamu "Hmm..."
    play sound [ "<silence 1>", "audio/fx/anime_wow.mp3" ] volume 0.05
    adamu "Ah ah ! Iyaaaaaaa ! Pas ici Sawa-chan..."
    adamu "Sekusuu..."

    scene adamuRoom
    show adamuSleeping with dissolve

    adamu "Hum ?"
    adamu "..."
    
    play sound "audio/fx/collision.mp3" volume 0.8
    show adamuSurprise with vpunch

    adamu "PUTAIN ZEBIIIIIIIII !!!"

    play music "audio/ost/speed.mp3" volume 0.1 loop fadein 1.0

    adamu "BORDEL J'AI ENCORE TROP DORMI !"
    adamu "JE SUIS EN RETARD DES LE 1ER JOUR !!!"
    adamu "Vite, je dois me dépêcher !"

    play sound "audio/fx/flashback.mp3" volume 0.5

    scene schoolPath1 with flash

    play sound "audio/fx/run.mp3" volume 0.5
    play sound "audio/fx/breathing.mp3" volume 0.5

    "{i}*Court en direction de l'école*{/i}"

    show adamuSpeakingSerious with dissolve

    adamu "Plus vite, il faut que j'accèlère."
    adamu "Je me demande comment ça va se passer aujourd'hui, Il faut que je fassse bonne impression."

    play sound "audio/fx/run.mp3" volume 0.5

    "{i}*Cours*{/i}"

    adamu "Je suis presque arrivé, encore un petit effort."

    "{i}*Cours*{/i}"

    show adamuSmileSchool
    adamu "C'est ici !"
    
    stop music fadeout 0.5
    stop sound fadeout 0.5

    scene frontSchool with fade

    play sound "audio/fx/school_ring.mp3" volume 0.2

    "{i}*Sonnerie*{/i}"

    show adamuSpeakingSerious with dissolve

    adamu "C'est la sonnerie, les cours ont commencé ! Vite !"

    play music "audio/ost/speed.mp3" volume 0.1 loop fadein 1.0
    play sound "audio/fx/run.mp3" volume 0.5

    "{i}*Cours*{/i}"

    scene corridorsSchool with fade
    show adamuSorry with dissolve
    
    stop sound fadeout 0.5

    adamu "Je suis bientôt arrivé, c'est juste après ces marches"
    "{i}*Cours*{/i}"

    scene stairs_school with fade
    
    hide adamuSpeakingSerious
    show adamuConfident
    
    adamu " C'est bon ma nouvelle vie m'att..."

    hide adamuConfident
    show adamuStun


    play sound "audio/fx/bump.mp3" volume 0.2
    stop music
    "{i}*BOUM* (Cogne quelqu'un){/i}" with vpunch

    hide adamuStun
    show adamuStun at right with dissolve
    adamu "Argh..."

    show ayaHurt at left with dissolve
    noname "Ouille..."
    
    play sound "audio/fx/exclamation.mp3" volume 0.4
    play music "audio/ost/flying_fairy.mp3" volume 0.1 fadein 1.0 loop

    hide ayaHurt at left
    show ayaSurprise at left 

    noname "Mince, mes affaires..."
    
    show adamuSorry2 at right

    adamu "Rien de cassé ? Je suis désolé..."

    hide ayaSurprise at left
    show ayaCalm at left 

    noname "Je vais bien, merci."

    hide adamuSorry2
    show adamuSorry at right
    adamu "Donne moi ça, je vais t'aider."

    show ayaSorry at left
    noname "Pas la peine, ne t'en fais pas haha..."
    adamu "Vous voulez bien ?"
    adamu "..."

    hide adamuSorry
    show adamuSmileSchool at right
    adamu "Et voilà c'est nickel !"

    hide ayaSorry
    noname "Merci, c'est super gentil"

    hide ayaCalm
    show ayaBlushed at left

    noname "Allez je file, je vais être en retard pour de bon cette fois ahah."

    hide adamuSmileSchool
    show adamuSurprisedSchool at right
    adamu "Attends comment tu t'app..."

    hide ayaBlushed
    show ayaBlushed2 at left

    noname "À la prochaine, salut !"

    hide ayaBlushed2 with dissolve
    hide adamuSurprisedSchool

    adamu "Je n'ai pas pu lui demander son nom..."

    scene stairs_school
    show adamuSorry with dissolve

    adamu "Elle était pressé, c'est sûrement pour ça haha..."  

    show adamuStun

    adamu "Enfin je crois..."
    
    hide adamuStun
    show adamuSorry

    adamu "Haha..."
    adamu "J'espère que je la reverrai, elle était vraiment mignonne..."

    show adamuSpeakingSerious

    stop music fadeout 1.0

    adamu "Voilà la porte de l'amphi."

    play sound "audio/fx/door_open.mp3" volume 0.5
    
    show adamuConfident
    adamu "Tout commence ici."

    play sound "audio/fx/flashback.mp3" volume 0.5

    scene amphiSchool with flash

    "{i}TO BE CONTINUED...{/i}"
    pause 5

    return
