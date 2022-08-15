# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define adamu = Character("Adamu", color="#ce2806")
define mami = Character("Mami", color="#ce06a4")
define aya = Character("Aya", color="#06ce67")
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

    image classroomExt:
        "background/env/classroom_ext.jpg"

    image classroomInt:
        "background/env/classroom_int.jpg"

    image streetDay:
        "background/env/street_classic_day.jpg"

    image streetEve:
        "background/env/street_classic_eve.jpg"

    image adamuHouseExt:
        "background/env/adamu_house_ext.jpg"

    image trainStation:
        "background/env/train_station.png"

    image trainInt:
        "background/env/train_int.png"

    image ebisuStation:
        "background/env/ebisu_station.png"

    image ebisuBar:
        "background/env/ebisu_bar.jpg"

    image ebisuConcert:
        "background/env/ebisu_concert.jpg"

    image ebisuStreetNight:
        "background/env/ebisu_street_night.png"


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

    image mamiAsking:
        "characters/mami/asking.png"
        zoom characterSize

    image mamiBlush:
        "characters/mami/blush.png"
        zoom characterSize

    image yoshida:
        "characters/yoshida/yoshida.png"
        zoom characterSize

# The game starts here.



label start:
    jump scene3

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
    "{i} TO BE CONTINUED..."

    stop music

    jump scene1


    label scene1:
        scene classroomExt with dissolve
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

        adamu "J'avais l'espoir d'être dans la même classe que Mami"
        adamu "Mes espoirs sont brisés."
        stop sound fadeout 3


        #Ajouter Ost
        scene classroomExt with dissolve
        play music "audio/ost/scattered_flowers.mp3" volume 0.1 loop fadein 1.0

        "{i}C'est alors qu'une sillouhette elancée se dessina devant lui."
        "{i}Contre toute attente, il reconnu une beauté innoncente."
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

        $RelationAya = 0
        $proposeDate = False


        menu:
            "Est-ce le bon moment pour proposer un date à Aya ?"
            "Oui":
                $proposeDate = True
                $scoreAya += 10
                scene corridorsSchool
                show ayaCalm at right
                show adamuSmileSchool at left
                adamu "Aya, t'es libre demain après-midi ?"
                show ayaSurprise at right
                aya "Oui je n'ai rien de prévu, pourquoi ?"
                adamu "Parfait, demain est une belle journée. Autant en profiter."
                adamu "Ca te dirait de se promener ensemble dans le quartier ? Je connais un coin sympa."
                hide ayaSurprise
                aya "C'est une bonne idée, on se voit demain alors"
                adamu "Ca marche, rentre bien."
                aya "Toi aussi, salut !"

                stop music


                show streetEve with dissolve
                play music "audio/ost/hero.mp3" volume 0.1  fadein 1.0

                "{i}Sur le chemin du retour, Adamu remercia les cieux de la bonne fortune qui l’avait touché."
                "{i}Enfin, il commencait à arpenter la voie légendaire de Maru Arufa, samouraï du passé et symbole de virilité pour notre héros."
                "{i}Ainsi se termina la rentrée de notre jeunot, il pouvait se reposer il l'avait bien mérité."

                stop music

                #jump to scene3 (date)

            "Non":
                show adamuConfident at left
                adamu "Dis Aya, t'es dis..."
                show ayaCalm at right
                aya "?"
                show adamuSorry at left
                adamu "Hum, non rien..."
                adamu "{i}Putain j'ai encore foiré."
                aya "Bon, je vais y aller. Rentre bien Adam !"
                show adamuSmileSchool
                adamu "Ca marche Aya, passe un bon week-end, à lundi !"

                stop music

                scene black with dissolve
                "{i}Chambre d'Adam, 19h07"

                scene adamu_room with dissolve

                play music "audio/ost/violet_sky.mp3" volume 0.1 loop fadein 1.0

                show adamuChill with dissolve
                adamu "Je suis enfin rentré, je suis crevé..."
                adamu "La journée s'est bien passée dans l'ensemble, je suis sur la bonne voie."
                adamu "J'aurais dû demander à Aya pour demain."
                adamu "Tant pis, j'aurais d'autres occasions..."
                adamu "Allez, une petite branlette et au lit."
                adamu "Non je déconne, c'est fini ces conneries."

                play sound "audio/fx/notification.mp3" volume 0.2

                "{i}*Vous avez reçu un nouveau message de Mami*{/i}"

                show adamuSurprise
                adamu "Hein ? Mami ?"
                adamu "Elle me propose de manger ensemble au CROUS lundi à midi !"
                adamu "Mais je m'entends bien avec Aya maintenant..."

                $scoreMami = 0

                menu:
                    adamu "Que faire ?"
                    "Accepter de manger avec Mami":
                        $scoreMami += 3
                        show adamuChillJoy
                        adamu "Je ne laisserai pas passer ma chance cette fois-ci"
                        adamu "Un tête à tête avec une Basic White Bitch, le pied !"
                        adamu "J'ai hâte d'être lundi"



                        #jump to scene 2 (CROUS w/ Mami)

                    "Refuser et prétexter une excuse":
                        $scoreMami -= 5
                        show adamuSleeping
                        adamu "Je dois rester fort."
                        adamu "Même si j'en ai terriblement envie, maintenant que je me suis rapproché d'Aya je ne peux pas accepter."
                        adamu "Je suis conscient de mes défauts."
                        adamu "Je suis un mauvais menteur, ça finira par se savoir tôt ou tard..."
                        adamu "Ne prenons pas de risques inutiles."

                        play sound "audio/fx/notification.mp3" volume 0.2
                        "{i}*Aya vous a envoyé un message !*"

                        hide adamuSleeping
                        show adamuSurprise
                        adamu "Un message d'Aya ! Je ne m'y attendais pas"
                        adamu "Elle me remercie pour la journée. Elle a dit que c'est la première fois qu'elle se sent aussi à l'aise avec un garçon !"

                        menu:
                            "{i}Dois-je répondre à Aya maintenant ?"

                            "Oui, tout de suite !":
                                show adamuChillJoy
                                adamu "Voilà, c'est fait !"
                                $scoreAya += 7
                                adamu "Bon là, je dois rectifier le tir."

                                menu:
                                    "{i} Proposer un date à Aya ?"

                                    "Oui, je n'ai rien à perdre !":
                                        $scoreAya += 7
                                        adamu "Elle a dit que c'était la première fois qu'elle se sentait aussi à l'aise avec un garçon"
                                        adamu "C'est un appel de phare, ne pas prendre les devants serait du int !"
                                        adamu "Tac tac tac, tac tac tac !"
                                        adamu "C'est envoyé ! C'est qui le gros baiseur ?"
                                        adamu "Bah je crois bien que c'est bibi !"

                                        #jump to scene 3


                                    "Non, c'est encore trop tôt !":
                                        show adamuChill
                                        adamu "Mieux vaut ne pas se presser avec les filles timides"
                                        show adamuChillJoy
                                        adamu "J'ai fait le bon choix, c'est sûr !"

                                        #jump to scene 5

                            "Non, attendre un peu. " :
                                show adamuChill
                                adamu "D'apres les estimations, il faut attendre au moins 2h avant de répondre pour montrer qu'on est occupé et suciter l'envie."
                                show adamuChillJoy
                                adamu "Je vais me lancer un petit Star Wars et je lui répondrai après."
                                adamu "Ikuzo !"

                                play music "audio/ost/star_wars_op.mp3" volume 0.1 fadein 1.0
                                "{i}*Regarde un épisode d'Obi-Wan Kenobi*"
                                show adamuChillJoy
                                adamu "Tin tin tin !"
                                hide adamuChillJoy
                                show adamuSurprise
                                adamu "Waaaah"
                                hide adamuSurprise
                                show adamuChillJoy
                                adamu "Ololo c'est trop !"
                                hide adamuChillJoy
                                show adamuChill
                                adamu "..."
                                hide adamuChill
                                show adamuChillJoy
                                adamu "Let's go !"
                                hide adamuChillJoy
                                show adamuChill
                                adamu "..."
                                hide adamuChill
                                show adamuSleeping
                                adamu "..."
                                hide adamuSleeping
                                show adamuSurprise
                                adamu "Waah, j'ai eu peur, la pute !"
                                hide adamuSurprise
                                show adamuChill
                                adamu "..."
                                hide adamuChill
                                show adamuSleeping
                                adamu "..."
                                hide adamuSleeping

                                scene black with dissolve

                                stop music

                                show adamuSleeping with dissolve
                                adamu "Aya..."
                                hide adamuSleeping
                                show adamuSurprise
                                adamu "Merde je me suis assoupi. Il est quelle heure ?"
                                adamu "Quoi ?!"
                                adamu "C'est déjà le matin ! J'ai pas répondu au message d'Aya et je l'ai laissée en vu !"
                                $RelationAya -= 5

                                scene black with dissolve


                                stop music

                                #jump to scene 5


    label scene3:

        play music "audio/ost/train_station.mp3" volume 0.1

        "{i}Le lendemain..."
        "{i}Le jour tant attendu arriva."
        "{i}Pour une fois, notre Adamu était en avance."
        "{i}Oui vous ne rêvez pas, le même Adamu qui ne s'était pas réveillé le jour de son concours blanc de PACES."

        show trainStation with dissolve

        "{i}Gare de Mommenrency, 11h07."

        show adamuConfident with dissolve

        adamu "Parfum, yes. "
        adamu "Chewing-gum c'est bon."
        adamu "Capote, ok."

        hide adamuConfident

        show adamuSpeakingSerious
        play sound "audio/fx/breathing.mp3" volume 0.2
        "{i}Respire..."
        "{i}Ca va bien se passer, allez ! Je me suis entrainé à sourire."

        hide adamuSpeakingSerious

        show adamuSmileSchool

        adamu "Tu veux que je te finisse ?"

        scene black

        play sound "audio/fx/flashback.mp3" volume 0.2

        adamu "Argh..."
        adamu "J'ai les paupières qui sautent."
        adamu "On dirait que j'ai un peu trop forcé cette nuit..."
        adamu "Ah, le train arrive super !"

        play sound "audio/fx/train_doors.mp3" volume 0.2

        stop music fadeout 0.5

        show trainInt with dissolve

        play music "audio/ost/train_int.mp3" volume 0.1

        adamu "Y'a personne dans le métro, trop cool !"
        adamu "C'est donc ça la yes life ?"
        adamu "Maintenant que j'y pense, ça a dû être difficile pour Aya cette rentrée."
        adamu "Elle habite loin d'ici..."
        adamu "Il faut que j'assure aujourd'hui, je dois être pixel."
        adamu "En mode 1v9, en mode gros saixeur."
        adamu "Le trajet va être long, pute de pute."
        adamu "Je vais faire un petit somme moi."

        stop music fadeout 0.5

        scene black

        play sound "audio/fx/ebisu_station.mp3" volume 0.2

        adamu "..."
        adamu "Oh..."
        adamu "*Pète*"
        adamu "..."
        adamu "Oui."
        adamu "Hmm"

        scene train_int with dissolve

        show adamuSurprisedSchool with dissolve
        adamu "Wah sa grand mère !"
        hide adamuSurprisedSchool
        show adamuStun
        adamu "C'est quoi cette voix, on dirait le freestyle du pédophile"
        hide adamuStun
        show adamuAngry
        play sound "audio/fx/train_doors.mp3" volume 0.2
        adamu "Bref, m'enfous."
        hide adamuAngry
        show adamuSmileSchool
        adamu "Le principal c'est que je sois arrivé"
        adamu "Ikuzo mina !"
        hide adamuSmileSchool

        scene black with dissolve

        show ebisuStation with dissolve
        play music "audio/ost/peaceful_day.mp3" volume 0.2

        show adamuSmileSchool at left with dissolve
        adamu "Salut Aya !"
        show ayaCalm at right with dissolve
        aya "Hey, tu as fait bonne route ?"
        hide adamuSmileSchool
        show adamuSorry at left
        adamu "Ouais, plus ou moins."
        hide adamuSorry
        show adamuSmileSchool at left
        adamu "En tout cas ça a l'air sympa par ici."
        aya "Oui, ça change de l'école."
        hide adamuSmileSchool
        show adamuSurprisedSchool at left
        adamu "Mais au fait, comment tu fais pour aller en cours ? Tu fais le trajet tous les jours ?"
        hide ayaCalm
        show ayaSorry at right
        aya "Bien sûr que non, c'est bien trop loin !"
        hide ayaSorry
        show ayaCalm at right
        aya "Je suis chez ma tante la semaine, et je rentre chez moi les week-end."
        hide adamuSurprisedSchool
        show adamuSorry at left
        adamu "Ah ouais, j'suis con..."
        hide adamuSorry
        show adamuSpeakingSerious at left
        adamu "Mais pourquoi m'avoir demandé de venir jusqu'ici au fait ?"
        hide ayaCalm
        show ayaSurprise at right
        aya "Ah !"
        hide adamuSpeakingSerious
        show adamuSmileSchool at left
        adamu "Pas besoin de te déranger pour moi, tu sais."
        hide ayaSurprise
        show ayaSorry at right
        aya "C'est que..."
        hide adamuSmileSchool
        show adamuStun at left
        adamu "Que ?"
        show ayaBlushed at right
        aya "Que je voulais te faire découvrir cet endroit !"
        hide adamuStun
        show adamuSurprisedSchool at left
        adamu "..."
        hide ayaBlushed
        show ayaCalm at right
        aya "Bon et si on allait un manger un bout ?"
        aya "Je connais un coin sympa."
        hide adamuSurprisedSchool
        show adamuSmileSchool at left
        adamu "Avec plaisir !"

        stop music fadeout 0.5

        scene black with dissolve

        show ebisuBar with dissolve
        play music "audio/ost/jazz_bar.mp3" volume 0.1 loop fadein 1.0

        show adamuSorry at left with dissolve
        adamu "{i}Arf j'ai mal au ventre, j'ai trop mangé..."
        hide adamuSorry
        show adamuSmileSchool at left
        adamu "Merci pour la découverte Aya, c'était bien bon."
        show ayaCalm at right with dissolve
        aya "Je t'en prie, ça me fait plaisir de partager ce moment ensemble."


        aya "Mais dis-moi Adam au fait..."
        $scoreAya3 = 0

        menu:
            aya "Tu as déjà eu une copine ?"
            "Oui mais c'est du passé.":
                $scoreAya3 -= 2
                hide adamuSmileSchool
                show adamuStun at left
                adamu "C'était y'a longtemps, j'étais jeune et naïf, puis ça s'est mal fini..."
                hide ayaCalm
                show ayaSorry at right
                aya "Ah..."
            "Euh non, jamais...":
                $scoreAya3 += 10
                hide adamuSmileSchool
                show adamuStun at left
                adamu "Hum, je n'ai jamais eu de copine."
                hide ayaCalm
                show ayaSorry at right
                aya "A vrai dire, moi non plus je n'ai jamais eu de copain..."
                hide adamuStun
                show adamuSurprisedSchool at left
                adamu "{i}QUOI ?!"
                menu:
                    aya "Et y'a quelqu'un qui te plaît en ce moment ?"
                    "Ouais, c'est possible...":
                        $scoreAya3 -= 10
                        hide adamuSurprise
                        show adamuStun at left
                        adamu "{i}Argh, je vais mourir de honte..."
                        hide ayaCalm
                        show ayaSurprise at right
                        aya "Ah bon, je ne m'en serai pas douté."
                    "Non, je n'ai pas la tête à ça.":
                        $scoreAya3 += 10
                        hide adamuStun
                        show adamuSpeakingSerious at left
                        adamu "Tu sais avec les cours et tout ça... J'ai plus trop le temps d'y penser finalement."
                        hide ayaSurprise
                        show ayaCalm at right
                        adamu "Et puis j'ai l'impression que la plupart des filles sont trop superficielles..."
                        aya "Hum je comprends ton point de vue, c'est intéressant."

        show ebisuBar
        show ayaSurprise at right
        aya "Oh mais il est déjà 17h !"
        aya "Je n'ai pas vu le temps passer."
        show adamuConfident at left
        adamu "C'est grâce à moi ça héhé !"
        hide ayaSurprise
        show ayaBlushed at right
        aya "N'importe quoi..."
        hide ayaBlushed
        show ayaCalm at right
        aya "Bon on doit se dépêcher pour aller voir le concert d'Airi ! "
        aya "Tu avais promis de m'accompagner, tu t'en souviens ?"
        hide adamuConfident
        show adamuStun at left
        adamu "{i} Ah bon j'ai dis ça moi ?"
        hide adamuStun
        show adamuSorry at left
        adamu "Bien sûr que je m'en souviens, pour qui tu me prends voyons !"
        aya "Parfait, c'est parti !"

        stop music

        scene black with dissolve

        play music "audio/ost/rock_concert.mp3" volume 0.2 loop

        show ebisuConcert with dissolve

        show adamuSpeakingSerious at left with dissolve

        adamu "{i}Plus je regarde Aya, plus je la trouve vraiment mignonne..."
        show ayaCalm at right with dissolve
        adamu "{i}Elle chante vraiment à fond, elle est tellement belle quand elle sourit..."
        hide adamuSpeakingSerious
        show adamuConfident at left
        adamu "{i} Merci Kami sama de m'avoir fait vivre jusqu'à ce jour béni !"
        hide adamuConfident
        show adamuStun at left
        adamu "Tu sais Aya, par rapport à tout à l'heure..."
        hide ayaCalm
        show ayaSurprise at right
        aya "Oui ?"

        menu:
            adamu "En fait je voulais te dire..."
            "Tu me plais et j'ai envie d'apprendre à te connaître davantage.":
                hide ayaSurprise
                show ayaBlushed2 at right
                hide adamuStun
                show adamuSorry at left
                adamu "{i}Purée je l'ai vraiment dit !"
                aya "Kya !"
                aya "Tu ne te moques pas de moi ?"
                hide adamuSorry
                show adamuSpeakingSerious at left
                adamu "Bien sûr que non ! Je suis sérieux Aya, tu me plais vraiment !"
                hide ayaBlushed2
                show ayaBlushed at right
                aya "Merci Adam, ça me touche beaucoup..."
                aya "Moi aussi j'aimerais approfondir notre relation !"
                #Score d'Aya ++ --> Condition avec un booléen +5 ou + 15 s'il l'a fait galérer au restau
            "Ah zut j'ai oublié ce que je voulais dire...":
                hide adamuStun
                show adamuSorry at left
                adamu "Euh, j'ai oublié..."
                aya "Ah bon ?"
                hide ayaSurprise
                show ayaCalm at right
                aya "Ca ne devait pas être important alors."
                adamu "Sûrement, oui."


        stop music fadeout 0.5

        scene black with dissolve

        "{i}Plus tard dans la nuit, une fois le concert fini."

        show ebisuStreetNight with dissolve

        play music "audio/ost/bye_feelings.mp3" volume 0.1 loop

        show adamuSmileSchool at left with dissolve
        show ayaCalm at right with dissolve

        adamu "C'était vraiment cool aujourd'hui, je me suis bien amusé !"
        aya "Oui, moi aussi ! Merci Adam c'est grâce à toi."
        aya "Alors, c'est l'heure de se dire au revoir."
        adamu "On se voit à l'école ne t'en fais pas."
        hide ayaCalm
        show ayaSorry at right
        aya "Ca va être long d'attendre, je vais m'ennuyer toute seule..."
        hide adamuSmileSchool
        show adamuConfident at left
        adamu "Ha ha ! Ma présence se mérite."
        hide ayaSorry
        show ayaBlushed at right
        aya "*{i}Regarde Adam d'un air gêné.*"
        hide ayaBlushed
        show ayaCalm at right
        aya "Bon je vais rentrer chez moi, mes parents m'attendent !"
        aya "Rentre bien ! Et envoie un message quand tu seras rentré chez toi."
        hide ayaCalm
        show ayaBlushed at right
        hide adamuConfident
        show adamuSpeakingSerious at left
        aya "Je veillerai jusqu'à ton retour, salut !"
        adamu "Salut !"
        hide ayaBlushed
        hide adamuSpeakingSerious
        show adamuSpeakingSerious at left
        adamu "{i}Ouah c'était génial aujourd'hui j'en reviens pas."
        adamu "{i} Il ne me reste plus qu'à prendre le dernier train et à filer..."

        play sound "audio/fx/notification.mp3" volume 0.2

        "{i}*Téléphone vibre, Adam reçoit un message de Mami*{/i}"

        hide adamuSpeakingSerious
        show adamuSurprisedSchool at left
        adamu "Hein ?! Un message de Mami !"
        adamu "Elle me propose qu'on se voit demain !!!"
        $scoreMami3 = 0

        menu:
            adamu "Qu'est-ce que je dois faire ?"
            "Accepter le rendez-vous de Mami !":
                $scoreMami3 += 7
                #jump to scene 4

            "Refuser son rendez-vous, c'est peut-être un piège après tout...":
                $scoreMami3 -= 7
                #jump to scene 5

        stop music fadeout 0.5




    return
