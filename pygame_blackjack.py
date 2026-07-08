# import the modules - import statements will always go at the top
# "if you know you are going to have some kind of RNG like in this case shuffling the deck and we know we are going to want to make copies of the deck so we dont overwrite our original one we want to import copy and random in the beginning." 

import copy
import random
import pygame

# game variables
# initialize all pygame modules that are required for the game (graphics, fonts, sounds)
pygame.init()
# cards are strings because J, Q, K and A are letters
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4
# create a copy of the full game deck
game_deck = copy.deepcopy(decks * one_deck)

# setting up a pygame window
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack!')

# Frames Per Seconds: controls how many times the game updates every second
fps = 60 
# clock that keep the game running at the chosen fps
timer = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)

active = True
# win, loss, draw/tie
records = [0, 0, 0]
player_score = 0
dealer_score = 0

# draw game conditions and buttons
def draw_game(active, record):
    button_list = []
    # iif the game is not active, only show deal button
    if not active: 
        # It draws an rectangle (300 = width and 100 = height)
        # the last two argments are optional. (0 = filled, 5 = round corners)
        deal = pygame.draw.rect(screen, 'white', [150, 20, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [150, 20, 300, 100], 3, 5)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, (165, 50))
        button_list.append(deal)
    # if the game is active, show hit/stand buttons and the score
    else: 
        hit = pygame.draw.rect(screen, 'white', [0, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [0, 700, 300, 100], 3, 5)
        hit_text = font.render('HIT ME', True, 'black')
        screen.blit(hit_text, (55, 735))
        button_list.append(hit)

        stand = pygame.draw.rect(screen, 'white', [300, 700, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [300, 700, 300, 100], 3, 5)
        stand_text = font.render('STAND', True, 'black')
        screen.blit(stand_text, (355, 735))
        button_list.append(stand)

        score_text = smaller_font.render(f'Wins: {record[0]}     Losses: {record[1]}     Draws:  {record[2]}', True, 'white') 
        screen.blit(score_text, (15, 840))
    return button_list

# main game loop
run = True
while run: #the code will repeat ass long the game is running 
    # control the frame rate and draw the background
    timer.tick(fps)
    screen.fill('black')
    buttons = draw_game(active, records)

    # check if the player closed the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False #if we hit the quit button we want to run to be equal to False
    # it allows a portion of the screen to be updated, instead of the entire area.
    pygame.display.flip()
pygame.quit()