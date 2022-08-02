# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define adamu = Character("Adamu", color="#7ed6df")
define mami = Character("Mami", color="#f0932b")
define aya = Character("Aya", color="#badc58")
define noname = Character("???")

define characterSize = .8

init python:

    config.underlay.append(
        renpy.Keymap(
            mousedown_1 = lambda: renpy.run(renpy.play("audio/fx/a_button.mp3"))
        )
    )

init:


    # Custom transitions

    $ flash = Fade(.25, 0, .75, color="#fff")

    # Background Env

    image adamuRoom:
        "background/env/adamu_room.png"

    image jitenshaVisu:
        "background/env/jitensha.png"

    image schoolPath1:
        "background/env/school_path1.jpg"

    image frontSchool:
        "background/env/front_school.png"

    image corridorsSchool:
        "background/env/corridors_school.png"

    image classroomSchool:
        "background/env/classroom_td.png"

    image amphiSchool:
        "background/env/amphi_school.png"

    image chairsAmphi:
        "background/env/chairs_amphi.png"

    image stairsSchool:
        "background/env/stairs_school.png"

    image cafeteriaSchool:
        "background/env/cafetaria.png"

    # Background Phone

    image msgAdmissL2:
        "background/phone/admission_L2.png"

    image msgClassMami:
        "background/phone/classroom_mami.png"


    # Characters

    # Adamu

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

    image adamuVeryHappy:
        "characters/adamu/very_happy.png"
        zoom characterSize

    # Aya

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

    image ayaCry:
        "characters/aya/cry.png"
        zoom characterSize


    # Mami
    image mamiStoic:
        "characters/mami/stoic.png"
        zoom characterSize

    image mamiAnnoyed:
        "characters/mami/annoyed.png"
        zoom characterSize

    image mamiSpeaking:
        "characters/mami/speaking.png"
        zoom characterSize

    image mamiAsking:
        "characters/mami/asking.png"
        zoom characterSize

    image mamiBlush:
        "characters/mami/blush.png"
        zoom characterSize

    image mamiSmile:
        "characters/mami/smile.png"
        zoom characterSize

    image mamiAngryCute:
        "characters/mami/angry-cute.png"
        zoom characterSize

    image mamiTaunt:
        "characters/mami/taunt.png"
        zoom characterSize




# The game starts here.

label start:

    scene adamuRoom

    "{i}Montmorency, dans les tréfons du 95.{/i}"
    "{i}Dans la pénombre de sa chambre miteuse, c’est à la lumière bleutée de son téléphone qu’un jeune homme allait apprendre la nouvelle qui allait tout changer...{/i}"

    jump scene2


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

    "{i}*Court*{/i}"

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

    play sound "audio/fx/flashback.mp3" volume 0.5

    scene amphiSchool with flash

    play sound "audio/fx/classroom.mp3" volume 0.1 fadein 1.0

    show adamuSurprisedSchool
    adamu "Waaah ! C'est beaucoup plus grand que ce que je pensais."

    show  adamuStun
    adamu "Y'a presque plus de place, merde."
    adamu "Ah j'en vois une là-bas !"
    "{i}*Bruit de pas, Adam se faufile entre les rangs*{/i}"

    show adamuSorry
    play music "audio/ost/quiet_intelligence.mp3" volume 0.1 fadein 1.0
    adamu "Pardon, excusez-moi."
    adamu "..."
    hide adamuSorry
    show  adamuStun
    adamu "Tiens, je crois que j'ai déjà vu l'homme qui parle sur une photo, ça doit être le principal"
    "{i}*Adam s'assoie*{/i}"

    scene chairsAmphi with dissolve

    stop sound fadeout 3


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

    play sound "audio/fx/sheet_paper.mp3" volume 0.5
    "{i}*Prends une feuille*{/i}"

    play sound "audio/fx/collision.mp3" volume 0.8
    show adamuVeryAngry with vpunch
    adamu "Merde, j'ai oublié ma trousse, je suis vraiment une pute de pute !"

    scene chairsAmphi
    show adamuSorry
    "{i}*Se tourne sur sa droite*{/i}"
    stop music fadeout 1.0
    adamu "Excuse-moi, t'au..."

    scene chairs_amphi with dissolve

    show adamuSorry at right
    show mamiStoic at left


    play music "audio/ost/bwb_encounter.mp3" volume 0.1 fadein 1.0

    noname "Tiens. Il s'appelle revient."

    "{i}*Donne un stylo*{/i}"

    show adamuSurprisedSchool at right

    adamu "Mer-mer-mer..."
    show mamiAsking at left
    noname "?"

    show adamuStun at right
    adamu "Euh..."

    scene chairsAmphi with dissolve

    "{i}La présentation suivi son cours mais Adam fut incapable de se concentrer.{/i}"
    "{i}Il était stupéfait par la beauté et la prestance de ce qu’il appelait une Basic White Bitch, être qu’il a toujours convoité dans ses rêves les plus profonds.{/i}"
    "{i}Il faut dire que que cette jeune blonde à l’air désinvolte parrassait désintéressée aux premiers abords mais dégageait une certaine grâce à travers ses gestes très tendres.{/i}"
    "{i}Adam resta circonspect, on aurait dit que le temps s'était figé pour lui.{/i}"
    "{i}La présentation se termina sans qu'il n'ait pu rien dire.{\i}"
    "{i}Alors qu'il se ressassait ses échecs précédents, pris dans un élan de courage, c'est avec une voix suave qu'il disa :{/i}"

    show adamuSorry at right with dissolve
    show mamiStoic at left with dissolve
    adamu "Tiens, merci. Moi c'est Adam, et toi c'est...?"
    mami "Mami."
    mami "Mami Aoi."

    show adamuSmileSchool at right
    adamu "Enchanté Mami !"
    adamu "Je ne crois pas t'avoir déjà vu ici. Tu es nouvelle ?"
    mami "Ouais, j'habite assez loin."

    show adamuSurprisedSchool at right
    adamu "Tu ne connais pas grand monde alors, je suppose."
    mami "Personne, non."

    scene chairs_amphi with dissolve
    show mamiStoic with dissolve
    "{i}Cette solitude ne semblait pas l’inquiéter pour autant, elle semblait y être habituée."

    scene chairsAmphi with dissolve
    show mamiStoic at left with dissolve
    show adamuSpeakingSerious at right with dissolve

    play sound "audio/fx/breathing.mp3" volume 0.5
    adamu "Ah ..."
    adamu "..."
    adamu "Dis est-ce que t'as Twi..."
    adamu "Twi..."
    adamu "Toi..."
    adamu "Toiture !"

    stop music fadeout 1.0
    show mamiAsking at left
    mami "Toiture ?"
    show adamuSorry at right
    adamu "Est-ce que t'as une toiture ?"
    mami  "..."

    scene chairsAmphi with dissolve
    play music "audio/ost/dramatic_kaguya.mp3" volume 0.1 fadein 1.0

    "{i}Adam bégaya."
    "{i}Catastrophe. Lui qui avait passé son été à travailler son éloquence en prévision de ce genre d’opportunité retomba dans ses anciens travers."
    "{i}Mami le fixait d’un air décontenancé sans dire un mot."

    show mamiSpeaking with dissolve
    "{i}Tout autour de lui devenait trouble, tout semblait perdu…"

    hide mamiSpeaking
    stop music fadeout 1.0

    play sound [ "<silence 1>", "audio/fx/excuse_moi.mp3" ] volume 0.2
    "{i}Une voix retentit: « Excuse-moi si j’tai blessé… »."
    "{i}En l’espace d’une fraction de seconde, lorsque tout semblait contre lui, Adamu demanda de manière intrépide les coordonnées de Mami."

    show adamuSpeakingSerious with dissolve
    play music "audio/ost/confess_kaguya.mp3" volume 0.1 fadein 1.0
    adamu "Est-ce que t'as Twittâ ?"
    hide adamuSpeakingSerious
    show mamiBlush with dissolve

    "{i}Surprise, Mami donna son Twittâ en détournant les yeux, comme d’un air légèrement gênée."
    hide mamiBlush
    "{i}Bénédiction divine, baraka du tout puissant, notre Rguig venait de réaliser l’impossible."
    "{i}Désormais c’est sûr, plus rien ne sera comme avant."
    scene black with dissolve
    "{i}La vraie rentrée se faisant dans une semaine, les jours passèrent sans trop de bruits."
    
    jump scene2

label scene2:

    scene frontSchool with dissolve

    show mamiStoic at left

    show adamuSmileSchool at right
    
    mami "..."
    
    adamu "Salut Mami!"

    show mamiAngryCute at left

    mami "Ça fait cinq minutes que je t’attends..."

    show adamuSorry2 at right

    adamu "Euh je... en fait... il était une fois... vous voulez bien... c’est à dire que..."

    hide adamuSmileSchool
    show adamuAngry at right

    adamu "{i}Putain j'aurais jamais dû tag une ranked ce matin !{/i}"

    show mamiSmile at left

    mami "** Sourit **"

    mami "Bon c'est pas grave, on va manger ?"

    show adamuSmileSchool at right

    adamu "Yoshuu !"

    scene black with dissolve

    scene cafeteriaSchool with dissolve

    show mamiAsking at left with dissolve

    mami "Ton assiette est vachement équilibrée"

    show adamuSorry at right with dissolve

    adamu "Oui c’est normal je suis à la diète en ce moment, on m’a mit mal ahah..."

    show mamiTaunt at left
    
    mami "C'est pour plaire aux filles que tu le fais hein..."

    show adamuSorry2 at right
    hide adamuSorry

    adamu "Vous voulez bien ?"

    show mamiTaunt at left
    
    mami "J'en étais sûre ahah"
    mami "Alors t'as des vues sur qui ? Tu vas tout me dire !"

    show adamuSorry at right
    hide adamuSorry2

    adamu "Ahah pourquoi pas mais toi tu t'intéresse pas aux mecs ?"

    show mamiStoic at left

    mami "..."

    show adamuSurprisedSchool at right

    adamu "Mami-chan ?"

    show mamiSpeaking at left

    mami "C’est rien t’inquiètes, je viens juste de sortir d’une longue relation c’est un peu compliqué du coup..."

    adamu "Ah excuse moi... je... euh..."

    mami "Tu pouvais pas savoir t'inquiètes"

    show mamiAnnoyed at left

    mami "En tout cas moi les garçons c’est fini, j’ai l’impression que c’est toujours la même chose, j’ai l’impression de toujours tout faire mal, enfin, je sais pas…"

    menu mami_good_girl:
        "Dire à Mami que c'est une fille bien ?"
        "Oui":
            jump scene2_1
        "Non":
            jump scene2_2


label scene2_1:
    scene cafeteriaSchool
    
    show mamiBlush at left

    show adamuSpeakingSerious at right

    mami "Pourquoi tu dis ça ? Et puis en vrai je suis pas celle que tu penses..."

    scene cafeteriaSchool with dissolve

    show ayaSurprise

    "{i}Aya venait d'arriver au réfectoire du CROUS, elle suprend au loin Adamu en train de déjeuner avec Mami. Adam croisa son regard et l'évita aussitôt{/i}"

    scene cafeteriaSchool with dissolve

    show mamiBlush at left

    show adamuSorry at right

    adamu "{i}Bordel de pute je suis cramé ! Aya voudra plus jamais me parler putain zebi…{/i}"

    show mamiAsking at left

    mami "Qu’est-ce qu’il y’a ?"

    adamu "Ah non rien t’inquiètes pas, j’ai un peu mal au ventre je pense que c’était pas très frais ce qu’on a mangé ahah…"

    mami "Ah bon tu trouves ? Moi j’ai trouvé ça plutôt bon."

    adamu "D’ailleurs c’est quoi ton plat préféré ?"

    scene cafeteriaSchool with dissolve

    show adamuAngry with dissolve

    adamu "{i}Il faut que je trouve une explication à donner à Aya tout à l’heure ! Réfléchis…{/i}"

    scene cafeteriaSchool with dissolve

    show mamiSpeaking at left with dissolve

    mami "Tu m'écoutes Adamu ?"

    show adamuSorry at right with dissolve

    adamu "Ah oui désolé, j’ai la tête qui tourne un petit peu, ahah…"

    mami "Bon en vrai on a fini de manger de toute façon, si tu veux on peut…"

    show adamuSmileSchool at right

    adamu "On peut ?"

    show mamiBlush at left

    mami "On peut aller se balader pour digérer un peu, enfin si tu veux..."

    scene cafeteriaSchool with dissolve

    show adamuVeryHappy with hpunch

    adamu "{i}MA-SA-KA ! Ai-je bien entendu ce que j’ai entendu ?! On pensera à Aya plus tard pour le moment je pars en mission !{/i}"

    scene cafeteriaSchool with dissolve

    show adamuSorry at right with dissolve

    show mamiBlush at left with dissolve

    adamu "Ouais bien-sûr !"

    show cafeteriaSchool with dissolve

    scene black with dissolve

    "{i}Mami et Adamu marchèrent le temps de la digestion...{/i}"

    scene frontSchool with dissolve

    show adamuConfident at right with dissolve

    show mamiStoic at left with dissolve

    mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi"

    adamu "Ouais clairement ! On se refera ça hein ?"

    show mamiTaunt at left
    hide mamiStoic

    show adamuSorry at right
    hide adamuConfident

    mami "Si t'es sage peut-être"

    show mamiStoic at left
    hide mamiTaunt

    mami "Bon allez à plus !"

    scene frontSchool with dissolve

    show adamuAngry with dissolve

    adamu "{i}Qu’est-ce qu’elle voulait dire par être sage ?{/i}"
    adamu "{i}J’ai toujours été sage moi, je suis abonné à la sagesse carrément et ça me rend fou !{/i}"

    scene frontSchool with dissolve

    "{i}La sonnerie retentit, les cours ayant repris Adam se précipita vers la classe.{/i}"

    scene corridorsSchool with dissolve

    "{i}Il arriva en retard de 4 minutes au cours d’informatique dont la séance était dédiée au projet...{/i}"

    scene classroomSchool with dissolve

    show adamuConfident at right with dissolve

    adamu "Salut Aya !"

    show ayaCalm at left with dissolve

    aya "Ça va bien et toi ?"

    adamu "Super nickel à la plonge !"

    aya "..."

    show ayaBlushed at left

    aya "Tu mangeais avec quelqu'un ce midi ?"

    scene classroomSchool with dissolve

    show adamuAngry with dissolve

    adamu "{i}C’est bon, le top-départ a été lancé, il faut à tout prix que je la wombo-combo avec des disquettes.{/i}"
    adamu "{i}Je sais bien qu’elle ma surprit en flag’, c’est un piège mais elle ne m’aura pas comme ça !{/i}"
    adamu "{i}Après tout je suis l’ultime Ninja ayant sauvé l’opération plan H par le passé… Ahah si elle savait...{/i}"

    scene classroomSchool with dissolve

    show adamuSorry at right with dissolve
    show ayaBlushed at left with dissolve

    adamu "J’ai mangé avec une amie, on avait jamais eu le temps vu qu’on a pas le même planning, et toi ?"

    aya "Ah ouais c'est cool ça ! J’ai mangé avec des amies du lycée, à vrai dire je ne me suis pas vraiment fait d’amies à la fac..."

    adamu "Ah ouais pourtant tout le monde voudrait devenir ami avec une fille aussi mignonne ahah"

    show ayaBlushed2 at left

    aya "Arrête de dire des bêtises..."

    adamu "Ahah tu vois même quand je te dis la vérité tu me fais des reproches"

    aya "Mais c’était pas un reproche c’est toi qui..."

    scene classroomSchool with dissolve

    "{i}À ce moment tout se passait bien, l’opération de sauvetage miraculeux eut été une réussite.{/i}"
    "{i}Sans même mentir Adamu s’était tiré d’affaire. À vrai dire mentir provoque toujours des retombées.{/i}"

    show ayaBlushed at left with dissolve
    show adamuConfident at right with dissolve

    adamu "Et puis tu sais pas ce qu’il s’est passé à ce moment là..."

    scene msgClassMami with dissolve

    "{i}*Téléphone vibre*{/i}" with hpunch

    scene classroomSchool with dissolve

    show adamuAngry with dissolve

    adamu "{i}Bordel de pute pourquoi pourquoiiiiii !{/i}" with hpunch
    adamu "{i}Oh bordel je suis refait elle veut me voir, mais attends zebi y’a Aya juste devant moi qu’est-ce qui se passe !{/i}"
    adamu "{i}Je suis vraiment condamné, l’univers entier veut me voir échouer !{/i}"

    scene classroomSchool with dissolve

    show adamuSorry at right with dissolve
    show ayaCalm at left with dissolve

    aya "C’est ton amie de tout à l’heure ?"

    menu lie_aya:
        "Réponse:"
        "Euh ouais c’est elle qui veut me voir hein moi j’ai rien demandé et puis...":
            jump scene2_1_1
        "Non du tout ! C'est un ami qui m'a envoyé un drôle de message, t'es parano un peu ahah...":
            jump scene2_1_2
        





label scene2_1_1:

    scene classroomSchool
    show ayaHurt at left
    show adamuSorry at right
    
    aya "T’as pas à te justifier Adamu hein ? On est qu’ami tous les deux..."
    
    show adamuSorry2 at right
    hide adamuSorry2

    adamu "Ouais je sais mais c’est que..."
    adamu "{i}On m'a mit mal, je veux mourir.{/i}"

    show ayaCalm at left
    aya "Du coup pour le projet, je pense qu’il faudrait surtout utiliser cette libraire en python et..."

    scene classroomSchool with dissolve

    "{i}Finalement pendant toute l’heure restante ils n’auront discuté que du projet. Adamu est en train mauvaise posture. Mais ce qu’il s’apprêtait à voir en sortant de la salle était terrible...{/i}"

    show adamuSorry at right with dissolve
    show ayaCalm at left with dissolve

    adamu "D’ailleurs Aya est-ce que..."

    show ayaBlushed at left

    aya "Bon bah salut Adamu à la semaine prochaine !"

    show adamuSurprisedSchool at right

    adamu "Attends Aya !"

    aya "..."

    show ayaCry at left

    aya "Salut..."

    scene classroomSchool with dissolve

    "{i}Aya était en larme, elle parti en courant.{w} Toute la salle était abasourdie face à la scène, des murmures se faisaient entendre, rien de bon pour la réputation de notre Majin Boo national{/i}"

    scene black with dissolve

    "{i}Adamu, de retour chez lui. 23h34.{/i}"

    scene adamuRoom with dissolve

    show adamuChill with dissolve

    adamu "Bordel qu’est-ce qui se passe dans ma vie... Qu’est-ce que je fais pour Mami..."

    adamu "En plus elle veut qu'on se voit au parc, c'est pas à côté..."

    adamu "Arrrrgh ça sert à rien de réfléchir, je fais quoi du coup..."

    menu see_mami:
        "Que faire ?"
        "Voir Mami":
            jump scene2_1_1_1
        "Rester à la case pépouze la main dans le falzar":
            jump scene2_1_1_2
        

label scene2_1_1_1:
    scene adamuRoom
    show adamuChill
    adamu 'Bon let’s go on pensera à Aya plus tard, pour le moment je repars en mission.'

    show adamuChillJoy
    adamu "J’y serais jamais à temps à pied... {w} je dois aller chercher l’arme ancestrale qui a permis au rat originel de s’évader des égouts..."

    scene jitenshaVisu with dissolve

    adamu "Le légendaire « Jitensha à Drancy »."

    scene black with dissolve

    return

label scene2_1_1_2:
    scene adamuRoom
    show adamuChill

    adamu "Bon en vrai la flemme de la voir, c'est trop pour moi aujourd'hui... {w} Je vais tag une petite game et ensuite dodo."
    
    scene black with dissolve
    "{i}Fin de journée pour Adamu{i}"

    return

