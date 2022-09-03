label scene5:

    scene black with dissolve

    play sound "audio/fx/light_rain.mp3" volume 0.2 loop


    narrator "{i}Deux mois s'étaient déjà écoulés depuis la rentrée."
    narrator "{i}Les moments passés avec Aya et Mami semblaient si loin désormais..."
    narrator "{i}Tout comme les derniers rayons de soleil laissaient place à la pluie."

    narrator "{i}Acte V - All is (not) lost."

    stop sound

    play sound "audio/fx/moderate_rain.mp3" volume 0.2


    show konbini with dissolve

    adamu "Quelle journée de merde..."
    adamu "Le sandwich bolognaise du 7Eleven va me réconforter."
    adamu "Hmm..."
    adamu "Ce goût si unique ! Et ces pâtes qui se marient à la perfection avec ce pain moelleux, je fonds de plaisir..."

    stop sound fadeout 0.5

    play sound "audio/fx/moderate_rain.mp3" volume 0.1 loop

    show najimoCalm with dissolve
    play music "audio/ost/najimo_theme.mp3" volume 0.4 loop
    noname "Hé, salut !"
    adamu "Bonsoir, on se connaît ?"
    naji "Tu t'appelles Adamu, c'est ça ? On est dans la même classe, moi c'est Najimo."
    adamu "Ah... Enchanté !"
    adamu "{i}C'est bizarre je ne l'ai jamais remarqué, pourtant un beau gosse pareil ne passe pas inaperçu..."
    adamu "{i}Oula qu'est-ce que je raconte moi !"
    naji "Alors, tu faisais quoi dans le coin ?"
    adamu "J'ai pris un truc à manger avant de rentrer chez moi."
    naji "Cette supérette est pas mal, je m'y arrête aussi de temps en temps."
    naji "Au fait, tu ne serais pas dans une asso par hasard ?"
    adamu "Non et puis c'est pas trop mon truc..."
    adamu "Je me sens pas très bien en ce moment à vrai dire."
    naji "Justement, rejoindre une asso pourrait être un bon moyen de te changer les idées."
    naji "Tu pourrais rencontrer du monde et te faire des amis qui partagent la même passion."
    adamu "Sûrement, ouais..."
    adamu "{i}Je me sens tellement vide en ce moment...Et s'il avait raison ?"
    naji "Passe demain à la salle E205 à partir de 10h, je crois que c'est une nouvelle association qui recrute."
    adamu "Et c'est une asso de quoi ?"
    naji "Je n'en sais pas plus, c'est juste des bruits de couloir que j'ai entendu."
    naji "Tu verras bien par toi même."
    naji "Allez, j'y vais moi, bonne soirée mec."
    adamu "Salut et merci !"
    adamu "Faire de nouvelles recontres, hein..."

    stop sound fadeout 0.5
    stop music fadeout 0.5

    scene black with dissolve

    narrator "{i}Le lendemain matin..."

    show meetingRoom with dissolve

    play music "audio/ost/sikusu_theme.mp3" volume 0.2  loop

    adamu "Hum, bonjour !"

    show kuromeCalmBDE with dissolve

    noname "Hey !"
    adamu "C'est bien ici la Sikusu ?"
    kuro "Tout à fait ! Je suis Kurome, la présidente de la Sikusu."
    adamu "Je m'appelle Adamu, enchanté."
    adamu "Alors voilà, j'aimerais bien rejoindre cette association..."
    hide kuromeCalmBDE
    show kuromeHappyBDE
    kuro "Pas de soucis ! A une condition..."
    adamu "Laquelle ?"
    kuro "Tu vas devoir passer un entretien pour me convaincre de te chosir !"
    kuro "C'est clair ?"
    adamu "Non c'est sombre."
    hide kuromeHappyBDE
    show kuromeCringeBDE
    kuro "..."
    hide kuromeCringeBDE
    show kuromeCalmBDE
    kuro "Comme tu es le premier à venir t'inscrire, tu deviendras mon larb... euh bras droit si tu réussis !"
    kuro "Es-tu prêt ?"
    adamu "Quoi, ça commence tout de sui-"
    kuro "En garde !"

    menu:
        kuro "Pourquoi veux-tu intégrer la Sikusu ?"
        "Pour ne plus être un mage noir.":
            hide kuromeCalmBDE
            show kuromeCringeBDE
            kuro "Icuras elran."
        "Pour découvrir la vie étudiante.":
            hide kuromeCalmBDE
            show kuromeCringeBDE
            kuro "Quelle réponse bateau, je suis déçue..."


    hide kuromeCringeBDE
    show kuromeCalmBDE
    kuro "Passons, c'est le moment de te resaisir !"

    menu:
        kuro "Dis-moi, tu bois un peu ?"
        "L'alcool c'est pas cool.":
            hide kuromeCalmBDE
            show kuromeCringeBDE
            kuro "Hum, je vois..."
            hide kuromeCringeBDE
            show kuromeCalmBDE
        "J'aime boire sous les ponts de la ville, 8.6 à la main.":
            hide kuromeCalmBDE
            show kuromeHappyBDE
            kuro "Tequilla, Heineken, pô l'temps de niaiser !"
            hide kuromeHappyBDE
            show kuromeCalmBDE


    kuro "On va voir si t'es drôle à présent."

    menu:
        kuro "QUOI ?"
        "feur.":
            hide kuromeCalmBDE
            show kuromeHappyBDE
            kuro "Haha !"
            hide kuromeHappyBDE
            show kuromeCalmBDE
        "El Psy Congroo...":
            hide kuromeCalmBDE
            show kuromeCringeBDE
            kuro "Pardon ?"
            hide kuromeCringeBDE
            show kuromeCalmBDE
        "LE SEEEEEEEEEEEEXE !":
            hide kuromeCalmBDE
            show kuromeCringeBDE
            kuro "..."
            hide kuromeCringeBDE
            show kuromeCalmBDE


    kuro "Ok, voilà une question un peu plus sérieuse maintenant."

    menu:
        kuro "A l'arrivé d'un CC..."
        "Je révise tout la veille.":
            hide kuromeCalmBDE
            show kuromeHappyBDE
            kuro "En légende !"
            hide kuromeHappyBDE
            show kuromeCalmBDE
        "Je ne me réveille pas.":
            kuro "Un grand classique..."
        "Je ne révise rien, c'est juste un partiel blanc.":
            hide kuromeCalmBDE
            show kuromeHappyBDE
            kuro "Zizi à l'air, larme à l'œil !"
            hide kuromeHappyBDE
            show kuromeCalmBDE


    kuro "Courage, c'est la dernière question !"

    menu:
        kuro "La soirée idéale selon toi..."
        "Soirée à Chatou avec piscine.":
            hide kuromeCalmBDE
            show kuromeHappyBDE
            kuro "Tu me tentes là."
            hide kuromeHappyBDE
            show kuromeCalmBDE
        "Boîte de nuit, on pose tout l'argent du BAFA.":
            hide kuromeCalmBDE
            show kuromeHappyBDE
            kuro "On fait péter la moula !"
            hide kuromeHappyBDE
            show kuromeCalmBDE
        "Rdv discord 21h, aramu gaming.":
            hide kuromeCalmBDE
            show kuromeCringeBDE
            kuro "Oh, ton odeur..."
            hide kuromeCringeBDE
            show kuromeCalmBDE

    stop music fadeout 0.5

    kuro "C'est terminé !"
    hide kuromeCalmBDE
    show kuromeHappyBDE
    play sound "audio/fx/drums_roll.mp3" volume 0.2
    kuro "Passons aux résultats !"
    kuro "..."
    hide kuromeHappyBDE
    show kuromeCringeBDE
    kuro "..."
    hide kuromeCringeBDE
    show kuromeCalmBDE
    kuro "Bon, mes analyses sont formelles."
    hide kuromeCalmBDE
    show kuromeCringeBDE
    kuro "Tu es une merde humaine et en chien devant l'état par dessus le marché !"
    adamu "Hum..."
    hide kuromeCringeBDE
    show kuromeHappyBDE
    play sound "audio/fx/gg.mp3" volume 0.2
    kuro "TU AS REUSSIS, FELICITATIONS !"
    adamu "Quoi ?"
    hide kuromeHappyBDE
    show kuromeCalmBDE
    play music "audio/ost/private_eye.mp3" volume 0.2 loop
    kuro "Et oui chez la Sikusu, nous sommes des déchets, c'est une qualité essentielle."
    hide kuromeCalmBDE
    show kuromeHappyBDE
    kuro "Alors bienvenu parmi nous Adamu-kun !"
    adamu "Super ! Je ne m'y attendais pas."
    hide kuromeHappyBDE
    show kuromeCalmBDE
    kuro "Maintenant que c'est fait, en tant que bras droit, je vais te confier ta première mission."
    kuro "Dans une semaine aura lieu la plus grosse soirée étudiante jamais réalisée dans le campus !"
    kuro "J'aurai donc besoin de ton aide pour préparer tout cela."
    adamu "Hein mais c'est bientôt, je ne pense pas en être capable..."
    kuro "Ne t'en fais pas, c'est là que ta première mission intervient."
    kuro "Pour t'entraîner, tu vas aller  nettoyer le terrain de volley !"
    hide kuromeCalmBDE
    show kuromeHappyBDE
    kuro "Bon moi je file, j'ai du pain sur la planche."
    kuro "Bisous !"
    adamu "Ok, hum..., à plus !"

    stop music fadeout 0.5

    show sportClass with dissolve
    play music "audio/ost/cool_guy_adamu.mp3" volume 0.2 loop

    adamu "Voici donc le terrain de sport, il est immense !"
    adamu "Déjà que j'ai du mal à ranger ma chambre, alors nettoyer un tel endroit seul..."
    adamu "Mais bon, je n'ai pas le choix, je le fais pour la Sikusu."
    adamu "Je dois devenir un homme de haute valeur et le monde entier sera à mes pieds."
    adamu "C'est sale par ici, je vais nettoyer ça."
    adamu "Oh !"
    adamu "Quelqu'un a oublié son maillot, beurk ça pue la transpiration..."
    adamu "Attends mais c'est plus petit que le diagramme."
    adamu "C'est du XS !"
    adamu "C'est sûrement celui d'une fille alors !"
    adamu "Super !"
    adamu "{i}Renifle..."
    adamu "Oh, le doux parfum de la science !"
    show najimoCalm with dissolve
    naji "Salut !"
    adamu "Waaah ! Salut..."
    adamu "{i}Putain il arrive toujours au pire moment..."
    naji "Que fais-tu ici tout seul ?"
    adamu "Ah, c'est pas ce que tu crois... On m'a mis mal."
    naji "Je vois bien que tu es en train de renifler ce maillot, je te parlais du nettoyage."
    naji "Tu joues au bon samaritain ?"
    adamu "Et puis quoi encore ? Je suis de corvée, je n'ai pas le choix."
    adamu "J'ai rejoins l'association dont tu m'avais parlé. C'est la Sikusu."
    naji "L'équivalent d'un BDE quoi."
    adamu "Entre autre, ouais. Ca t'intéresse de nous rejoindre ?"
    naji "Bof, ça a l'air chiant comme truc."
    naji "Tu veux pas un coup de main pour le nettoyage sinon ?"
    adamu "Avec plaisir !"
    hide najimoCalm

    narrator "{i}Les deux étudiants passèrent tout l'après-midi à nettoyer le terrain. Peu à peu Adamu s'ouvrait à Najimo et lui raconta ses aventures avec Aya et Mami."
    narrator "{i}Il faut dire que depuis qu'Adamu courrait après les filles, il avait complètement délaissé ses amis."
    narrator "{i}Pouvoir parler à quelqu'un sans langue de bois, sans réfléchir à ce qu'on allait dire, Adamu avait oublié cette liberté."
    narrator "{i}Les jours suivant furent plus calmes, Adamu continua de traîner avec Najimo. Cette nouvelle amitié naissante remonta le moral de notre héros."

    stop music fadeout 0.5

    scene black with dissolve
    play music "audio/ost/moulaga.mp3" volume 0.2 loop

    narrator "{i}Puis la soirée tant attendue arriva."
    narrator "{i}C'était le moment où tous les étudiants se lâchaient et révelaient leur vrai nature."
    narrator "{i}Il faut dire qu'avec l'alcool qui coule à flots et des tenues légères, celà facilait les choses."
    narrator "{i}Les bonnes comme les moins bonnes."
    narrator "{i}Sikusu Night - 03:17"

    show sikusu_party with dissolve

    show kuromeCalm with dissolve
    kuro "Alors Adamu, ça te plaît la soirée ?"
    adamu "Ouais c'est génial !"
    adamu "{i}Je ne peux pas lui dire que je suis membre de la confrérie PALM..."
    hide kuromeCalm
    show kuromeHappy
    kuro "Merci pour ton aide précieuse, on aurait jamais pu finir à temps sans toi !"
    adamu "Haha, y'a pas de quoi, je suis ton bras droit après tout !"
    adamu "{i}Merde, elle est mignonne..."
    adamu "{i}Je crois que je commence à m'attacher."
    kuro "Allez, je nous ressers un verre pour fêter ça, on fait cul sec !"
    adamu "{i}Glou glou..."
    kuro "..."
    hide kuromeHappy
    show kuromeDrunk
    adamu "Arrgh..."
    adamu "C'est une purge ton truc..."
    adamu "{i}Je tiens pas l'alcool moi fais chier..."
    adamu "Hé Kurome, tu vas bien ?"
    kuro "Bien sûuur, ze vais bien !"
    kuro "Viens on va danzer sur la biste..."
    adamu "{i}Elle est arrachée... Elle me propose de danser, ça sent pas bon cette histoire."
    adamu "{i}Mais je ne peux pas la laisser dans cet état alors autant profiter."
    adamu "{i}On reverra plus tard pour la fidélité au PALM..."

    narrator "{i}Adamu et Kurome commencèrent à danser. Au fur et à mesure que la musique avancait, leur corps se rapprochaient."
    narrator "{i}Une telle proximité avec une femme, Adamu n'avait jamais connu une telle chose. Que ce soit avec Aya ou Mami il n'était jamais arrivé à ce stade."
    narrator "{i}Kurome l'enlaça et le serra dans ses bras. Leurs jambes s'entrêmelaient et leurs bras s'enchevêtraient."
    narrator "{i}Cette image rappela à Adamu son TP de brassage interchromosomique en Terminale."
    narrator "{i}Il ne pu s'empêcher d'avoir le surligneur actif, le barreau donc."

    kuro "Hé, embraze boi !"
    adamu "{i}Quoi elle veut que je l'ignite ?"
    adamu "{i}Mais je joue ghost, je sais pas comment faire..."
    kuro "Allez, un bisous."
    adamu "{i}Ah putain c'était ça !"
    adamu "{i}Dans ce cas, j'y vais."
    "Adamu saisissa délicatement le menton de Kurome avec trois doigts et rapprocha en douceur son visage du sien."
    hide kuromeDrunk
    show kuromeBlush
    kuro "..."
    adamu "..."
    hide kuromeBlush
    show kuromeKiss
    kuro "Hmm..."
    adamu "Aaah..."
    hide kuromeKiss
    show kuromeBlush
    kuro "..."
    adamu "{i}C'était géni-"
    hide kuromeBlush

    stop music fadeout 0.5
    play music "audio/ost/najimo_true_face.mp3" volume 0.2 loop

    show najimoCalm with dissolve
    naji "Hop c'est dans la boîte."
    naji "La fête est finie."
    adamu "Hein ?!"
    hide najimoCalm
    show najimoMean
    play sound "audio/fx/collision.mp3" volume 0.2
    naji "HEY LES GARS, REGARDEZ UNE FILLE BOUREE SE FAIT ABUSER !!!" with hpunch
    naji "Ce mec là c'est Adamu et il l'a forcé à l'embrasser !"
    adamu "Najimo ? Mais qu'est-ce que tu racontes !!!"
    adamu "Ecoutez-moi tous !!! Ce n'est pas vrai, je n'ai pas fait ça !"
    hide najimoMean
    show najimoCalm
    naji "Alors pourquoi ton jean est taché ?"
    hide najimoCalm
    show najimoMean
    naji "Cet homme est un exhibitionniste, appelez la police !"
    adamu "Mais pourquoi tu me fais ça ?! Je pensais qu'on était amis..."
    hide najimoMean
    show najimoLaugh
    naji "Ha ha ha ha !"
    naji "Elle est bien bonne celle-là. Moi ami avec un type pareil, pas possible !"
    hide najimoLaugh
    show najimoMean
    naji "Tu sais je vais te dire un truc, Kurome c'est une crasseuse tout le monde l'a déjà foudroyée ici moi y compris !"
    adamu "Pas possible..."
    adamu "Pourquoi..."
    naji "Si tu savais le bien fou que ça me fait de te pourrir !"
    naji "Tu ne peux pas me comprendre après tout."

    play sound "audio/fx/flashback.mp3" volume 0.2

    show amphiSchool with flash
    show najimoDark with dissolve
    naji "J'ai toujours été seul depuis le début. Personne ne s'intéressait à moi. C'était comme si je n'existais pas."
    naji "Alors peu à peu je me suis replié sur moi, je ne pouvais plus supporter cette souffrance."
    show corridorsSchool with dissolve
    naji "Mais toi ! Oui toi Adamu, tout est de ta faute ! TOUT !"
    show stairsSchool with dissolve
    naji "Tu es arrivé dans cette école et tu m'as privé d'Aya, de mon seul bonheur."
    show chairsAmphi with dissolve
    show najimoDarkBlush at left with dissolve
    show ayaCalm at right with dissolve
    naji "C'était la seule personne à m'adresser la parole, elle était tellement gentille avec moi, je n'oublierai jamais."
    hide najimoDarkBlush
    hide ayaCalm
    show streetEve with dissolve
    show najimoDark with dissolve
    naji "Puis lorsque tu es arrivé, j'ai tout perdu, tu m'as tout pris..."
    naji "Alors maintenant, c'est à ton tour de goûter au désespoir !"
    hide najimoDark

    play sound "audio/fx/flashback.mp3" volume 0.2
    scene sikusuParty with flash

    show najimoMean
    naji "C'est fini à présent, la police va arriver d'une minute à l'autre."
    hide najimoMean
    show najimoLaugh
    naji "Tu es fait comme un rat !"
    naji "Ha ha ha !"
    naji "Un rat ! Comme toi ! Tu l'as ou pas ?"
    naji "Ha ha ha !"
    hide najimoLaugh
    show najimoMean
    naji "Sache une chose, les corbeaux auront toujours le dernier mot."

    narrator "{i}Adamu resta muet tout le long mais compris la situation.{/i}"
    narrator "{i}Cette fois-ci c'était du sérieux et s'il ne réagissait pas maintenant il serait définitivement fichu.{/i}"

    menu :
        adamu "{i}Merde, il faut que je réagisse !"
        "Talk no jutsu !":
            stop music fadeout 0.5
            play music "audio/ost/talk_no_jutsu.mp3" volume 0.1 loop
            adamu "Najimo écoute-moi !"
            hide najimoMean
            show najimoSkeptic
            adamu "Je sais que tu te sentais seul depuis tout ce temps et que tu avais besoin d'un peu d'amour !"
            adamu "Tu penses qu'on est différent, mais..."
            adamu "Détrompe-toi ! Moi aussi j'ai connu ce sentiment bien trop longtemps et des nuits entières passées le calebut rempli de mayonaise."
            adamu "Mais tu peux encore changer comme je l'ai fait !"
            naji "..."
            adamu "Et si tu ne crois pas en toi, crois en moi qui crois en toi !"
            adamu "Moi aussi, je croyais que ma vie était morte et enterrée mais je n'ai pas abandonné !"
            adamu "Tu peux y arriver, j'en suis certain !"
            adamu "L'espoir vaincra le désespoir."
            naji "Hmm..."
            adamu "Je refuse d'abandonner."
            adamu "Je refuse de perdre ici et maintenant."
            adamu "Je refuse de tout jeter parce que tout ce que j'ai pour moi c'est le désir de continuer à avancer."
            adamu "Et toi tu continueras d'avancer avec l'espoir dans ton cœur."
            adamu "Que la passion te guide, ouais !"
            adamu "{i}Alors est-ce que ça a marché ?"
            naji "..."
            adamu "{i}C'était mon dernier coup."
            hide najimoSkeptic
            show najimoMean
            play sound "audio/fx/bump.mp3" volume 0.1
            stop music
            naji "MAIS FERME LAAAAA BOUFFON !!!" with hpunch
            hide najimoMean
            show najimoLaugh
            naji "Répète sans miauler pour voir."
            scene black with dissolve
            play music "audio/ost/despair.mp3" volume 0.1 loop
            narrator "{i}Comment raisonner un corbeau, Najimo avait sombré dans la folie, c'était perdu d'avance."
            narrator "{i}La police ne mit pas longtemps à arriver. Ils embarquèrent le suspect et le placèrent en garde à vue."
            narrator "{i}Adamu tenta d'expliquer la situation mais personne ne le prit au sérieux."
            narrator "{i}Il fut relâché trois jours plus tard. Son honneur était bafoué et sa réputation ternie."
            narrator "{i}Qui sait comment allait se dérouler les jours suivant désormais..."

            stop music fadeout 0.5
            jump endingAlt

        "Repli tactique !":
            stop music fadeout 0.5
            play music "audio/ost/despair.mp3" volume 0.1 loop
            naji "Il s'enfuit ! Arrêtez-le !"
            play sound "audio/fx/bump.mp3" volume 0.2
            scene black with dissolve
            narrator "{i}La tentative d'évasion d'Adamu fut vaine, la salle entière se jeta contre lui et le roua de coups."
            narrator "{i}La police ne mit pas longtemps à arriver. Ils embarquèrent le suspect et le placèrent en garde à vue."
            narrator "{i}Adamu tenta d'expliquer la situation mais personne ne le prit au sérieux."
            narrator "{i}Il fut relâché trois jours plus tard. Son honneur était bafoué et sa réputation ternie."
            narrator "{i}Qui sait comment allait se dérouler les jours suivant désormais..."

            stop music fadeout 0.5
            jump endingAlt
