# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define adamu = Character("Adamu")
define noname = Character("???")

define characterSize = .8

init:

    # Custom transitions

    $ flash = Fade(.25, 0, .75, color="#fff")

    # Background Env

    image adamuRoom:
        "background/env/adamu_room.png"

    image streetSchool:
        "background/env/street_school.png"

    image frontSchool:
        "background/env/front_school.png"

    image corridorsSchool:
        "background/env/corridors_school.png"   
    
    image amphiSchool:
        "background/env/amphi_school.png"        
    
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
    
    image adamuSpeakingSerious:
        "characters/adamu/speaking_serious.png"
        zoom characterSize

    image adamuStun:
        "characters/adamu/stun.png"
        zoom characterSize

    image adamuSorry:
        "characters/adamu/sorry.png"
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

# The game starts here.

label start:

    scene adamuRoom

    "{i}Montmorency, dans les tréfons du 95.{/i}"
    "{i}Dans la pénombre de sa chambre miteuse, c’est à la lumière bleutée de son téléphone qu’un jeune homme allait apprendre la nouvelle qui allait tout changer...{/i}"

    show adamuChill with dissolve

    adamu "{i}*Clic clic clic*{/i}"
    adamu "Bordel de cul..."
    adamu "{i}*Clic clic clic*{/i}"
    adamu "Putain de Teemo de merde, on m'a mis mal."
    "{i}*Téléphone vibre, Adam reçoit le message*{/i}"

    scene msgAdmissL2 with dissolve
    pause 2

    adamu "Hmm..."
    adamu "Hein ? Mais non ?"
    adamu "..."

    scene adamuRoom with dissolve
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
    "{i}Trois mois plus tard. Le jour de la rentrée.{/i}"
    
    adamu "Hmm..."
    adamu "Ah ah ! Iyaaaaaaa ! Pas ici Sawa-chan..."
    adamu "Sekusuu..."
    scene adamuRoom
    show adamuSleeping with dissolve
    adamu "Hum ?"
    adamu "..."
    show adamuSurprise with vpunch
    adamu "PUTAIN ZEBIIIIIIIII !!!"
    adamu "BORDEL J'AI ENCORE TROP DORMI !"
    adamu "JE SUIS EN RETARD DES LE 1ER JOUR !!!"
    adamu "Vite, je dois me dépêcher !"


    scene streetSchool with flash
    "{i}*Court en direction de l'école*{/i}"
    show adamuSpeakingSerious with dissolve
    adamu "Plus vite, il faut que j'accèlère."
    adamu "Je me demande comment ça va se passer aujourd'hui, Il faut que je fassse bonne impression."
    "{i}*Cours*{/i}"
    adamu "Je suis presque arrivé, encore un petit effort."
    "{i}*Cours*{/i}"
    adamu "C'est ici !"

    scene frontSchool with fade
    "{i}*Sonnerie*{/i}"
    show adamuSpeakingSerious with dissolve
    adamu "C'est la sonnerie, les cours ont commencé ! Vite !"
    "{i}*Cours*{/i}"

    scene corridorsSchool with fade
    show adamuSpeakingSerious with dissolve

    adamu "Je suis bientôt arrivé, c'est juste après ces marches"
    "{i}*Cours*{/i}"
    adamu " C'est bon ma nouvelle vie m'att..."
    "{i}*BOUM*{/i}" with vpunch


    hide adamuSpeakingSerious
    show adamuStun at right with dissolve
    adamu "Argh..."

    show ayaHurt at left with dissolve
    noname "Ouille..."
    
    hide ayaHurt at left
    show ayaSurprise at left 
    noname "Mince, mes affaires..."
    adamu "Rien de cassé ? Je suis désolé..."

    hide ayaSurprise at left
    show ayaCalm at left 
    noname "Je vais bien, merci."

    adamu "Donne moi ça, je vais t'aider."
    noname "Pas la peine, ne t'en fais pas haha..."
    adamu "Vous voulez bien ?"
    adamu "..."

    show adamuSorry at right
    adamu "Et voilà c'est nickel !"


    noname "Merci, c'est super gentil"
    noname "Allez je file, je vais être en retard pour de bon cette fois."
    adamu "Attends comment tu t'app..."
    noname "A la prochaine, salut !"

    hide ayaCalm with dissolve
    hide adamuSorry

    adamu "Je n'ai pas pu lui demander son nom..."
    adamu "Elle était pressé, c'est sûrement pour ça haha..."
    adamu "Enfin je crois"
    adamu "Haha..."
    adamu "J'espère que je la reverrai, elle était vraiment mignonne..."
    adamu "Voilà la porte de l'amphi."
    adamu "Tout commence ici."

    scene amphiSchool with flash
    "{i}TO BE CONTINUED...{/i}"
    pause 5

    return
