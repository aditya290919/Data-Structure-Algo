import random

suits = ('Hearts','Spades','Diamond','Club')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King',
         'Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
         'Jack':11,'Queen':12,'King':13,'Ace':14}





class Cards():

	def __init__(self,suit,rank):

		self.suit = suit
		self.rank = rank
		self.value = values[rank]
		

	def __str__(self):

		return self.rank + " of " + self.suit


class Deck():

	def __init__(self):


		self.all_cards = []

		for suit in suits:

			for rank in ranks:

				created_card = Cards(suit,rank)

				self.all_cards.append(created_card)


	def shuffle(self):

		random.shuffle(self.all_cards)

	def deal_one(self):

		return self.all_cards.pop()





class Player():

	def __init__(self,name):

		self.name = name

		self.all_cards = []



	def remove_card(self):

		return self.all_cards.pop(0)


	def add_card(self,new_card):

		if type(new_card) == type([]):

			self.all_cards.extend(new_card)

		else:
			self.all_cards.append(new_card)


	def __str__(self):

		return f"{self.name} has {len(self.all_cards)} cards"


player1 = Player('One')
player2 = Player('Two')



new_deck = Deck()

new_deck.shuffle()


for x in range(26):

	player1.add_card(new_deck.deal_one())

	player2.add_card(new_deck.deal_one())



game_on = True

round_game = 0

while game_on:

	round_game+=1

	print(f'{round_game} rounds')

	if len(player1.all_cards) == 0:

		print('player1 is out of cards! player2 wins')

		game_on = False

		break

	if len(player2.all_cards) == 0:

		print('player2 is out of cards! player1 wins')

		game_on = False

		break


	player1_cards = []

	player1_cards.append(player1.remove_card())

	player2_cards = []

	player2_cards.append(player2.remove_card())


	war_on = True

	while war_on:

		if player1_cards[-1].value < player2_cards[-1].value:

			player1_cards.append(player1_cards)
			player1_cards.append(player2_cards)

			war_on = False

		



		elif player2_cards[-1].value < player1_cards[-1].value:



			player2_cards.append(player2_cards)
			player2_cards.append(player1_cards)

			war_on = False

		


		else:


			if len(player1.all_cards) < 5:

				print('player2 wins')

				game_on = False

				break

			elif len(player2.all_cards) < 5:

				print('player2 wins')

				game_on = False

				break


			else:

				for i in range(5):

					player1_cards.append(player1.remove_card())
					player2_cards.append(player2.remove_card())
                
            

					






























