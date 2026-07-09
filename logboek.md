## 08 julie 2026
Vandaag ben ik gestart met de tutorial. Ik heb de eerste game variables aangemaakt, een game window opgezet en de main game loop geschreven. De while loop zorgt ervoor dat het spel blijft draaien zolang 'run' true is. Verder heb ik de draw game functie gevolgd waarin de knoppen en scoretekst op het scherm getekend worden. In deze functie heb ik de parameter naam 'active' gebruikt in plaats van 'act' zoals in de tutorial, omdat ik die naam duidelijker en makkelijker te begrijpen vind.

Ik ben geraakt tot het onderdeel waarin de deal button wordt afgehandeld. Tijdens het volgen van de tutorial heb ik ondertitels aangezet en belangrijke uitleg als commentaar bij de juiste regel code gezet. Zo kan ik later makkelijker begrijpen wat de code doet en sneller verder werken. Volgende keer werk ik verder vanaf dat punt.

## 09 julie 2026
Vandaag heb ik verder gewerkt aan de blackjack tutorial. Eerst heb ik het mouse click event toegevoegd zodat de knoppen kunnen reageren op muisklikken. 
Daarna heb ik de initial deal ingevoerd, zodat de speler en de dealer automatisch hun eerste kaarten krijgen wanneer een nieuw spel start. Vervolgens heb ik de functies: draw_cards, deal_cards, calculate_score en draw_scores toegevoegd. Met deze functies worden de kaarten uitgedeeld, op het scherm getekend en wordt de score van de speler en de dealer berekend en weergegeven. Dan ook nog de logica toegevoegd waarbij de score van de dealer pas berekend wordt wanneer de speler zijn beurt heef beeindigt. Ook zijn de knoppen 'hit me' en 'stand' werkend gemaakt. Daarna heb ik ook ervoor gezorgd dat het spel automatisch stopt wanneer de speler score van 21 of meer behaald.

Op ongeveer 26:26 in de tutorial heb ik mijn code getest en ik kreeg een fout: (AttributeError: 'pygame.event.Event' object has no attribute 'position') Ik had per ongeluk event.position geschreven in plaats van event.pos zoals in de tutorial binnen de collidepoint() controle. Na verbeteren van de naam werkte alles weer.

Later kreeg ik nog een andere fout: [pygame.draw.rect(screen, 'white', [70 + (70 * i), 460, (5 * i), 120, 220], 0, 5)
TypeError: rect argument is invalid] ik had blijkbaar vijf waarden ingegeven in plaats van vier [x, y, width, height]. Het kwam omdat ik tussen 460 en (5 * i) een komma heb gezet in plaats van een +.

Ik moest dit deel van de tutorial een paar keer opnieuw bekijken omdat de uitleg hier sneller ging en ik niet meer kon volgen. Uiteindelijk begreep ik het wel. Ik had gehoopt om de hele tutorial vandaag af te werken, maar de laatste vijftien minuten ga ik toch op een ander dag doen. 