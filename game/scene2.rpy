
label scene2:

    stop music

    scene black with dissolve

    narrator "{i}Le lendemain, devant le CROUS. 12h03.{/i}"

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

    mami "J'en étais sûre haha !"
    mami "Alors t'as des vues sur qui ? Tu vas tout me dire !"

    show adamuSorry at right
    hide adamuSorry2

    adamu "Haha pourquoi pas mais toi tu t'intéresses pas aux mecs ?"

    show mamiStoic at left

    stop music fadeout 2.0

    mami "..."

    show adamuSurprisedSchool at right

    adamu "Mami-chan ?"

    play music "audio/ost/lone_sojourner.mp3" volume 0.3 loop fadein 1.0

    show mamiSpeaking at left

    mami "C’est rien t’inquiète, je viens juste de sortir d’une longue relation c’est un peu compliqué du coup..."

    adamu "Ah excuse-moi... je... euh..."

    mami "Tu pouvais pas savoir t'inquiète."

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

    narrator "{i}Aya venait d'arriver au réfectoire du CROUS, elle surprend au loin Adamu en train de déjeuner avec Mami. Adam croisa son regard et l'évita aussitôt.{/i}"

    scene cafeteriaSchool with dissolve

    show mamiBlush at left

    show adamuSorry at right

    play music "audio/ost/excited.mp3" volume 0.2 loop fadein 1.0

    play sound "audio/fx/collision.mp3"
    adamu "{i}Bordel de pute je suis cramé ! Aya voudra plus jamais me parler putain zebi…{/i}" with hpunch

    show mamiAsking at left

    mami "Qu’est-ce qu’il y’a ?"

    adamu "Ah non rien t’inquiète pas, j’ai un peu mal au ventre je pense que c’était pas très frais ce qu’on a mangé haha…"

    mami "Ah bon tu trouves ? Moi j’ai trouvé ça plutôt bon."

    adamu "D’ailleurs c’est quoi ton plat préféré ?"

    scene cafeteriaSchool with dissolve

    show adamuAngry with dissolve

    adamu "{i}Il faut que je trouve une explication à donner à Aya tout à l’heure ! Réfléchis…{/i}"

    scene cafeteriaSchool with dissolve

    show mamiSpeaking at left with dissolve

    mami "Tu m'écoutes Adamu ?"

    show adamuSorry at right with dissolve

    adamu "Ah oui désolé, j’ai la tête qui tourne un petit peu, haha…"

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

    narrator "{i}Mami et Adamu marchèrent le temps de la digestion...{/i}"

    scene frontSchool with dissolve

    play music "audio/ost/happy_school.mp3" volume 0.3 fadein 2.0 loop

    show adamuConfident at right with dissolve

    show mamiStoic at left with dissolve

    mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi."

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


    narrator "{i}La sonnerie retentit, les cours ayant repris Adam se précipita vers la classe.{/i}"

    scene corridorsSchool with dissolve

    narrator "{i}Il arriva en retard de 4 minutes au cours d’informatique dont la séance était dédiée au projet...{/i}"

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
    adamu "{i}Après tout je suis l’ultime Ninja ayant sauvé l’opération plan H par le passé… Haha si elle savait...{/i}"

    scene classroomSchool with dissolve

    show adamuSorry at right with dissolve
    show ayaBlushed at left with dissolve

    adamu "J’ai mangé avec une amie, on avait jamais eu le temps vu qu’on a pas le même planning, et toi ?"

    aya "Ah ouais c'est cool ça ! J’ai mangé avec des amies du lycée, à vrai dire je ne me suis pas vraiment fait d’amies à la fac..."

    adamu "Ah ouais pourtant tout le monde voudrait devenir ami avec une fille aussi mignonne haha..."

    show ayaBlushed2 at left

    aya "Arrête de dire des bêtises..."

    adamu "Ahah tu vois même quand je te dis la vérité tu me fais des reproches !"

    aya "Mais c’était pas un reproche c’est toi qui..."

    scene classroomSchool with dissolve
    play sound "audio/fx/anime_wow.mp3" volume 0.3
    narrator "{i}À ce moment tout se passait bien, l’opération de sauvetage miraculeux eut été une réussite.{/i}"
    narrator "{i}Sans même mentir Adamu s’était tiré d’affaire. À vrai dire mentir provoque toujours des retombées.{/i}"

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
        "Non du tout ! C'est un ami qui m'a envoyé un drôle de message, t'es parano un peu haha...":
            stop music fadeout 3.0
            jump scene2_1_2

label scene2_2:

    show adamuStun at right

    adamu "Ouais je comprends..."

    mami "C'est la vie hein..."

    menu:
        "Répondre à Mami-chan:"
        "En tout cas si t'as un problème tu peux m'appeler n'hésite pas":
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
            mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi."
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
            narrator "{i}Le déjeuner se passa sans accroc. {/i}"
            scene frontSchool with dissolve
            show adamuConfident at right with dissolve
            show mamiStoic at left with dissolve
            mami "Bon il faut que j’y aille ! C’était plutôt cool ce midi."
            adamu "Ouais clairement ! On se refera ça hein ?"
            show adamuSorry at right
            hide adamuConfident
            mami "Euh ouais pourquoi pas..."
            mami "Bon allez à plus !"
            scene black with dissolve
            narrator "{i}La journée se termina pour Adamu. Les jours passèrent sans nouvelles de Mami...{/i}"
            return
            jump scene5


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

    narrator "{i}Finalement pendant toute l’heure restante ils n’auront discuté que du projet. Adamu est en train mauvaise posture. Mais ce qu’il s’apprêtait à voir en sortant de la salle était terrible...{/i}"

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

    narrator "{i}Aya était en larme, elle partit en courant.{w} Toute la salle était abasourdie face à la scène, des murmures se faisaient entendre, rien de bon pour la réputation de notre Majin Boo national.{/i}"

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
    narrator "{i}Et leur petite scène de ménage continua. Ils étaient tellement mignons que beaucoup dans la salle pensaient à la formation même d'un couple à cet instant.{/i}"
    show adamuConfident at right with dissolve
    show ayaLaugh at left with dissolve
    adamu "Et c'est comme ça que ma mère m'a surpris sur Twitter en train de dire que j'allais niquer des daronnes !"
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
    narrator "{i}À moment précis, Adamu commenceait à monter les saintes marches de la légende du P.A.L.M.{/i}"
    narrator "{i}Un moment historique dans sa longue vie d'ermite croupissant dans les débris de sa chambre morose.{/i}"
    narrator "{i}Il venait d'obtenir le premier date de toute sa vie. Plus rien ne sera comme avant. {/i}"
    narrator "{i}Nom de code de l'opération: PLAN D(ate).{/i}"
    scene black with dissolve
    stop music fadeout 2.0
    narrator "{i}Les jours passèrent. {w} Le jour saint du date arriva.{w}{/i}"
    jump scene3
    return


label scene2_mami_dm:
    scene black with dissolve

    play music "audio/ost/papakatsu.mp3" volume 0.3 loop fadein 1.0

    narrator "{i}Adamu, de retour chez lui. 23h34.{/i}"

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
    stop music
    jump scene4

label scene2_1_1_2:
    scene adamuRoom
    show adamuChill

    adamu "Bon en vrai la flemme de la voir, c'est trop pour moi aujourd'hui... {w} Je vais tag une petite game et ensuite dodo."

    scene black with dissolve
    narrator "{i}Fin de journée pour Adamu.{i}"

    jump scene5
    return
