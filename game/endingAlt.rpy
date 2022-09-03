label endingAlt:
    scene black with dissolve
    stop music fadeout 3.0
    "{i}Adamu avait cessé de suivre les cours depuis plusieurs jours.{/i}"
    "{i}En un jour pluvieux, il n'arrivait plus à supporter sa vie.{/i}"

    play sound "audio/fx/rain.mp3" volume 0.3 loop fadeout 5
    play music "audio/ost/bakamitai_radio.mp3" volume 0.1 loop
    scene rainStreet with dissolve
    "{i}Là, dans cette ruelle aux sournois appels.{i}"
    "{i}Adamu s'en allait marcher sans savoir où aller.{i}"
    "{i}Finalement il s'arrêta devant une taverne malfamé. {w}Les vrais rats reconnaissent les ratelières.{i}"

    stop sound
    scene tavernDark with dissolve
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    "{i}Cette enseigne semblait être fréquentée des désoeuvrés.{/i}"
    "{i}Les gémissements d'agonies se faisaient entendre de toute part.{/i}"
    "{i}Adamu commanda un bon vieux verre de Ricard pour broyer du noir.{/i}"
    noname "Bah alors mon petit gars, qu'est-ce qu'il t'arrives à toi ?"
    show tinoSmile with dissolve
    noname "T'as pas l'air dans ton assiette, hein..."
    noname "Qu'est-ce tu dis ? {w} Les minettes te font tourner la tête ?"
    show tinoLaugh
    play sound "audio/fx/collision.mp3" volume 0.2
    noname "BAHAHAHAHAH !" with hpunch
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    hide tinoLaugh
    noname "C'est pas contre toi mon vieux hein, sans rancune."
    noname "Simplement ici c'est monnaie courante ce genre d'histoire."
    noname "T'en fais pas, en réalité c'est toutes des grosses folles."
    show tinoSmile 
    noname "Je t'assure te prends pas la tête mec."
    noname "... {w} Hein comment ça ?{w} Hmm... On t'a tendu un guet-apens ?"
    noname "Ta réputation est complètement foutue tu dis ?"
    noname "T'es cramé jusqu'à la mort, hein..."
    hide tinoSmile
    show tinoLaugh
    play sound "audio/fx/collision.mp3" volume 0.2
    noname "WEEEE AHAHAHAHAHAHAH !" with hpunch
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    hide tinoLaugh
    show tinoSmile
    noname "Écoute moi enfoiré, je crois que t'as pas compris le délire."
    noname "T'es un putain de rat mec. {w} Pas un corbeau{w}, t'entends ?"
    noname "T'en as rien à branler de ces crasseux{w}, qu'ils aillent se faire taper dans la raie."
    noname "L'amour c'est pas pour nous, on est des maudits{w}, tu comprends pas vrai ?"
    noname "Tout ce qu'il te reste à faire, c'est de terminer ta putain quête."
    show tinoLaugh
    play sound "audio/fx/collision.mp3" volume 0.2
    noname "REVIENS D'ENTRE LES MORTS LEUR FAIRE DE LA D !!!" with hpunch
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    hide tinoLaugh
    show tinoQuiet
    noname "Moi mon nom c'est Tino...{w} Ah je suis qu'un vestige du passé, j'attends aussi mon heure..."
    show tinoLaugh
    tino "Et n'oublie pas...{w} C'est toutes des folles... tous des SIDA sur pattes..."
    tino "Démarre la camionnette{w} et remonte la pente."
    tino "Et surtout..."
    tino "{b}C'est dans la fosse{w} que naissent les héros.{/b}"
    stop sound
    scene rainStreet with dissolve
    "{b}TO BE CONTINUED...{b}"
    jump credits