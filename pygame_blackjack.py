# import the modules - import statements will always go at the top

import copy
import random
import pygame

# game variables
# initialize all pygame modules that are required for the game (graphics, fonts, sounds)
pygame.init()
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack!')

# Frames Per Seconds: controls how many times the game updates every second
fps = 60 
# clock that keep the game running at the chosen fps
timer = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)

brown_card_img = pygame.image.load('img/playing_card_brown.png')
brown_card_img = pygame.transform.scale(brown_card_img, (120, 220))
black_card_img = pygame.image.load('img/playing_card_black.png')
black_card_img = pygame.transform.scale(black_card_img, (120, 220))

game_status = "start"
# win, loss, draw/tie
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
add_score = False 
results = ['', 'Player busted o_O', 'Player wins! :)', 'Dealer wins :(', 'Tie game...']

# deal cards by selecting randomly from deck, and make function for one card at a time
def deal_cards(current_hand, current_deck):
    # it picks a random card from the deck
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    return current_hand, current_deck

# draw scores for player and dealer on screen
def draw_scores(player, dealer):
    screen.blit(smaller_font.render(f'Player: {player}', True, 'white'), (50, 420))
    if reveal_dealer:
        screen.blit(smaller_font.render(f'Dealer: {dealer}', True, 'white'), (50, 120))

# draw cards visually onto screen
def draw_cards(player, dealer, reveal):
    for i in range(len(player)):
        pygame.draw.rect(screen, 'white', [70 + (130 * i), 480, 120, 220], 0, 5)
        screen.blit(smaller_font.render(player[i], True, 'black'), (77 + 130 * i, 480 + 5 * 1))
        screen.blit(smaller_font.render(player[i], True, 'black'), (160 + 130 * i, 655 + 5 * 1))
    
    # if player hasn't finished turn, dealer will hide one card
    for i in range(len(dealer)):
        pygame.draw.rect(screen, 'white', [70 + (130 * i), 170, 120, 220], 0, 5)
        if i != 0 or reveal:
            screen.blit(smaller_font.render(dealer[i], True, 'black'), (75 + 130 * i, 170 + 5 * 1))
            screen.blit(smaller_font.render(dealer[i], True, 'black'), (145 + 130 * i, 345 + 5 * 1))
        else:
            screen.blit(brown_card_img, (70 + 130 * i, 170))

def calculate_score(hand):
    # calculate hand score fresh every time, check how many aces we have
    hand_score = 0
    aces_count = hand.count('A')
    for i in range(len(hand)):
        # for 2, 3, 4, 5, 6, 7, 8, 9 - just add the number to total
        for j in range(8):
            if hand[i] == cards[j]:
                hand_score += int(hand[i])
        # for 10 and face cards, add 10
        if hand[i] in ['10', 'J', 'Q', 'K']:
            hand_score += 10
        # for aces start by adding 11, we'll check if we need to reduce afterwards 
        elif hand[i] == 'A': 
            hand_score += 11
    # determine how many aces need to be 1 instead of 11 to get under 21 if possible
    if hand_score > 21 and aces_count > 0:
        for i in range(aces_count):
            if hand_score > 21:
                hand_score -= 10
    return hand_score

# draw game conditions and buttons
def draw_game(game_status, record, result):
    button_list = []
    if game_status == "start": 
        brown_card_rotate = pygame.transform.rotate(brown_card_img, 30)
        screen.blit(brown_card_rotate, (350, 50))
        black_card_rotate = pygame.transform.rotate(black_card_img, -35)
        screen.blit(black_card_rotate, (350, 450))

        welcome_text = font.render('Blackjack', True, 'White')
        screen.blit(welcome_text, (350, 350))

        # the last two argments are optional. (0 = filled, 5 = round corners)
        start_btn = pygame.draw.rect(screen, 'darkgreen', [330, 760, 240, 80], 0, 5)
        pygame.draw.rect(screen, 'gray', [330, 760, 240, 80], 3, 5)
        start_btn_text = smaller_font.render('Start Game!', True, 'white')
        text_rect = start_btn_text.get_rect(center=start_btn.center)
        screen.blit(start_btn_text, text_rect)
        button_list.append(start_btn)

    elif game_status == "playing": 
        hit = pygame.draw.rect(screen, 'darkgreen', [200, 760, 240, 80], 0, 5)
        pygame.draw.rect(screen, 'grey', [200, 760, 240, 80], 3, 5)
        hit_text = smaller_font.render('Hit me', True, 'white')
        text_rect = hit_text.get_rect(center=hit.center)
        screen.blit(hit_text, text_rect)
        button_list.append(hit)

        stand = pygame.draw.rect(screen, 'darkgreen', [475, 760, 240, 80], 0, 5)
        pygame.draw.rect(screen, 'grey', [475, 760, 240, 80], 3, 5)
        stand_text = smaller_font.render('Stand', True, 'white')
        text_rect = stand_text.get_rect(center=stand.center)
        screen.blit(stand_text, text_rect)
        button_list.append(stand)

        #pygame.draw.rect(screen, 'darkgreen', [0, 0, 900, 100], 0)
        #pygame.draw.rect(screen, 'grey', [0, 0, 900, 100], 3)

        score_text = smaller_font.render(f'Wins: {record[0]}     Losses: {record[1]}     Draws:  {record[2]}', True, 'white') 
        screen.blit(score_text, (200, 30))

    elif game_status == "result":
        score_text = smaller_font.render(f'Wins: {record[0]}     Losses: {record[1]}     Draws:  {record[2]}', True, 'white') 
        screen.blit(score_text, (200, 30))
        screen.blit(smaller_font.render(results[result], True, 'white'), (300, 80))
        new_hand_btn = pygame.draw.rect(screen, 'darkgreen', [300, 760, 240, 80], 0, 5)
        pygame.draw.rect(screen, 'white', [300, 760, 240, 80], 3, 5)
        new_hand_btn_text = smaller_font.render('New Hand', True, 'white')
        text_rect = new_hand_btn_text.get_rect(center=new_hand_btn.center)
        screen.blit(new_hand_btn_text, text_rect)
        button_list.append(new_hand_btn)
    return button_list

# check endgame conditions function
# outcome is results, records are totals 
def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    # check end game scenarios if player has stood, busted or blackjacked
    # result: 1- player bust, 2- win, 3- loss, 4- push
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            result = 2
        elif play_score < deal_score <= 21:
            result = 3
        else: 
            result = 4

        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else: 
                totals[2] += 1
            add = False
    return result, totals, add

# main game loop
run = True
while run:
    # control the frame rate and draw the background
    timer.tick(fps)
    screen.fill('darkgreen')
    # initial deal to player and dealer
    if initial_deal:
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)  
        initial_deal = False
    if game_status == "playing": 
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)
    elif game_status == "result":
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        draw_scores(player_score, dealer_score)
    buttons = draw_game(game_status, records, outcome)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            # only allow clicking DEAL when no game is running
            if game_status == "start":
                # check if the DEAL button was clicked
                start_btn = buttons[0]
                if start_btn.collidepoint(event.pos):
                    # start a new game
                    game_status = "playing"
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    reveal_dealer = False
                    hand_active = True
                    outcome = 0
                    add_score = True
                    dealer_score = 0
                    player_score = 0
            elif game_status == "playing":
                hit_btn = buttons[0]
                stand_btn = buttons[1]
                if hit_btn.collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                elif stand_btn.collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
            elif game_status == "result":
                new_hand_btn = buttons[0]
                if new_hand_btn.collidepoint(event.pos):
                    game_status = "playing"
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    reveal_dealer = False
                    hand_active = True
                    dealer_score = 0
                    player_score = 0
                    outcome = 0
                    add_score = True

    # if player busts, automatically end turn - treat like a stand 
    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

    if outcome != 0 and game_status == "playing":
        game_status = "result"

    # it allows a portion of the screen to be updated, instead of the entire area.
    pygame.display.flip()
pygame.quit()