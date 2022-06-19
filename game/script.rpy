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
    
    image chairsAmphi:
        "background/env/chairs_amphi.png"        
    
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

    image adamuAngry:
        "characters/adamu/angry.png"
        zoom characterSize

    image adamuVeryAngry:
        "characters/adamu/very_angry.png"
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

    image mamiStoic:
        "characters/mami/stoic.png"
        zoom characterSize

    image mamiAnnoyed:
        "characters/mami/annoyed.png"
        zoom characterSize

    image mamiSpeaking:
        "characters/mami/speaking.png"
        zoom characterSize




# The game starts here.

label start:

    scene adamuRoom

    jump scene0_part2

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
    
    stop music
    stop sound

    jump scene0_part2


label scene0_part2:

    play sound "audio/fx/flashback.mp3" volume 0.5
    
    scene amphiSchool with flash

    play sound "audio/fx/classroom.mp3" volume 0.01 fadein 1.0

    show adamuSurprisedSchool
    adamu "Waaah ! C'est beaucoup plus grand que ce que je pensais."
    
    show  adamuStun
    adamu "Y'a presque plus de place, merde."
    adamu "Ah j'en vois une là-bas !"
    "{i}*Bruit de pas, Adam se faufile entre les rangs*{/i}"

    show adamuSorry
    adamu "Pardon, excusez-moi."
    adamu "..."
    hide adamuSorry
    show  adamuStun
    adamu "Tiens, je crois que j'ai déjà vu l'homme qui parle sur une photo, ça doit être le principal"
    "{i}*Adam s'assoie*{/i}"

    scene chairsAmphi with dissolve

    stop sound fadeout 0.5

    show adamuStun
    adamu "On voit pas grand chose d'ici"
    show adamuSorry
    adamu "Bon, c'est pas comme si j'allais suivre de toute façon."
    show adamuStun
    adamu "Tout le monde autour de moi est en train de prendre des notes."
    adamu "..."
    show adamuSorry2
    adamu "J'ai l'impression que le prof me fixe"

    show adamuAngry
    adamu "Je dois me fondre dans la masse, vite !"
    "{i}*Prends une feuille*{/i}"
    
    show adamuVeryAngry
    adamu "Merde, j'ai oublié ma trousse, je suis vraiment une pute de pute !"

    show adamuSorry
    "{i}*Se tourne sur sa droite*{/i}"
    adamu "Excuse-moi, t'au..."

    scene chairs_amphi with dissolve

    show adamuSorry at right
    show mamiStoic at left

    noname "Tiens. Il s'appelle revient."

    "{i}*Donne un stylo*{/i}"

    show adamuSurprise2 at right
    
    adamu "Mer-mer-mer..."
    show mamiAnnoyed at left
    noname "?"
    adamu "Euh..."

    scene chairsAmphi with dissolve

    "{i}La présentation suivi son cours mais Adam fut incapable de se concentrer.{/i}"
    "{i}Il était stupéfait par la beauté et la prestance de ce qu’il appelait une Basic White Bitch, être qu’il a toujours convoité dans ses rêves les plus profonds.{/i}"
    "{i}Il faut dire que que cette jeune blonde à l’air désinvolte parrassait désintéressée aux premiers abords mais dégageait une certaine grâce à travers ses gestes très tendres.{/i}"
    "{i}Adam resta circonspect, on aurait dit que le temps s'était figé pour lui.{/i}"
    "{i}La présentation se termina sans qu'il n'ait pu rien dire.{\i}"
    "{i}Alors qu'il se ressassait ses échecs précédents, pris dans un élan de courage, c'est avec une voix suave qu'il disa :{/i}"

    show adamuSorry at right with dissolve

    return
