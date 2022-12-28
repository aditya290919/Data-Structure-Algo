import random

suits = ('Hearts','Spades','Diamond','Club')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King',
         'Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
         'Jack':10,'Queen':10,'King':10,'Ace':11}



playing = True

class Card:
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        
        return self.rank + " of " + self.suit


class Deck:
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            
            for rank in ranks:
                
                self.deck.append(Card(suit,rank))
                
                
    def __str__(self):
        
        deck_comp = ''
        
        for card in self.deck:
            
            deck_comp+= '\n' + card.__str__()
            
        return deck_comp
    
    def shuffle(self):
        
        random.shuffle(self.deck)
        
    def pick_one(self):
        
        card_picked = self.deck.pop()

        return card_picked

class Hand:
    
    def __init__(self):
        
        self.cards = []
        self.value = 0
        self.ace = 0
        
    def add_card(self,card):
        
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            
            self.ace +=1
            
    def ace_adjust(self):
        
        while self.value > 21 and self.ace:
            
            self.value -= 10
            self.ace -=1
            

class Chips:
    
    def __init__(self,total = 500):
        
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        
        self.total+=self.bet
        
    def lose_bet(self):
        
        self.total-=self.bet


def take_bet(chips):
    
    while True:
        
        try:
            
            chips.bet = int(input('How many chips do you want to bet?'))
            
        except:
            
            print('Only integers value are valid!')
            
        else:
            
            if chips.bet > chips.total:
                
                print('sorry you dont have enough chips to bet!')
                
                
            else:
                
                break


def hit(deck,hand):
    
    pulled_card = deck.pick_one()
    hand.add_card(pulled_card)
    hand.ace_adjust()


def hit_stand(deck,hand):
    
    global playing
    
    while True:
        
        x = input('enter h for hit and s stand:  ')
        
        if x[0].lower()=='h':
            
            hit(deck,hand)
            
        elif x[0].lower()=='s':
            
            print("player doesn't want hit any card!")
            
            playing = False
            
        else:
            print('Sorry you did not enter valid input!')
            
            continue
            
        break
            

def show_some(player,dealer):
    
    # it will show one of the dealer's card
    # and both(all) of the players cards
    
    print('\n Dealer hand: ')
    print('first card hidden')
    print(dealer.cards[1])
    
    
    print('\n player cards: ')
    for card in player.cards:
        
        print(card)
    
def show_all(player,dealer):
    
    
    # show all of the dealers cards
    # show all of the players cards.
    
    print('dealers cards')
    for card in dealer.cards:
        
        print(card)
    
#     print('dealers cards: ', *dealer.cards,sep= '\n')
    
    
    
    print('player cards')
    for card in player.cards:
        
        print(card)


def player_burst(player,dealer,chips):
    print('player burst')
    chips.lose_bet()
    
def player_win(player,dealer,chips):
    print('player win')
    chips.win_bet()
    
def dealer_burst(player,dealer,chips):
    print('player wins')
    chips.win_bet()
    
def dealer_win(player,dealer,chips):
    print('dealer win')
    chips.lose_bet()
    
def push(player,dealer):
    print('dealer and player tie. PUSH!')


while True:
    
    print('Welcome to black jack')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.pick_one())
    player_hand.add_card(deck.pick_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.pick_one())
    dealer_hand.add_card(deck.pick_one())
    
    player_chips = Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        hit_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value>21:
            player_burst(player_hand,dealer_hand,player_chips)
            break
            
    if player_hand.value<=21:
        
        while dealer_hand.value<player_hand.value:
            
            
            hit(deck,dealer_hand)
            
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value>21:
            
            dealer_burst(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            
            player_win(player_hand,dealer_hand,player_chips)
            
            
        
        elif dealer_hand.value > player_hand.value:

            dealer_win(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)


    print(f'\n Player total chips are at: {player_chips.total}')


    play_again = input('would you like to play again? y or n')

    if play_again[0].lower() == 'y':

        continue

    else:
        print('user doesnt want to play again')

        break
        
    
    
    
