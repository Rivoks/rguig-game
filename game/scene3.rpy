label scene3:

    scene black with dissolve

    play music "audio/ost/train_station.mp3" volume 0.1

    narrator "{i}Le lendemain..."
    narrator "{i}Le jour tant attendu arriva."
    narrator "{i}Pour une fois, notre Adamu était en avance."
    narrator "{i}Oui vous ne rêvez pas, le même Adamu qui ne s'était pas réveillé le jour de son concours blanc de PACES."

    show trainStation with dissolve

    narrator "{i}Gare de Mommenrency, 11h07."

    show adamuConfident with dissolve

    adamu "Parfum, yes. "
    adamu "Chewing-gum c'est bon."
    adamu "Capote, à la plonge."

    hide adamuConfident

    show adamuSpeakingSerious
    play sound "audio/fx/breathing.mp3" volume 0.2
    narrator "{i}Respire..."
    narrator "{i}Ca va bien se passer, allez ! Je me suis entrainé à sourire."

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
    adamu "C'est quoi cette voix, on dirait le freestyle du pédophile !"
    hide adamuStun
    show adamuAngry
    play sound "audio/fx/train_doors.mp3" volume 0.2
    adamu "Bref, m'enfous."
    hide adamuAngry
    show adamuSmileSchool
    adamu "Le principal c'est que je sois arrivé."
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

    menu:
        aya "Tu as déjà eu une copine ?"
        "Oui mais c'est du passé.":
            hide adamuSmileSchool
            show adamuStun at left
            adamu "C'était y'a longtemps, j'étais jeune et naïf, puis ça s'est mal fini..."
            hide ayaCalm
            show ayaSorry at right
            aya "Ah..."
        "Euh non, jamais...":
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
                    hide adamuSurprise
                    show adamuStun at left
                    adamu "{i}Argh, je vais mourir de honte..."
                    hide ayaCalm
                    show ayaSurprise at right
                    aya "Ah bon, je ne m'en serai pas douté."
                "Non, je n'ai pas la tête à ça.":
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
            $proposeAya = True
            hide ayaSurprise
            show ayaBlushed2 at right
            hide adamuStun
            show adamuSorry at left
            adamu "{i}Purée je l'ai vraiment dit !"
            aya "Kyaaa !"
            aya "Tu ne te moques pas de moi ?"
            hide adamuSorry
            show adamuSpeakingSerious at left
            adamu "Bien sûr que non ! Je suis sérieux Aya, tu me plais vraiment !"
            hide ayaBlushed2
            show ayaBlushed at right
            aya "Merci Adam, ça me touche beaucoup..."
            aya "Moi aussi tu me plais..."
            hide adamuSpeakingSerious
            show adamuSurprisedSchool at left
            aya "Je ne savais pas comment te le dire alors j'ai pensé que ce rendez-vous était une bonne idée."
            hide adamuSurprisedSchool
            show adamuSpeakingSerious at left
            adamu "Aya-chan..."
            hide ayaBlushed
            show ayaSurprise at right
            adamu "Je veux sortir avec toi !"
            hide ayaSurprise
            show ayaBlushed at right
            hide adamuSpeakingSerious
            show adamuSorry at left
            adamu "Dès notre rencontre, je l'ai toujours voulu."
            hide ayaBlushed
            show ayaBlushed2 at right
            adamu "Je n'ai cessé de penser à toi nuits et jours..."
            hide adamuSorry
            show adamuSmileSchool at left
            adamu "Mais ce jour est enfin arrivé, alors voilà..."
            adamu "Je t'aime Aya !"
            aya "..."
            hide ayaBlushed2
            show ayaCalm at right
            aya "Je t'aime aussi Adamu..."
            aya "Profitons de ce concert en tant que couple maintenant."

        "Ah zut j'ai oublié ce que je voulais dire...":
            hide adamuStun
            show adamuSorry at left
            adamu "Euh, j'ai oublié..."
            aya "Ah bon ?"
            hide ayaSurprise
            show ayaCalm at right
            aya "Ca ne devait pas être important alors."
            adamu "Sûrement, oui."

            scene black with dissolve
            narrator "Aie ! Adamu venait de laisser passer une occasion en or et il s'en était rendu compte."
            narrator "Il resta silencieux pendant toute la fin du concert."
            narrator "Aya et lui s'enchangèrent quelques regards mais rien de plus."
            narrator "Eh oui, qu'il est con ! Aya attendait la déclaration de notre jeune riche, elle était déçue mais essaya de sauver les apparences."
            narrator "Adamu ne pouvait plus supporter la réalité en face. Cette réalité où il ne sera jamais avec une hlel."
            narrator "Pris de honte, il s'éclipsa discrètement et resta assis dehors sur un banc jusqu'à la fin du concert."
            narrator "Evidemment, remarquant qu'Adamu avait disparu, Aya le chercha, tenta de l'appeler mais rien à faire, Adamu ne répondit pas."
            narrator "Quel gâchis !"

            stop music fadeout 0.5

            jump scene5


    stop music fadeout 0.5

    if proposeAya == True:
        scene black with dissolve

        narrator "{i}Plus tard dans la nuit, une fois le concert fini."

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
        show adamuSmileSchool at left
        adamu "{i}Ouah c'était génial aujourd'hui j'en reviens pas. Enfin après 21 ans de misère sexuelle, je suis en COUPLE !"
        hide adamuSmileSchool
        show adamuSpeakingSerious at left
        adamu "{i} Que se passe t-il maintenant que je suis seul, j'ai mon kokoro qui bat si vite."
        hide adamuSpeakingSerious
        show adamuConfident at left
        adamu "{i} Oui, je crois que je commence à comprendre, c'est donc ça : être aimé."
        adamu "{i} Bon, il ne me reste plus qu'à prendre le dernier train et à filer..."

        stop music fadeout 0.5

        jump sceneAX
