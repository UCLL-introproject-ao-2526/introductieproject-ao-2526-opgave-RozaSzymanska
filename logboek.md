TUTORIAL

## 08 julie 2026
Vandaag ben ik gestart met de tutorial. Ik heb de eerste game variables aangemaakt, een game window opgezet en de main game loop geschreven. De while loop zorgt ervoor dat het spel blijft draaien zolang 'run' true is. Verder heb ik de draw game functie gevolgd waarin de knoppen en scoretekst op het scherm getekend worden. In deze functie heb ik de parameter naam 'active' gebruikt in plaats van 'act' zoals in de tutorial, omdat ik die naam duidelijker en makkelijker te begrijpen vind.

Ik ben geraakt tot het onderdeel waarin de deal button wordt afgehandeld. Tijdens het volgen van de tutorial heb ik ondertitels aangezet en belangrijke uitleg als commentaar bij de juiste regel code gezet. Zo kan ik later makkelijker begrijpen wat de code doet en sneller verder werken. Volgende keer werk ik verder vanaf dat punt.

## 09 julie 2026
Vandaag heb ik verder gewerkt aan de blackjack tutorial. Eerst heb ik het mouse click event toegevoegd zodat de knoppen kunnen reageren op muisklikken. 
Daarna heb ik de initial deal ingevoerd, zodat het speler en de dealer automatisch hun eerste kaarten krijgen wanneer een nieuw spel start. Vervolgens heb ik de functies: draw_cards, deal_cards, calculate_score en draw_scores toegevoegd. Met deze functies worden de kaarten uitgedeeld, op het scherm getekend en wordt de score van het speler en de dealer berekend en weergegeven. Dan ook nog de logica toegevoegd waarbij de score van de dealer pas berekend wordt wanneer het speler zijn beurt heef beeindigt. Ook zijn de knoppen 'hit me' en 'stand' werkend gemaakt. Daarna heb ik ook ervoor gezorgd dat het spel automatisch stopt wanneer het speler score van 21 of meer behaald.

Op ongeveer 26:26 in de tutorial heb ik mijn code getest en ik kreeg een fout: (AttributeError: 'pygame.event.Event' object has no attribute 'position') Ik had per ongeluk event.position geschreven in plaats van event.pos zoals in de tutorial binnen de collidepoint() controle. Na verbeteren van de naam werkte alles weer.

Later kreeg ik nog een andere fout: [pygame.draw.rect(screen, 'white', [70 + (70 * i), 460, (5 * i), 120, 220], 0, 5)
TypeError: rect argument is invalid] ik had blijkbaar vijf waarden ingegeven in plaats van vier [x, y, width, height]. Het kwam omdat ik tussen 460 en (5 * i) een komma heb gezet in plaats van een +.

Ik moest dit deel van de tutorial een paar keer opnieuw bekijken omdat de uitleg hier sneller ging en ik niet meer kon volgen. Uiteindelijk begreep ik het wel. Ik had gehoopt om de hele tutorial vandaag af te werken, maar de laatste vijftien minuten ga ik toch op een ander dag doen. 

## 14 julie 2026
Ik ben begonnen met het nalezen van het logboek, om te zien wat ik in de vorige deel had gemaakt. 

In dit laatste deel van de tutorial heb ik de variabelen outcome en add_score toegevoegd. Ook heb ik de functie check_endgame() ingevoerd. Deze functie controleert wanneer een spelronde afgelopen is en bepaalt of het speler wint, verliest, busted is of gelijk speelt. Daarnaast wordt in de functie draw_game gecontroleerd of er een resultaat is, zodat het juiste bericht en de knop 'new hand' worden weergegeven.

Na het beeindigen van de tutorial merkte ik op dat ik twee keer de variabele outcome gedefinieerd had, wat overbodig is. Dus ik heb een van de twee verwijdert.

probleem 1: vertraging bij 'player busted' resultaat
    Wanneer het speler meer dan 21 punten had, duurde het heel lang voordat de melding 'player busted' verscheen. Eerst heb ik de functie check_endgame nagekeken, maar daar vond ik niet direct een fout. Ik had dus de laatste deel van de tutorial opnieuw bekeken en zag direct dat de laatste if controle in de main game loop verkeerd was ingesprongen. Ik had die per ongeluk in de for loop gezet en niet erbuiten. 

probleem 2: De kaarten van de dealer blijven zichtbaar bij een nieuwe hand. 
    Bij het starten van een nieuwe hand werd de eerste kaart van de dealer niet meer verborgen. Daarom heb ik alle plaatsen nagekeken waar de variabele reveal_dealer gebruikt werd. Ik merkte op dat ik deze nergens opnieuw op False zette bij het starten van een nieuwe spelronde. Ik heb dit toegevoegd op de plaatsen waar een nieuwe hand wordt geinitialiseerd. 

probleem 3: De knop 'stand' werkte niet 
    In het begin reageerde de knop 'stand' niet wanneer ik erop klikte. Ik heb dit probleem als laatste gehouden, omdat de andere fouten eenvoudiger leken om op te lossen. Toen ik het spel verder aan het testen was, bleek de knop uiteindelijk weer correct te werken. Ik weet niet exact wat dit probleem heeft opgelost. 

Nadat ik deze fouten had opgelost heb ik het spel nog enkele keren getest. Ik had geen andere fouten opgemerkt. De grafische afwerking is niet volledig uitgewerkt maar dat ga ik waarschijnlijk verbeteren in de uitbreidingsfase. 