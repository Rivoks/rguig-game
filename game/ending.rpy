label ending:
    scene black with dissolve
    stop music fadeout 3.0
    narrator "{i}Adamu avait cessé de suivre les cours depuis plusieurs jours.{/i}"
    narrator "{i}En un jour pluvieux, il n'arrivait plus à supporter sa vie.{/i}"

    play sound "audio/fx/rain.mp3" volume 0.3 loop fadeout 5
    play music "audio/ost/bakamitai_radio.mp3" volume 0.1 loop
    scene rainStreet with dissolve
    narrator "{i}Là, dans cette ruelle aux sournois appels.{i}"
    narrator "{i}Adamu s'en allait marcher sans savoir où aller.{i}"
    narrator "{i}Finalement il s'arrêta devant une taverne malfamée. {w}Les vrais rats reconnaissent les ratelières.{i}"

    stop sound
    scene tavernDark with dissolve
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    narrator "{i}Cette enseigne semblait être fréquentée par des désoeuvrés.{/i}"
    narrator "{i}Les gémissements d'agonies se faisaient entendre de toute part.{/i}"
    narrator "{i}Adamu commanda un bon vieux verre de Ricard pour broyer du noir.{/i}"
    noname "Bah alors mon petit gars, qu'est-ce qu'il t'arrive à toi ?"
    show tinoSmile with dissolve
    noname "T'as pas l'air dans ton assiette, hein..."
    noname "Qu'est-ce tu dis ? {w} Ta gonzesse vient de te quitter ?"
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
    noname "... {w} Hein comment ça ?{w} Hmm... C'était ta première meuf ?"
    noname "Tu lui as tout donné et elle t'a quitté..."
    hide tinoSmile
    show tinoLaugh
    play sound "audio/fx/collision.mp3" volume 0.2
    noname "WEEEE AHAHAHAHAHAHAH !" with hpunch
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    hide tinoLaugh
    show tinoSmile
    noname "Écoute moi enfoiré, je crois que t'as pas compris le délire."
    noname "T'es un putain de rat mec. {w} Pas un corbeau{w}, t'entends ?"
    noname "Tout ce qu'il te reste à faire, c'est de terminer ta putain de quête."
    noname "L'amour c'est pas pour nous, on est des maudits{w}, tu comprends pas vrai ?"
    show tinoLaugh
    play sound "audio/fx/collision.mp3" volume 0.2
    noname "ALLEZ, RETOURNE EN MISSION MON VIEUX !" with hpunch
    play sound "audio/fx/bar_ambiance.mp3" volume 0.1 loop
    hide tinoLaugh
    show tinoQuiet
    noname "Moi mon nom c'est Tino...{w} Ah je suis qu'un vestige du passé, j'attends aussi mon heure..."
    show tinoLaugh
    tino "Et n'oublie pas...{w} C'est toutes des folles..."
    tino "Démarre la camionnette{w} et remonte la pente."
    stop sound
    scene rainStreet with dissolve
    "{b}TO BE CONTINUED...{b}"
    jump credits
