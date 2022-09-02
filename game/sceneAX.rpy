label sceneAX:
    scene black with dissolve
    "{i}Tout se passait bien pour notre Adamu national.{/i}"
    "{i}Il vivait ses débuts de couples heureux...{/i}"
    scene adamuRoom with dissolve
    show adamuChill with dissolve
    play music "audio/ost/lone_sojourner.mp3" volume 0.2 loop fadein 2.0
    adamu "Je l'aime trop ma petite Aya, j'ai trop envie de..."
    adamu "J'ai trop envie de benzer j'arrive plus à me retenir..."
    adamu "Je lui ai déjà demandé mais elle a pas l'air partante... {w}zebi."
    adamu "Bon tant pis j'attendrais."
    scene adamuRoom
    "{i}** Téléphone vibre **{/i}"
    play sound "audio/fx/notification.mp3" volume 0.3
    stop music
    scene msgAyaEnd with dissolve
    pause
    scene adamuRoom
    show adamuChillJoy with dissolve
    pause
    scene adamuRoom
    show adamuSurprise 
    play sound "audio/fx/collision.mp3" volume 0.3
    adamu "BORDEL DE MERDE QU'EST-CE QU'IL SE PASSE ???" with hpunch
    adamu "Putain est-ce que j'ai merdé ? Qu'est-ce qu'elle veut bien vouloir me dire..."
    hide adamuSurprise
    show adamuChillJoy
    adamu "Bon ça sert à rien de s'affoler, ça doit être un petit truc."
    adamu "On se verra demain matin vite fait devant l'école..."
    adamu "Allez let's go, dodo..."
    scene black with dissolve
    "{i}À ce moment, il ne le savait pas.{/i}"
    scene frontSchool with dissolve
    "{i}Le lendemain, 7h55 devant l'université.{/i}"
    play music "audio/ost/flying_fairy.mp3" volume 0.1
    show ayaSorry at left with dissolve
    show adamuSmileSchool at right with dissolve
    adamu "Salut ma gauffre ça va ?"
    aya "Euh... Salut Adamu..."
    adamu "Qu'est-ce qu'il y'a ?"
    show ayaHurt at left
    aya "..."
    aya "Écoute Adamu je ne sais pas comment te le dire mais..."
    adamu "Mais ?"
    stop music
    play sound "audio/fx/glass_break.mp3" volume 0.1
    aya "Mais je pense qu'on devrait en rester là nous deux..." with hpunch
    aya "Je suis vraiment pas encore prête."
    show adamuSurprisedSchool at right
    adamu "Mais qu'est-ce que tu racontes... Tu peux pas me faire ça !"
    show adamuSorry2 at right
    adamu "C'est une blague hein ?!{w} Tu veux que je te finisses ?"
    hide ayaHurt
    aya "Je suis vraiment désolée t'y es pour rien !"
    show ayaHurt at left
    aya "C'est allé trop vite entre nous..."
    aya "J'espère que tu trouveras quelqu'un de mieux, vraiment Adamu."
    play sound "audio/fx/school_ring.mp3" volume 0.3
    "{i}** Sonnerie ** {/i}"
    hide ayaHurt
    aya "Bon je dois y aller... Désolée encore..."
    scene frontSchool with dissolve
    show adamuSurprisedSchool with dissolve
    adamu "..."
    play music "audio/ost/sadness.mp3" volume 0.1 loop
    show adamuCryingSchool
    adamu "...{w} Putain... {w} Bordel..."
    adamu "..."
    adamu "Putain faut que j'y aille..."
    scene frontSchool with dissolve
    "{i}La journée continua malgré tout pour Adamu.{/i}"
    scene corridorsSchool with dissolve
    "{i}Croyant enfin avoir vu le bout du tunnel, ce dernier se retrouvait plus profond que les bas-fonds.{/i}"
    pause 3.0
    scene classroomExt with dissolve
    "{i}Comme à son habitude, on venait de lui fermer la porte au nez.{/i}"
    "{i}Son coeur n'allait s'en remettre avant plusieurs années.{/i}"
    pause 3.0
    scene stairsSchool with dissolve
    "{i}Surmonter les marches lui semblait être une éternité...{/i}"
    "{i}Mais l'éternité n'est qu'instant pour le condamné.{/i}"
    pause 3.0
    scene cafeteriaSchool with dissolve
    "{i}Quand le coeur chante, le ventre est en grève.{/i}"
    "{i}Avoue que tu kiffes bien toutes ces disquettes depuis tout à l'heure. {w}Petit batard.{/i}"
    pause 3.0
    scene frontSchool with dissolve
    "{i}La journée, bien qu'elle fut longue et rude, se termina.{/i}"
    "{i}Notre RGUIG National se retrouve en piteux état, pathétique si bien que nous ne pouvons vous le montrer.{/i}"
    pause 3.0
    scene streetEve with dissolve
    "{i}Finalement, il aura fait ce qu'il a pu.{/i}"
    "{i}Merci pour tout Adamu, tu t'es bien battu.{/i}"
    jump ending

