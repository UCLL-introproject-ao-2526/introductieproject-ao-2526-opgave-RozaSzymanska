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

EIGEN UITBREIDING

## 23 julie 2026 - 27 julie 2026

Eerst besloot ik om het design van de spel te veranderen. Hiervoor heb ik inspiratie gezocht op google. Uiteindelijk heb ik een ontwerp gevonden dat mij aansprak, namelijk: https://medium.com/strategio/cv-project-blackjack-game-d128730eff4b 
Ik heb ervoor gekozen om die als inspiratiebron te gebruiken voor een paar elementen van het spel.

Eerste stap was het vergroten van de breedte van het spelvenster en het aanpassen van de achtergrondkleur naar donkergroen, zodat het meer lijkt op een echte Blackjack tafel. Daarna heb ik de tekst op de startknop gewijzigd van "DEAL HAND" naar "Start Game", omdat ik hoofdletters minder mooi vond en de nieuwe tekst duidelijker is voor de gebruiker.

Daarnaast heb ik een titel toegevoegd aan het startscherm en twee speelkaarten als decoratie geplaatst, een boven en een onder de titel, net zoals in mjin inspiratieontwerp. Hiervoor heb ik een vectorafbeelding met vrije licentie gebruikt. Ik heb de uitleg om een afbeelding toe te voegen aan een pygame hier gevonden: https://pythonprogramming.net/displaying-images-pygame .Vervolgens zocht ik op hoe ik de kaarten kon roteren, hiervoor heb ik deze website gevonden: https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate Daar heb ik op de search examples geklikt wat mij naar een Github pagina bracht en daar vond ik genoeg voorbeelden om het uit te proberen in mijn code.

Na het startscherm heb ik het speelscherm aangepast. Als eerste heb ik de hit me en stand knoppen dezelfde stijl gegeven als de startknop en ze opnieuw gepositioneerd zodat de in het midden staan in de bredere spelweergave. 
Het was een beetje prullen omdat ik telkens de positie van de tekst moest aanpassen wanneer ik de knoppen verplaatste, dus ik heb gezocht of er een optie is om die tekst te centreren ten opzichte van de knop zelf zoals het ook mogelijk is in css. Hiervoor heb ik verschillende bronnen geraadpleegd maar de meest helpende website was deze: https://stackoverflow.com/questions/23982907/how-to-center-text-in-pygame 

Daarnaast heb ik de kaarten naast elkaar gepositioneerd in plaats van op elkaar wat mij meer aansprak. Dan heb ik de verborgen dealerkaart aangepast, in plaats van drie vraagtekens heb ik de achterkant van een spelkaart weergegeven zoals op het startscherm. Ik heb ook de rode en blauwe randen rond de kaarten verwijdert. Dan heb ik de lettertype van de kaarten verkleind door gebruik te maken van smaller_font. De onderste getal op de kaart heb ik meer naar rechts geplaatst. Bij de kaart met waarde 10 komt de tekst soms uit de kaart. Ik heb ervoor gekozen om dit zo te laten omdat het opschuiven naar links er voor zal zorgen dat de kaarten met 1 cijfer minder mooi uitgelijnd zouden worden.

Vervolgens heb ik gewerkt aan de weergave van het resultaat. Hiervoor heb ik de new hand knop dezelfde opmaak gegeven als de overige knoppen en die te verplaatsen naar beneden. Het probleem was dat de oude knoppen zichtbaar bleven wanneer een hand afgelopen was. Eerst heb ik dus de knoppen en kaarten naar beneden verschoven zodat de resultaat zin onder de scoreboard kan verschijnen. Wat betreft de knoppen had ik een idee om hiervoor een apart resultaatscherm te maken waarop alleen de new hand knop wordt weergegeven.

Hier zat ik het langst vast want in de code werd de overgang tussen het startscherm en de speelscherm overgeschakeld door de boolean variabele active. Wanneer active gelijk was aan False, werd het startscherm weergegeven. Wanneer active gelijk was aan True, werd het speelscherm getoond. Maar voor mijn idee had ik een derde scherm nodig die de resultaatscherm zal tonen en ik wist niet hoe ik precies het in elkaar moest krijgen alleen met die active variabele. Daarom heb ik ervoor gekozen om een nieuwe variabele te gebruiken: game_status. Zo kon ik veel makkelijker bepalen welk scherm moest worden weergegeven. Hiervoor heb ik drie waardes voor gebruikt, namelijk: start, playing en result. 

Om deze wijziging in te voeren heb ik de volledige code van begin tot einde overlopen en alle controles aangepast die gebruikmaakten van de variabele active. In de functie draw_game() heb ik eerst de parameter active vervangen door game_status. De if not active controle en de else structuur heb ik vervangen door if game_status == "start", "playing" en "result". Hierdoor heb ik de code voor het tekenen van de resultaatscherm rechtstreeks in de result controle toegevoegd. Daarnaast heb ik ook enkele variabelen hernoemd zodat ze duidelijker beschrijven waarvoor ze dienen. Bv. variabele deal heb ik gewijzigd naar start_btn en deal_text naar start_btn_text. 

In de while loop heb ik alle controles met active verwijdert en vervangen door controles op game_status. Ik heb ook onderaan een extra controle toegevoegd. Wanneer de functie check_endgame() een outcome teruggeeft die niet 0 is en terwijl het spel zich nog in de status "playing" bevindt, wordt de game_status automatisch gewijzigd naar result. Hierdoor verschijnt het resultaatscherm automatisch zodra een hand is afgelopen. 

Na een paar keer testen van het spel heb ik toch ook de scoretekst in kleinere font gezet en van score[] heb ik dealer of player bijgeschreven zodat het iets duidelijker is van wie die punten zijn en ook heb ik die aan de linkerkant uitgeleind zodat ze minder storen tijdens het spelen. 

Ten slotte heb ik in de event-loop de knoppen duidelijkere namen gegeven zoals start_btn, hit_btn, stand_btn en new_hand_btn. Hierdoor is het voor mij duidelijker over welke knop het gaat.

## 03 augustus 2026

Om te starten heb ik het spel eerst opnieuw gespeeld om te zien of alles nog correct werkt. Tijdens het spelen kreeg ik het idee om de interface nog eens te veranderen naar echte afbeeldingen van speelkaarten. Ik wilde dat er met alle kaarten gespeeld werd, met alle vier symbolen en twee verschillende kleuren zodat het wat kleurrijker wordt. 

Ik heb eerst een vectorafbeelding met alle speelkaarten gerbuikt. Daarna heb ik alle kaarten apart uitgeknipt en opgeslagen als aparte afbeeldingen. De bestandsnamen heb ik zo gekozen dat eerst de kaartwaarde staat, gevolgd door het symbool. Dit idee kende ik nog uit een oefening in javascript die ik ooit maakte, waar de naam van het bestand gebruikt werd om informatie uit af te leiden. En dan maakte ik ook een lijst met de vier symbolen.

In mijn eerste poging gebruikte ik een for loop waarin ik een willekeurige index koos om een kaartwaarde en een symbool te selecteren. Maar dat bleek geen goede oplossing te zijn, omdat het geen volledige deck maakte en dezelfde kaart meerdere keren kon voorkomen. Dit heb ik opgelost met een geneste for loop waar ik eerst alle kaartwaarde doorloop en vervolgens alle symbolen waardoor elke mogelijke combinatie wordt gemaakt.

Dan heb ik overal one_deck = 4 * cards vervangen door een kopie van de deck, omdat deck al alle kaarten bevat. Vervolgens heb ik in de functie draw_cards de witte rechthoek en de kaartwaarde verwijdert en in plaats daarvan de juiste kaartafbeelding geladen. 

Daarna moest ik ook nog de scoreberekening aanpassen, omdat de kaarten nu bestandsnamen hebben zoals Qhearts kon de functie de kaartwaarde niet meer rechtstreeks uithalen. Daarom heb ik een aparte functie gemaakt: get_card_value gemaakt waar ik controleer of de bestandsnaam begint met een waarde uit de lijst cards. Dan geeft het de value terug om ermee verder te kunnen berekenen. 

Tijdens het testen kwam ik verschillende fouten tegen die ik telkens rechtstreeks verbeterde. Voorbeelden van fouten: 

Probleem 1: NameError
    Ik wou de afbeelding van de kaarten schalen buiten de functie draw_cards zoals bij de afbeeldingen van de achterkant van de kaarten, maar de fout gaf aan dat de variabele card nog niet gedefinieerd was. Dus heb ik de schalen van de kaart in de functie gezet om de fout te vermijden. 

Probleem 2: UnboundLocalError
    Ik schreef: value = get_card_value(value) in de functie calculate_score terwijl value nog niet bestond. Ik verwarde de huidige kaart (card) met de kaartwaarde (value). 

Probleem 3: FileNotFoundError
    Ik gebruikte de extensie .png in plaats van .jpg in de kaartafbeeldingen waardoor Pygame de bestanden niet kon vinden. 

Dan heb ik het spel opnieuw geprobeerd en merkte ik snel op dat na het klikken van new hand het spel opeens stopte. Er bleek dat ik op een plaats nog de oude variabele one_deck gebruikte in plaats van het nieuwe deck. Dan werkte alles weer opnieuw. 

Ten slotte wou ik nog een speciaal effect toevoegen wanneer de speler een hand gewonnen heeft. Daarvoor ben ik op zoek gegaan naar een vuurwerkeffect en ben ik deze tutorial tegengekomen: https://www.youtube.com/watch?v=8nIi2x2m6yE&t=276s 

Ik heb eerst de volledige code van de tutorial uitgewerkt in een apart bestand. Daarna heb ik nagedacht over welke delen ik precies nodig had en waar ik die in mijn eigen code moest toevoegen. Ik heb hiervoor eerst de nodige imports, classes en variabelen overgenomen. Vervolgens heb ik een variabele show_fireworks aangemaakt met als beginwaarde False. In tegenstelling tot het vuurwerkproject wil ik de vuurwerkeffecten alleen tonen wanneer de speler gewonnen heeft, dus ik moet kunnen bijhouden wanneer ze wel en niet mogen verschijnen. Ik heb deze variabele op True gezet wanneer de outcome gelijk is aan 2 en opnieuw op False wanneer de speler op de knop new hand klikt. 

Daarna heb ik de launcher objecten aangemaakt en de for loop die de launchers bijwerkt en tekent in de main loop geplaatst. Deze heb ik genest in een if-controle zodat de vuurwerkeffecten alleen worden uitgevoerd wanneer show_fireworks op True staat.

Na het uittesten merkte ik op dat het vuurwerk onder de kaarten werd getekend in plaats van erboven. Ik herinnerde mij direct dat ik vroeger op school in p5.js ook al eens een gelijkaardig probleem had. Ik wist nog dat dit te maken had met de volgorde waarin alles getekend wordt. Dus ik heb de code van de  launchers naar een lagere plaats in de main loop verplaatst, zodat het vuurwerk als laatste getekend wordt. En het heeft inderdaad het probleem opgelost. 

Ten slotte heb ik ook nog de hoogte waarop de vuurpijlen ontploffen aangepast en ook de snelheid van de vuurpijlen. De rechthoek van de launcher heb ik ook verwijdert zodat alleen het vuurwerk zichtbaar blijft en het wat mooier eruitziet. 