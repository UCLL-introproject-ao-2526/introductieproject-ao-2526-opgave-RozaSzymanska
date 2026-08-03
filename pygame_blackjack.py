
import copy
import random
import time
import math
import pygame

pygame.init()
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

symbols = ["spades", "hearts", "diamonds", "clubs"]
deck = []

for value in cards:
    for suit in symbols:
        deck.append(f"{value}{suit}")   

decks = 4

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack!')

fps = 60 
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
show_fireworks = False

colors = [
    (255, 0, 0),
    (0, 255, 0), 
    (0, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (255, 255, 255),
    (230, 230, 250),
    (255, 192, 203)
]

# deal cards by selecting randomly from deck, and make function for one card at a time
def deal_cards(current_hand, current_deck):
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
        card = pygame.image.load(f"img/{player[i]}.jpg")
        card = pygame.transform.scale(card, (120, 220))
        screen.blit(card, (70 + (130 * i), 480))
    
    # if player hasn't finished turn, dealer will hide one card
    for i in range(len(dealer)):
        if i != 0 or reveal:
            card = pygame.image.load(f"img/{dealer[i]}.jpg")
            card = pygame.transform.scale(card, (120, 220))
            screen.blit(card, (70 + (130 * i), 170))
        else:
            screen.blit(brown_card_img, (70 + 130 * i, 170))

def get_card_value(card):
    for value in cards:
        if card.startswith(value):
            return value

def calculate_score(hand):
    # calculate hand score fresh every time, check how many aces we have
    hand_score = 0
    aces_count = 0
    for card in hand:
        value = get_card_value(card)
        # for 2, 3, 4, 5, 6, 7, 8, 9 - just add the number to total
        if value == "A":
            aces_count += 1
            
        for j in range(8):
            if value == cards[j]:
                hand_score += int(value)
        # for 10 and face cards, add 10
        if value in ['10', 'J', 'Q', 'K']:
            hand_score += 10
        # for aces start by adding 11, we'll check if we need to reduce afterwards 
        elif value == 'A': 
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
def check_endgame(hand_act, deal_score, play_score, outcome, totals, add):
    # check end game scenarios if player has stood, busted or blackjacked
    # result: 1- player bust, 2- win, 3- loss, 4- push
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            outcome = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            outcome = 2
        elif play_score < deal_score <= 21:
            outcome = 3
        else: 
            outcome = 4

        if add:
            if outcome == 1 or outcome == 3:
                totals[1] += 1
            elif outcome == 2:
                totals[0] += 1
            else: 
                totals[2] += 1
            add = False
    return outcome, totals, add

class Projectile:
    width = 5
    height = 10
    alpha_decrement = 3

    def __init__(self, x, y, x_vel, y_vel, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.alpha = 255

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.alpha = max(0, self.alpha - self.alpha_decrement)

    def draw(self, win):
        self.draw_rect_alpha(win, self.color + (self.alpha,), (self.x, self.y, self.width, self.height))

    @staticmethod
    def draw_rect_alpha(surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

class Firework:
    radius = 10
    max_projectiles = 50
    min_projectiles = 25
    projectile_vel = 4

    def __init__(self, x, y, y_vel, explode_height, color):
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.explode_height = explode_height
        self.color = color
        self.projectiles = []
        self.exploded = False

    def explode(self):
        self.exploded = True
        num_projectiles = random.randrange(self.min_projectiles, self.max_projectiles)

        if random.randint(0, 1) == 0:
            self.create_circular_projectiles(num_projectiles)
        else:
            self.create_star_projectiles()

    def create_circular_projectiles(self, num_projectiles):
        angle_dif = math.pi*2 / num_projectiles
        current_angle = 0
        vel = random.randrange(self.projectile_vel -1, self.projectile_vel + 1)
        for _ in range(num_projectiles):
            x_vel = math.sin(current_angle) * vel
            y_vel = math.cos(current_angle) * vel
            color = random.choice(colors)
            self.projectiles.append(Projectile(self.x, self.y, x_vel, y_vel, color))
            current_angle += angle_dif

    def create_star_projectiles(self):
        angle_diff = math.pi/4
        current_angle = 0
        num_projectiles = 32
        for i in range(1, num_projectiles + 1):
            vel = self.projectile_vel + (i % (num_projectiles / 8))
            x_vel = math.sin(current_angle) * vel
            y_vel = math.cos(current_angle) * vel
            color = random.choice(colors)
            self.projectiles.append(Projectile(self.x, self.y, x_vel, y_vel, color))
            if i % (num_projectiles / 8) == 0:
                current_angle += angle_diff

    def move(self, max_width, max_height):
        if not self.exploded:
            self.y += self.y_vel
            if self.y <= self.explode_height:
                self.explode()

        projectiles_to_remove = []
        for projectile in self.projectiles:
            projectile.move()

            if projectile.x >= max_width or projectile.x < 0:
                projectiles_to_remove.append(projectile)
            elif projectile.y >= max_height or projectile.y < 0:
                projectiles_to_remove.append(projectile)

        for projectile in projectiles_to_remove:
            self.projectiles.remove(projectile)

    def draw(self, win):
        if not self.exploded:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

        for projectile in self.projectiles: 
            projectile.draw(win)

class Launcher:
    width = 20
    height = 20
    color = 'grey'

    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency #ms
        self.start_time = time.time()
        self.fireworks = []

    def draw(self, win):

        for firework in self.fireworks:
            firework.draw(win)

    def launch(self):
        color = random.choice(colors)
        explode_height = random.randrange(50, 550)
        firework = Firework(self.x + self.width/2, self.y, -10, explode_height, color)
        self.fireworks.append(firework)

    def loop(self, max_width, max_height):
        current_time = time.time()
        time_elapsed = current_time - self.start_time

        if time_elapsed * 1000 >= self.frequency:
            self.start_time = current_time
            self.launch()

        fireworks_to_remove = []
        for firework in self.fireworks:
            firework.move(max_width, max_height)
            if firework.exploded and len(firework.projectiles) == 0:
                fireworks_to_remove.append(firework)

        for firework in fireworks_to_remove:
            self.fireworks.remove(firework)

launchers = [
    Launcher(80, HEIGHT-20, 1800),
    Launcher(250, HEIGHT-20, 2500),
    Launcher(450, HEIGHT-20, 2200),
    Launcher(650, HEIGHT-20, 3000),
    Launcher(820, HEIGHT-20, 1700),
]

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

    if show_fireworks:
        for launcher in launchers:
            launcher.loop(WIDTH, HEIGHT)
            launcher.draw(screen)

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
                    game_deck = copy.deepcopy(deck)
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
                    game_deck = copy.deepcopy(deck)
                    my_hand = []
                    dealer_hand = []
                    reveal_dealer = False
                    hand_active = True
                    show_fireworks = False
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
        if outcome == 2:
            show_fireworks = True

    # it allows a portion of the screen to be updated, instead of the entire area.
    pygame.display.flip()
pygame.quit()