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
             