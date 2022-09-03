label scene1:
    scene classroomExt with dissolve
    narrator "{i}Lundi 5 septembre 2022, 8h03."
    play sound "audio/fx/classroom.mp3" volume 0.1 fadein 1.0

    show adamuSmileSchool with dissolve

    adamu "Voici ma classe..."
    adamu "On dirait que des groupes sont déjà formés."
    adamu "Ils doivent se déjà connaître."
    adamu "Voyons voir, au niveau des meufs..."

    show adamuSpeakingSerious

    "*Jette un rapide coup d'oeil.*"
    adamu "..."

    show adamuAngry

    adamu "Ca recommence la putain de sa mère..."

    show adamuVeryAngry

    adamu "Y'a que des chinois 1m10 les bras levés comme en 2nd."
    "*Zieute*"

    show adamuAngry

    adamu "Aucun gros tarpé de lopessa à l'horizon."

    adamu "J'avais l'espoir d'être dans la même classe que Mami"
    adamu "Mes espoirs sont brisés."
    stop sound fadeout 3


    #Ajouter Ost
    scene classroomExt with dissolve
    play music "audio/ost/scattered_flowers.mp3" volume 0.1 loop fadein 1.0

    narrator "{i}C'est alors qu'une sillouhette elancée se dessina devant lui."
    narrator "{i}Contre toute attente, il reconnu une beauté innoncente."
    narrator "{i}Comment pourrait-il l'oublier."
    narrator "{i}Ce jour-là l'humanité s'en est souvenue."

    show ayaSurprise with dissolve

    noname "Oh mais c'est toi !"


    narrator "{i}À ce moment il comprit."
    narrator "{i}Son instinct de PALM ne le trompait jamais: c’était ce qu’il appelait une « Hlel »."
    narrator "{i}Une fille pudique, innocente et qui se retrouvait décontenancée en parlant avec un homme."

    scene classroomExt with dissolve

    show adamuSurprisedSchool at left with dissolve
    show ayaCalm at right with dissolve

    adamu "Salut, comment ça va depuis le temps ?"
    noname "Bien merci, au fait moi c'est Aya."
    aya "Aya Kataragi."
    adamu "Adam, enchanté."

    show adamuSmileSchool at left

    adamu "On est dans la même classe, c'est cool."
    adamu "J'espère qu'on va bien s'entendre."

    show ayaBlushed at right

    aya "Haha..."
    aya "Euh, le cours va commencer, allons-y Adam."

    play sound "audio/fx/door_open.mp3" volume 1.0
    stop sound

    scene classroomInt with dissolve
    show yoshida with dissolve



    "Yoshida" "Bonjour, je m'appelle Yoshida et je serai votre professeur principal pour ce semestre."
    "Yoshida" "Rentrons dans le vif du sujet sans tarder."
    "Yoshida" "Ce semestre, vous aurez un projet d'informatique à réaliser en binôme."
    "Yoshida" "Le choix du binôme est libre, bien évidemment."

    hide yoshida with dissolve

    narrator "{i}Alors que les groupes commencaient à se former et à discuter entre eux, la petite Aya semblait esseulée."

    show ayaCalm

    narrator "{i}Adam ne resta pas insensible à la détresse d'Aya. Dès lors, il activa le mode « Bête de Guerre »."
    narrator "{i}C'est avec un air confiant, presque sournois, qu'il s'approcha à pas de loup d'Aya."

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
    adamu "Bien sûr que non !"

    show ayaCalm at right
    aya "Merci, Adam."

    scene classroomInt with dissolve

    narrator "{i}Le cours se termina et les élèves commencaient à rentrer chez eux."

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

    narrator "{i}Evidemment notre ventre-en-coeur ne l’entendit pas de cette oreille."
    narrator "{i}Les dieux étaient avec lui, il savait que cette demande n'était pas anodine."



    menu:
        "Est-ce le bon moment pour proposer un date à Aya ?"
        "Oui":
            scene corridorsSchool
            show ayaCalm at right
            show adamuSmileSchool at left
            adamu "Aya, t'es libre demain après-midi ?"
            show ayaSurprise at right
            aya "Oui je n'ai rien de prévu, pourquoi ?"
            adamu "Parfait, demain est une belle journée. Autant en profiter."
            adamu "Ca te dirait de se promener ensemble dans le quartier ? Je connais un coin sympa."
            hide ayaSurprise
            aya "C'est une bonne idée, on se voit demain alors."
            adamu "Ca marche, rentre bien."
            aya "Toi aussi, salut !"

            stop music


            show streetEve with dissolve
            play music "audio/ost/hero.mp3" volume 0.1  fadein 1.0

            narrator "{i}Sur le chemin du retour, Adamu remercia les cieux de la bonne fortune qui l’avait touché."
            narrator "{i}Enfin, il commencait à arpenter la voie légendaire de Maru Arufa, samouraï du passé et symbole de virilité pour notre héros."
            narrator "{i}Ainsi se termina la rentrée de notre jeunot, il pouvait se reposer il l'avait bien mérité."

            stop music
            jump scene3

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
            narrator "{i}Chambre d'Adam, 19h07."

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

            menu:
                adamu "Que faire ?"
                "Accepter de manger avec Mami":
                    show adamuChillJoy
                    adamu "Je ne laisserai pas passer ma chance cette fois-ci..."
                    adamu "Un tête à tête avec une Basic White Bitch, le pied !"
                    adamu "J'ai hâte d'être lundi !"
                    jump scene2

                "Refuser et prétexter une excuse":
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
                    adamu "Un message d'Aya ! Je ne m'y attendais pas..."
                    adamu "Elle me remercie pour la journée. Elle a dit que c'est la première fois qu'elle se sent aussi à l'aise avec un garçon !"

                    menu:
                        "{i}Dois-je répondre à Aya maintenant ?"

                        "Oui, tout de suite !":
                            show adamuChillJoy
                            adamu "Voilà, c'est fait !"
                            adamu "Bon là, je dois rectifier le tir."

                            menu:
                                "{i} Proposer un date à Aya ?"

                                "Oui, je n'ai rien à perdre !":
                                    adamu "Elle a dit que c'était la première fois qu'elle se sentait aussi à l'aise avec un garçon."
                                    adamu "C'est un appel de phare, ne pas prendre les devants serait du int !"
                                    adamu "Tac tac tac, tac tac tac !"
                                    adamu "C'est envoyé ! C'est qui le gros baiseur ?"
                                    adamu "Bah je crois bien que c'est bibi !"

                                    return
                                    jump scene3


                                "Non, c'est encore trop tôt !":
                                    show adamuChill
                                    adamu "Mieux vaut ne pas se presser avec les filles timides..."
                                    show adamuChillJoy
                                    adamu "J'ai fait le bon choix, c'est sûr !"
                                    return
                                    jump scene5

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
                            adamu "Waaaah !"
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

                            scene black with dissolve


                            stop music

                            jump scene5
