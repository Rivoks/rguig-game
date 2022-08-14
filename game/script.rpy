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

    transform atldelay:
        alpha 0.0
        pause 5.0
        alpha 1.0

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

    image classroomExt:
        "background/env/classroom_ext.jpg"

    image classroomInt:
        "background/env/classroom_int.jpg"

    image streetEve:
        "background/env/street_classic_eve.jpg"

    image adamuHouseExt:
        "background/env/adamu_house_ext.jpg"

    image cafeteriaSchool:
        "background/env/cafetaria.png"
    
    image parkNightBench:
        "background/env/park_night_bench.png"

    image parkNight:
        "background/env/park_night.png"

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
    
    image adamuDiabolic:
        "characters/adamu/diabolic.png"
        zoom characterSize

    image adamuChillNoHead:
        "characters/adamu/chill_no_head.png"
        zoom characterSize
    
    image adamuCryingSchool:
        "characters/adamu/crying_school.png"
        zoom characterSize
    
    image adamuStoicOut:
        "characters/adamu/stoic_out.png"
        zoom characterSize

    image adamuCloseEyesOut:
        "characters/adamu/eyes_closed_out.png"
        zoom characterSize

    image adamuAngryOut:
        "characters/adamu/angry_out.png"
        zoom characterSize

    image adamuSmileOut:
        "characters/adamu/smile_out.png"
        zoom characterSize

    image adamuSmileOutAlt:
        "characters/adamu/smile_out_alt.png"
        zoom characterSize

    image adamuShyOut:
        "characters/adamu/shy_out.png"
        zoom characterSize

    image adamuShyOut2:
        "characters/adamu/shy_out2.png"
        zoom characterSize

    image adamuDiabolicOut:
        "characters/adamu/diabolic_out.png"
        zoom characterSize

    image adamuDiabolicOut2:
        "characters/adamu/diabolic_out2.png"
        zoom characterSize

    image adamuSorryOut:
        "characters/adamu/sorry_out.png"
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
    
    image ayaCuteAngry:
        "characters/aya/cute_angry.png"
        zoom characterSize

    image ayaLaugh:
        "characters/aya/laugh.png"
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

    image yoshida:
        "characters/yoshida/yoshida.png"
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
    
    image mamiStoicOut:
        "characters/mami/stoic_out.png"
        zoom characterSize

    image mamiShyOut:
        "characters/mami/shy_out.png"
        zoom characterSize
    
    image mamiShyOut2:
        "characters/mami/shy_out2.png"
        zoom characterSize
    
    image mamiShyEyesOpen:
        "characters/mami/shy_eyes_open.png"
        zoom characterSize

    image mamiSpeakingOut:
        "characters/mami/speaking_out.png"
        zoom characterSize

    image mamiShySurprisedOut:
        "characters/mami/shy_surprised_out.png"
        zoom characterSize

    image mamiShyHappyOut:
        "characters/mami/shy_happy_out.png"
        zoom characterSize



# The game starts here.

label start:

    jump scene4

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

    stop music fadeout 2.0 fadeout 1.0

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

    stop music fadeout 2.0 fadeout 0.5
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
    stop music fadeout 2.0
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

    adamu "Elle était pressée, c'est sûrement pour ça haha..."

    show adamuStun

    adamu "Enfin je crois..."

    hide adamuStun
    show adamuSorry

    adamu "Haha..."
    adamu "J'espère que je la reverrai, elle était vraiment mignonne..."

    show adamuSpeakingSerious

    stop music fadeout 2.0 fadeout 1.0

    adamu "Voilà la porte de l'amphi."

    play sound "audio/fx/door_open.mp3" volume 0.5

    show adamuConfident
    adamu "Tout commence ici."

    stop music fadeout 2.0
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
    stop music fadeout 2.0 fadeout 1.0
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

    stop music fadeout 2.0 fadeout 1.0
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
    stop music fadeout 2.0 fadeout 1.0

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
    
    stop music fadeout 2.0
    jump scene1



label scene1:
        scene classroomExt with dissolve
        play sound "audio/fx/school_ring.mp3" volume 0.2
        "{i}Lundi 5 septembre 2022, 8h03"
        play sound "audio/fx/classroom.mp3" volume 0.1 fadein 1.0

        show adamuSmileSchool with dissolve

        adamu "Voici ma classe..."
        adamu "On dirait que des groupes sont déjà formés."
        adamu "Ils doivent se déjà connaître."
        adamu "Voyons voir, au niveau des meufs..."

        show adamuSpeakingSerious

        "*Jette un rapide coup d'oeil*"
        adamu "..."

        show adamuAngry

        adamu "Ca recommence la putain de sa mère..."

        show adamuVeryAngry

        adamu "Y'a que des chinois 1m10 les bras levés comme en 2nd"
        "*Zieute*"

        show adamuAngry

        adamu "Aucun gros tarpé de lopessa à l'horizon."
        adamu "¯\_(ツ)_/¯"

        adamu "J'avais l'espoir d'être dans la même classe que Mami"
        adamu "Mes espoirs sont brisés."
        stop sound fadeout 3


        #Ajouter Ost
        scene classroomExt with dissolve
        play music "audio/ost/scattered_flowers.mp3" volume 0.1 loop fadein 1.0

        "{i}C'est alors qu'une sillouhette elancée se dessina devant lui."
        "{i}Contre toute attente, il reconnu une beauté innocente."
        "{i}Comment pourrait-il l'oublier."
        "{i}Ce jour-là l'humanité s'en est souvenue."

        show ayaSurprise with dissolve

        noname "Oh mais c'est toi !"


        "{i}À ce moment il comprit."
        "{i}Son instinct de PALM ne le trompait jamais: c’était ce qu’il appelait une « Hlel »."
        "{i}Une fille pudique, innocente et qui se retrouvait décontenancée en parlant avec un homme."

        scene classroomExt with dissolve

        show adamuSurprisedSchool at left with dissolve
        show ayaCalm at right with dissolve

        adamu "Salut, comment ça va depuis le temps ?"
        noname "Bien merci, au fait moi c'est Aya"
        aya "Aya Kataragi."
        adamu "Adam, enchanté."

        show adamuSmileSchool at left

        adamu "On est dans la même classe, c'est cool."
        adamu "J'espère qu'on va bien s'entendre"

        show ayaBlushed at right

        aya "Haha..."
        aya "Euh, le cours va commencer, allons-y Adam."

        play sound "audio/fx/door_open.mp3" volume 1.0
        stop sound

        scene classroomInt with dissolve
        show yoshida with dissolve



        "Yoshida" "Bonjour, je m'appelle Yoshida et je serai votre professeur principal pour ce semestre."
        "Rentrons dans le vif du sujet sans tarder."
        "Ce semestre, vous aurez un projet d'informatique à réaliser en binôme."
        "Le choix du binôme est libre, bien évidemment."

        hide yoshida with dissolve

        "{i}Alors que les groupes commencaient à se former et à discuter entre eux, la petite Aya semblait esseulée."

        show ayaCalm

        "{i}Adam ne resta pas insensible à la détresse d'Aya. Dès lors, il activa le mode « Bête de Guerre »."
        "{i}C'est avec un air confiant, presque sournois, qu'il s'approcha à pas de loup d'Aya."

        scene classroomInt with dissolve
        show adamuSmileSchool at left with dissolve
        show ayaCalm at right with dissolve

        adamu "Aya t'as un binôme pour le projet ?"

        show ayaBlushed at right
        aya "Ah, euh..."
        aya "Non.."
        adamu "Ecoute, on peut se mettre ensemble pour le projet si tu veux."
        aya "Hum..."

        show ayaBlushed2 at right

        aya "Ca ne te dérange pas que ce soit avec moi ?"
        adamu "Bien sûr que non"

        show ayaCalm at right
        aya "Merci, Adam."

        scene classroomInt with dissolve

        "{i}Le cours se termina et les élèves commencaient à rentrer chez eux."

        scene corridorsSchool with dissolve
        show adamuSmileSchool at left with dissolve
        show ayaBlushed at right with dissolve

        aya "Euh..."
        show ayaCalm at right
        aya "Merci pour aujourd'hui Adam, je me suis bien amusée."
        show adamuConfident at left

        adamu "Tout le plaisir est pour moi."
        aya "Au fait..."
        aya "Adam, c'est quoi ton snapuchatu ?"
        show adamuSurprisedSchool at left
        adamu "irongaren.euw, pourquoi ?"
        aya "C'est pour qu'on puisse échanger pour le projet."
        show adamuStun at left
        adamu "Ah oui, le projet bien sûr."

        "{i}Evidemment notre ventre-en-coeur ne l’entendit pas de cette oreille."
        "{i}Les dieux étaient avec lui, il savait que cette demande n'était pas anodine."

        show streetEve with dissolve
        stop music fadeout 2.0
        play music "audio/ost/hero.mp3" volume 0.1  fadein 1.0

        "{i}Sur le chemin du retour, Adamu remercia les cieux de la bonne fortune qui l’avait touché."
        "{i}Il ne pouvait attendre de rentrer chez lui et envoya le premier message à Aya et discutait de temps en temps avec Mami."
        "{i}Il se dit qu’il était enfin sur la voie légendaire de Maru Aruba, samouraï du passé et symbole de virilité pour notre héros."
        "{i}Ainsi se termina la rentrée de notre jeunot, il pouvait se reposer il l'avait bien mérité."

        scene black with dissolve

        "{i}Un jour Adamu proposa à Mami de déjeuner ensemble. Par chance cette dernière accepta la proposition{/i}"
        "{i}Ils se donnèrent rendez-vous le lendemain devant l'université. Que le sort puisse lui être favorable.{/i}"

        stop music


label scene2:

    scene frontSchool with dissolve

    play music "audio/ost/bwb_encounter.mp3" volume 0.1 loop fadein 1.0

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

    mami "Ton assiette est vachement équilibrée !"

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

    stop music fadeout 2.0

    mami "..."

    show adamuSurprisedSchool at right

    adamu "Mami-chan ?"

    play music "audio/ost/lone_sojourner.mp3" volume 0.3 loop fadein 1.0

    show mamiSpeaking at left

    mami "C’est rien t’inquiètes, je viens juste de sortir d’une longue relation c’est un peu compliqué du coup..."

    adamu "Ah excuses-moi... je... euh..."

    mami "Tu pouvais pas savoir t'inquiètes."

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

    stop music fadeout 2.0
    play sound "audio/fx/exclamation.mp3" volume 0.5

    "{i}Aya venait d'arriver au réfectoire du CROUS, elle suprend au loin Adamu en train de déjeuner avec Mami. Adam croisa son regard et l'évita aussitôt{/i}"

    scene cafeteriaSchool with dissolve

    show mamiBlush at left

    show adamuSorry at right

    play music "audio/ost/excited.mp3" volume 0.2 loop fadein 1.0

    play sound "audio/fx/collision.mp3"
    adamu "{i}Bordel de pute je suis cramé ! Aya voudra plus jamais me parler putain zebi…{/i}" with hpunch

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

    play sound "audio/fx/collision.mp3"
    show adamuVeryHappy with hpunch
    play sound "audio/fx/masaka.mp3" volume 1.5
    adamu "{i}MA-SA-KA ! Ai-je bien entendu ce que j’ai entendu ?! On pensera à Aya plus tard pour le moment je pars en mission !{/i}"

    scene cafeteriaSchool with dissolve

    show adamuSorry at right with dissolve

    show mamiBlush at left with dissolve

    adamu "Ouais bien-sûr !"

    show cafeteriaSchool with dissolve

    scene black with dissolve

    stop music fadeout 2.0

    "{i}Mami et Adamu marchèrent le temps de la digestion...{/i}"

    scene frontSchool with dissolve

    play music "audio/ost/happy_school.mp3" volume 0.3 fadein 2.0 loop

    show adamuConfident at right with dissolve

    show mamiStoic at left with dissolve

    mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi"

    adamu "Ouais clairement ! On se refera ça hein ?"

    show mamiTaunt at left
    hide mamiStoic

    show adamuSorry at right
    hide adamuConfident

    mami "Si t'es sage... Peut-être ?"

    show mamiStoic at left
    hide mamiTaunt

    mami "Bon allez à plus !"

    scene frontSchool with dissolve

    show adamuAngry with dissolve

    adamu "{i}Qu’est-ce qu’elle voulait dire par être sage ?{/i}"
    adamu "{i}J’ai toujours été sage moi, je suis abonné à la sagesse carrément et ça me rend fou !{/i}"

    scene frontSchool with dissolve

    stop music fadeout 2.0
    play sound "audio/fx/school_ring.mp3"
    play music "audio/ost/bwb_encounter.mp3" volume 0.3 fadein 2.0 loop


    "{i}La sonnerie retentit, les cours ayant repris Adam se précipita vers la classe.{/i}"

    scene corridorsSchool with dissolve

    "{i}Il arriva en retard de 4 minutes au cours d’informatique dont la séance était dédiée au projet...{/i}"

    play sound "audio/fx/classroom.mp3" volume 0.1 fadein 2.0
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
    play sound "audio/fx/swoosh1.mp3" volume 0.4
    stop music fadeout 1.0
    play music "audio/ost/papakatsu.mp3" volume 0.3 fadein 3.0 loop


    adamu "{i}C’est bon, le top-départ a été lancé, il faut à tout prix que je la wombo-combo avec des disquettes.{/i}"
    adamu "{i}Je sais bien qu’elle ma surprit en flag’, c’est un piège mais elle ne m’aura pas comme ça !{/i}"
    show adamuVeryHappy
    adamu "{i}Après tout je suis l’ultime Ninja ayant sauvé l’opération plan H par le passé… Ahah si elle savait...{/i}"

    scene classroomSchool with dissolve

    show adamuSorry at right with dissolve
    show ayaBlushed at left with dissolve

    adamu "J’ai mangé avec une amie, on avait jamais eu le temps vu qu’on a pas le même planning, et toi ?"

    aya "Ah ouais c'est cool ça ! J’ai mangé avec des amies du lycée, à vrai dire je ne me suis pas vraiment fait d’amies à la fac..."

    adamu "Ah ouais pourtant tout le monde voudrait devenir ami avec une fille aussi mignonne ahah"

    show ayaBlushed2 at left

    aya "Arrête de dire des bêtises..."

    adamu "Ahah tu vois même quand je te dis la vérité tu me fais des reproches !"

    aya "Mais c’était pas un reproche c’est toi qui..."

    scene classroomSchool with dissolve
    play sound "audio/fx/anime_wow.mp3" volume 0.3
    "{i}À ce moment tout se passait bien, l’opération de sauvetage miraculeux eut été une réussite.{/i}"
    "{i}Sans même mentir Adamu s’était tiré d’affaire. À vrai dire mentir provoque toujours des retombées.{/i}"

    show ayaBlushed at left with dissolve
    show adamuConfident at right with dissolve

    adamu "Et puis tu sais pas ce qu’il s’est passé à ce moment là..."

    scene msgClassMami with dissolve
    stop music
    play sound "audio/fx/collision.mp3" volume 1
    play music 'audio/ost/excited.mp3' volume 0.3 loop
    "{i}*Téléphone vibre*{/i}" with hpunch

    scene classroomSchool with dissolve

    show adamuAngry with dissolve
    play sound "audio/fx/collision.mp3" volume 1

    adamu "{i}Bordel de pute pourquoi pourquoiiiiii !{/i}" with hpunch
    adamu "{i}Oh bordel je suis refait elle veut me voir, mais attends zebi y’a Aya juste devant moi qu’est-ce qui se passe !{/i}"
    adamu "{i}Je suis vraiment condamné, l’univers entier veut me voir échouer !{/i}"

    scene classroomSchool with dissolve

    show adamuSorry at right with dissolve
    show ayaCalm at left with dissolve

    aya "C’est ton amie de tout à l’heure ?"

    menu lie_aya:
        "Répondre à Aya"
        "Euh ouais c’est elle qui veut me voir hein moi j’ai rien demandé et puis...":
            stop music
            jump scene2_1_1
        "Non du tout ! C'est un ami qui m'a envoyé un drôle de message, t'es parano un peu ahah...":
            stop music fadeout 3.0
            jump scene2_1_2
        
label scene2_2:

    show adamuStun at right

    adamu "Ouais je comprends..."

    mami "C'est la vie hein..."

    menu:
        "Répondre à Mami-chan:"
        "En tout cas si t'as un problème tu peux m'appeler n'hésites pas":
            scene cafeteriaSchool
            show adamuConfident at right
            show mamiBlush at left
            mami "Hum... vraiment ?"
            show adamuSmileSchool at right
            adamu "Mais ouais bien sûr !"
            show mamiTaunt at left
            mami "Bon bah t'as pas intérêt à revenir là dessus alors !"
            adamu "Je ne reviens jamais sur ma parole, tel est mon Nindô."
            show mamiStoic at left
            stop music fadeout 2.0
            mami "Cringe ?"
            show adamuSorry at right
            play music "audio/ost/happy_school.mp3" volume 0.3 loop fadein 1.0
            adamu "Vous voulez bien ?"
            scene frontSchool with dissolve
            show adamuConfident at right with dissolve
            show mamiStoic at left with dissolve
            mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi"
            adamu "Ouais clairement ! On se refera ça hein ?"
            show mamiTaunt at left
            hide mamiStoic
            show adamuSorry at right
            hide adamuConfident
            mami "Si t'es sage... peut-être ?"
            show mamiStoic at left
            hide mamiTaunt
            mami "Bon allez à plus !"
            scene black with dissolve
            scene corridorsSchool with dissolve
            show adamuSpeakingSerious with dissolve
            adamu "Allez c'est reparti pour les cours, en plus jusqu'à 18h00 aujourd'hui..."
            show adamuAngry
            adamu "Quelle vie de merde..."
            stop music fadeout 2.0
            scene msgClassMami with dissolve
            play sound "audio/fx/notification.mp3" volume 0.2
            "{i}* Téléphone vibre * {/i}" with hpunch
            play music "audio/ost/excited.mp3" volume 0.3 loop fadein 1.0
            scene corridorsSchool with dissolve
            show adamuVeryHappy with dissolve
            play sound "audio/fx/collision.mp3" volume 0.8
            adamu "NANIIIIIIIII ! MAIS QU'EST-CE QUE TU CACHES DERRIÈRE CE SOURIRE ADAMU !" with hpunch
            show adamuConfident
            adamu "Ça s'annonce bien pour moi, je réponderai plus tard à son message."
            show adamuStun
            adamu "Mais en vrai y'a aussi Aya, qu'est-ce que je dois faire ?"
            show adamuAngry
            adamu "Bon en vrai on verra ce soir, là je dois aller en cours."
            stop music fadeout 2.0
            jump scene2_mami_dm
        "...":
            scene cafeteriaSchool
            "{i}Le déjeuner se passa sans accrocs. {/i}"
            scene frontSchool with dissolve
            show adamuConfident at right with dissolve
            show mamiStoic at left with dissolve
            mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi"
            adamu "Ouais clairement ! On se refera ça hein ?"
            show adamuSorry at right
            hide adamuConfident
            mami "Euh ouais pourquoi pas..."
            mami "Bon allez à plus !"
            scene black with dissolve
            "{i}La journée se termina pour Adamu. Les jours passèrent sans nouvelles de Mami...{/i}"
            return
            # jump scene5
            
            
label scene2_1_1:

    scene classroomSchool
    show ayaHurt at left
    show adamuSorry at right
    
    aya "T’as pas à te justifier Adamu hein ? On est qu’ami tous les deux..."
    
    show adamuSorry2 at right
    hide adamuSorry2

    adamu "Ouais je sais mais c’est que..."
    scene classroomSchool with dissolve
    show adamuCryingSchool with dissolve
    play music "audio/ost/dramatic_kaguya.mp3" volume 0.2 loop 
    adamu "{i}On m'a mit mal, je veux mourir.{/i}"
    
    scene classroomSchool with dissolve
    show adamuSorry at right with dissolve
    show ayaCalm at left with dissolve
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

    jump scene2_mami_dm

label scene2_1_2:
    scene classroomSchool
    play music "audio/ost/flying_fairy.mp3" volume 0.2 fadein 2.0 loop
    show adamuSorry at right
    show ayaBlushed at left
    aya "Ah d'accord désolée je ne voulais pas rentrer dans tes affaires, c'est juste que..."
    show adamuConfident at right
    adamu "Que ?"
    show ayaBlushed2 at left
    aya "C'est juste que je vous trouvais vachement proches, mais si tu me dis que vous êtes amis..."
    show adamuSmileSchool at right
    adamu "Est-ce que tu ne me ferais pas une petite crise de jalousie là hein ?"
    show ayaCuteAngry at left
    aya "Non du tout tu dis n'importe quoi, comme d'habitude..."
    scene classroomSchool with dissolve
    "{i}Et leur petite scène de ménage continua. Ils étaient tellement mignons que beaucoup dans la salle pensaient à la formation même d'un couple à cet instant.{/i}"
    show adamuConfident at right with dissolve
    show ayaLaugh at left with dissolve
    adamu "Et c'est comme ça que ma mère m'a suprise sur Twitter en train de dire que j'allais niquer des daronnes !"
    aya "Ahah qu'est-ce que t'es bête Adamu !"
    scene classroomSchool with dissolve
    show adamuStun with dissolve
    stop music fadeout 2.0
    adamu "{i}Bon il faut que je me lance, c'est mon moment.{/i}"
    play music "audio/ost/love_dramatic.mp3" volume 0.3 loop
    play sound "audio/fx/collision.mp3" volume 1.0
    show adamuVeryHappy
    adamu "ALLEZ JE VAIS LUI PROPOSER UN DATE !" with hpunch
    scene classroomSchool with dissolve
    show adamuConfident at right with dissolve
    show ayaLaugh at left with dissolve
    aya "Et puis c'est là que je suis allé la première fois au karaoké de la ville, j'y étais jamais allée et c'est trop bien !"
    show adamuSmileSchool at right
    adamu "D'ailleurs Aya, ça te dirait de sortir en ville ce week-end ?"
    adamu "Tu pourras me montrer tes talents de chanteuse au karaoké par exemple !"
    show ayaBlushed at left
    aya "..."
    show ayaBlushed2 at left
    aya "Oui pourquoi pas c'est vrai que ce serait cool !"
    scene classroomSchool with dissolve
    show adamuVeryHappy with dissolve
    play sound "audio/fx/collision.mp3" volume 1.0
    play sound "audio/fx/pourquoi_pas.mp3" volume 0.7 fadeout 2.0
    adamu "LET'S GO ! BORDEL DE MERDE ! OUAIS POURQUOI PAS POURQUOI PAAAAAAAAAAAAS !!!" with hpunch
    hide adamuVeryHappy with dissolve
    "{i}À moment précis, Adamu commenceait à monter les saintes marches de la légende du P.A.L.M.{/i}"
    "{i}Un moment historique dans sa longue vie d'ermite croupissant dans les débris de sa chambre morose.{/i}"
    "{i}Il venait d'obtenir le premier date de toute sa vie. Plus rien ne sera comme avant. {/i}"
    "{i}Nom de code de l'opération: PLAN D(ate){/i}"
    scene black with dissolve
    stop music fadeout 2.0
    "{i}Les jours passèrent. {w} Le jour saint du date arriva.{w} Samedi 10 septembre. 11h33, Chature-Re-Haru.{/i}"
    # jump scene4
    return

        
label scene2_mami_dm:
    scene black with dissolve

    play music "audio/ost/papakatsu.mp3" volume 0.3 loop fadein 1.0

    "{i}Adamu, de retour chez lui. 23h34.{/i}"

    scene adamuRoom with dissolve

    show adamuChillNoHead with dissolve

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
    show adamuChillNoHead
    adamu 'Bon let’s go on pensera à Aya plus tard, pour le moment je repars en mission.'

    hide adamuChillNoHead
    show adamuSurprise
    stop music fadeout 2.0
    play sound "audio/fx/exclamation.mp3"
    adamu "Mais attends bordel... J’y serais jamais à temps à pied !"
    adamu "..."
    hide adamuSurprise
    show adamuDiabolic
    adamu "...{w} je dois aller chercher l’arme ancestrale qui a permis au rat originel de s’évader des égouts..."

    play music "audio/ost/very_stronger.mp3" volume 0.3 loop fadein 1.0


    scene jitenshaVisu with dissolve:
        xpos 0.85 ypos 1.0 xanchor 0.66 yanchor 0.93 zoom 1.5
        linear 5 yanchor 0.8
    
    pause 5.0
    scene jitenshaVisu with dissolve
    play sound 'audio/fx/anime_wow.mp3' volume 0.5
    adamu "Le légendaire « Jitensha à Drancy »."
    scene jitenshaVisu
    pause 5.0
    scene black with dissolve

    return

label scene2_1_1_2:
    scene adamuRoom
    show adamuChill

    adamu "Bon en vrai la flemme de la voir, c'est trop pour moi aujourd'hui... {w} Je vais tag une petite game et ensuite dodo."
    
    scene black with dissolve
    "{i}Fin de journée pour Adamu{i}"

    # Jump scene 5
    return

label scene4:
    scene parkNight with dissolve
    play music "audio/ost/lone_sojourner.mp3" fadein 2.0 volume 0.2 loop
    show adamuStoicOut with dissolve
    adamu "Bon je suis devant le parc... Faut que je reste calme."
    adamu "Mami m'attends à l'autre bout au niveau du lac, juste après le Pont Iris."
    hide adamuStoicOut
    show adamuCloseEyesOut
    adamu "C'est donc ici que tout commence pour moi..."
    adamu "Calme toi Adamu... calme toi ça va bien se passer..."
    adamu "..."
    hide adamuCloseEyesOut
    show adamuAngryOut
    play sound "audio/fx/collision.mp3" volume 0.8
    adamu "PUTAIN POURQUOI J'AI LE BARREAU MAINTENANT !" with hpunch
    hide adamuAngryOut
    show adamuCloseEyesOut
    adamu "Bon ça sert à rien de stresser de toute façon."
    adamu "..."
    adamu "C'est donc ça la sensation..."
    show adamuStoicOut
    adamu "Cette sensation que le rat originel avait lorsqu'il fut le premier à s'évader ?"
    stop music fadeout 2.0
    adamu "On y va let's go, que la bénédiction des rats soit sur moi ce soir..."
    scene black with dissolve
    play music "audio/ost/love_dramatic.mp3" fadein 2.5 volume 0.2 loop
    "{i}Adamu traversa le parc pour rejoindre Mami qui l'attendait à l'autre bout.{/i}"
    "{i}Que va-t-il advenir à notre héro au ventre-en-cœur ?{/i}"
    "{i}Nous le saurons dans un instant, juste après la pub.{/i}"
    "{i}Est-ce que vous avez déjà entendu parler de Nord VPN ?{/i}"
    "{i}Et bien en réalité vous pouvez vous connecter{w}... Non je déconne on a pas le temps pour ces conneries.{/i}"
    "{i}Avoue que tu y a cru petit batard hein ?{/i}"
    "{i}Allez c'était le Highlight du narrateur, désormais place à l'aventure de notre Rguig National.{/i}"
    stop music fadeout 2.0
    scene parkNightBench with dissolve
    show adamuSmileOut at right with dissolve
    show mamiStoicOut at left with dissolve
    play music "audio/ost/papakatsu.mp3" fadein 2.0 volume 0.2 loop
    adamu "Salut ahah..."
    mami "Finalement tu as fini par venir."
    adamu "Ah ouais désolé mon vélo a crevé sur le chemin, encore ces satanés corbeaux ahah..."
    mami "..."
    show mamiShyOut at left
    mami "Pouquoi t'es venu finalement ?"
    adamu "Bah j'allais pas laisser une fille seule dans la nuit et puis..."
    show adamuSmileOutAlt at right
    adamu "Et puis tu avais visiblement quelque chose à me dire donc je suis là."
    mami "..."
    hide mamiShyOut 
    show mamiShyOut2 at left
    mami "Bon voilà j'avais simplement besoin de parler un petit peu."
    mami "En vrai je sais pas pourquoi je t'ai demandé de se voir..."
    mami "On aurait pu en parler par téléphone et puis..."
    show adamuStoicOut at right
    adamu "Dis moi qu'est-ce qui ne va pas Mami."
    adamu "Je te l'ai dis, en cas de problème je serais toujours là pour toi."
    show mamiShyEyesOpen at left
    mami "..."
    mami "Comme tu le sais je suis nouvelle dans la ville, je me suis fait plein d'amis et je commence à me faire à cette nouvelle vie"
    show mamiSpeakingOut at left
    mami "Tout semble bien aller mais je ne sais pas..."
    mami "C'est comme s'il manquait une pièce dans le puzzle..."
    scene parkNightBench with dissolve
    show adamuStoicOut with dissolve
    adamu "{i}La pièce manquante du puzzle...{/i}"
    show adamuAngryOut 
    play sound "audio/fx/collision.mp3" volume 0.8
    adamu "{i}MAIS JE RECONNAIS, CETTE PIÈCE DU PUZZLE C'EST MON GIGA-CHIBRAX LVL. 100 DONT ELLE VEUT PARLER !!!{/i}" with hpunch
    hide adamuAngryOut
    adamu "{i}Bon calme toi Adamu, c'est potentiellement l'occasion du siècle qui se présente devant toi.{/i}"
    adamu "{i}Fais pas le con.{/i}"
    scene parkNightBench with dissolve
    show adamuSmileOut at right with dissolve
    show mamiShyOut2 at left with dissolve
    adamu "Qu'est-ce que tu veux dire par pièce manquante du puzzle ?"
    mami "..."
    show mamiShyOut at left
    mami "Bah je trouve qu'on s'entend plutôt bien et puis... je sais pas..."
    stop music fadeout 2.0
    menu:
        "Que faire ?"
        "Fuuton: Rasen-Disketu géant":
            scene parkNightBench
            show mamiShyOut at left
            show adamuSmileOutAlt at right
            adamu "Bah pour être honnête avec toi moi aussi j'apprécie beaucoup notre relation, et puis..."
            show mamiShyEyesOpen at left
            play music "audio/ost/excited.mp3" fadein 2.0 volume 0.1 loop
            mami "Et puis ?"
            adamu "Bah franchement tu me plais, tant physiquement mais surtout, surtout ta personnalité."
            adamu "T'es une fille discrète, très tendre et surtout ton regard..."
            show adamuShyOut at right
            adamu "Ahah je sais pas pourquoi je te dis ça, c'est complètement bizarre hein ?"
            hide mamiShyOut2
            show mamiShyOut at left
            mami "..."
            show adamuSorryOut at right
            adamu "Mami-chan ?"
            hide mamiShyOut
            show mamiShyOut2 at left
            mami "T'es vraiment sérieux quand tu dis ça ?"
            scene parkNightBench
            show mamiShyOut2 at left
            show adamuSmileOutAlt at right
            adamu "Bah ouais bien sûr ! Et puis c'est pas tout genre avec toi je peux dire n'importe quoi je me sens vraiment à l'aise."
            mami "..."
            scene parkNightBench with dissolve
            show adamuDiabolicOut with dissolve
            adamu "{i}Bon il est l'heure de claquer l'ulti...{/i}"
            adamu "{i}C'est pour tous mes rats enfermés que je le fais...{/i}"
            stop music fadeout 2.0
            adamu "{i}Pour Mimi...{/i}"
            play sound "audio/fx/extension.mp3" volume 0.8
            show adamuDiabolicOut2
            adamu "{i}EXTENSION DU TERRITOIRE: PRÉPUS DES ÉGOUTS !!!{/i}" with vpunch
            play sound "audio/fx/flashback.mp3" volume 0.3
            scene parkNightBench with flash
            show adamuShyOut at right with dissolve
            show mamiShyOut2 at left with dissolve
            play music "audio/ost/flying_fairy.mp3" volume 0.2 loop
            adamu "Dis Mami, je sais que c'est un peu soudain mais j'arrive plus à garder ça pour moi..."
            mami "..."
            play sound "audio/fx/breathing.mp3" volume 0.3
            adamu "Est-ce que ça te dirait de ..."
            adamu "De..."
            adamu "..."
            show adamuShyOut2 at right
            play sound "audio/fx/anime_wow.mp3" volume 0.2
            adamu "Est-ce ça te dirait d'être ma petite copine ?"
            mami "..."
            show mamiShySurprisedOut at left
            mami "Vraiment ?"
            adamu "Vraiment, je n'ai de yeux que pour toi Mami-chan."
            adamu "T'es ma Mami-chan !"
            mami "..."
            mami "Hum..."
            show mamiShyHappyOut at left
            mami "Dans ce cas tu seras mon Adamu-kun..."
            show adamuShyOut at right
            adamu "..."
            scene parkNightBench with dissolve
            show adamuDiabolicOut2 with dissolve
            play music "audio/ost/confess_kaguya.mp3" volume 0.2 loop
            play sound "audio/fx/pavard.mp3" volume 0.5
            adamu "{i}SECOND POTO ADAAAAAAAAAAAAAAAAAAM !!!{/i}" with hpunch
            play sound "audio/fx/bordel.mp3" volume 0.5
            adamu "{i}BORDEL DE MERDE JE L'AI FAIT BORDEL !!!!{/i}"
            adamu "{i}JE L'AI FAIT BORDEL !!!!{/i}"
            hide adamuDiabolicOut2
            show adamuDiabolicOut
            adamu "{i}JE ME SUIS ENFIN ÉVADÉ DES ÉGOUTS JE L'AI FAIT !!!{/i}"
            show adamuDiabolicOut2
            play sound "audio/fx/arigato.mp3" volume 0.1
            adamu "{i}MERCI À TOUS CEUX QUI ONT TOUJOURS CRU EN MOI !!!{/i}"
            scene parkNightBench with dissolve
            show adamuSmileOutAlt at right with dissolve
            show mamiShyOut2 at left with dissolve
            adamu "Putain tu sais pas comme je suis content !"
            show mamiShyHappyOut at left
            mami "Je vois ça tu fais une tête trop drôle depuis tout à l'heure."
            show adamuShyOut2 at right
            adamu "J'arrive pas à cacher ma joie ahah..."
            show mamiSpeakingOut at left
            mami "Bon il se fait tard je pense que je vais rentrer..."
            menu: 
                "Supplément boursin ?"
                "Oui":
                    show adamuSmileOut at right
                    adamu "Bon bah je te raccompagnes chez toi quand même !"
                "Non (t'es un enfoiré)":
                    show adamuSmileOut at right
                    adamu "Bon bah dans ce cas on se dit à demain..."
                    mami "..."
                    show mamiShyOut at left
                    mami "Tu veux pas même pas raccompagner ta meuf ?"
                    hide adamuSmileOut
                    adamu "Euh ouais bien sûr je savais pas si tu voulais... en fait... c'est que..."

            scene parkNightBench with dissolve
            "{i}C'est sur ces belles paroles que notre ancien déchet de la société venait de réaliser l'impensable.{/i}"
            "{i}Ce jour là, l'humanité s'en est souvenu.{/i}"
            "{i}Sa beu-teu aussi.{/i}"
            "{i}Il venait de s'évader des égouts. Désormais plus rien ne sera comme avant.{/i}"
            "{i}Laissant derrière lui nombre de rats condamnés à errer dans les bas-fonds, sans aucun espoir, sans aucune lueur.{/i}"
            "{i}C'était justement pour tout ces malheureux qu'Adamu avait prit son courage à deux main.{/i}"
            "{i}Il se devait de le faire, par respect pour ses semblables bannis.{/i}"
            "{i}Ainsi commençait sa nouvelle vie d'homme heureux, au côté de sa belle et douce dulciné.{/i}"
            stop music
            return

        "Fuite":
            scene parkNightBench
            show adamuSmileOutAlt at right
            show mamiStoicOut at left
            adamu "Ouais carrément t'es vraiment une camarade de classe sympa !"
            mami "Ah ouais tu trouves... ouais en vrai c'est ça..."
            scene parkNightBench with dissolve
            play music "audio/ost/dramatic_kaguya.mp3" volume 0.3 loop
            "{i}Quelle erreur.{/i}"
            "{i}À cet instant précis, Adamu ne le savait pas. Il venait de commettre l'irréparable.{/i}"
            "{i}Leur rendez-vous nocturne se termina assez rapidement. Mami pretextant avoir à faire chez elle.{/i}"
            "{i}En rentrant chez lui, Adamu se rendit compte que Mami était en 'gris' sur Sunapuchattu.{/i}"
            "{i}Il comprit à ce moment. En l'espace d'une journée il venait de perdre Aya et Mami.{/i}"
            "{i}Finalement, comme on dit dans les égouts: l'espoir n'accorde qu'une simple danse aux rats.{/i}"
            "{i}Il fallait désormais repartir de zéro. Il aurait fallut un miracle pour tirer notre individu de cette situation.{/i}"
            "{i}Et les miracles, {w} s'arrêtent à la porte du condamné.{/i}"
            stop music
            return
            
        
    
