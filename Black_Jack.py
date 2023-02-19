# ask player if they would like to play the game or not
# deal both cards face up to player and only one face up to dealer
# the dealers second card will remain face down (unkown to the player/ not displayed)
# we will then promt the player with another question
# this question will ask the user if they would like to Hit or Stand
# if they pick hit we will deal them another card and add up there total cards if over 21 they lose, if 21 exact they win
# if anything below 21 we will promt the user with the same question
# if player hits 21 on the initial deal, they instantly win
# once the player decides they are going to stay
# the dealer will then reveal there second card if it is 17 or under they will have to hit again
# if the dealer hits 21 at anypoint they win and the player loses
# if the dealer goes over 21 and busts the player wins
# after every win or loss we will ask the player if they would like to play
# if yes repeate the above steps
# if not then we will quit the program

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.hand = []

    def hit(self, deck):
        card = deck.deal()
        self.hand.append(card)

    def stand(self):
        pass

    def get_hand_value(self):
        total = 0
        num_aces = 0
        for card in self.hand:
            if card.value == 1:
                num_aces += 1
                total += 11
            elif card.value >= 10:
                total += 10
            else:
                total += card.value
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1
        return total


class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.hide_second_card = True

    def show_first_card(self):
        self.hide_second_card = False
        return self.hand[1]

    def should_hit(self):
        return self.get_hand_value() < 17


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.deck.shuffle()
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        hidden_card = self.dealer.show_first_card()
        print("Player's hand:")
        for card in self.player.hand:
            print(card.value, "of", card.suit)
        print("Player's hand value:", self.player.get_hand_value())
        print("\nDealer's hand:")
        print(hidden_card.value, "of", hidden_card.suit)
        if self.dealer.hide_second_card:
            print("Second card is hidden")

    def play_round(self):
        if self.player.get_hand_value() == 21:
            return "player"
        while self.player.get_hand_value() < 21:
            if input("Hit or stand? ") == "hit":
                self.player.hit(self.deck)
            else:
                break
        if self.player.get_hand_value() > 21:
            return "dealer"
        while self.dealer.should_hit():
            self.dealer.hit(self.deck)
        if self.dealer.get_hand_value() > 21:
            return "player"
        if self.player.get_hand_value() > self.dealer.get_hand_value():
            return "player"
        elif self.player.get_hand_value() < self.dealer.get_hand_value():
            return "dealer"
        else:
            return "push"


while True:
    play = input("Would you like to play a game of Blackjack? (Y/N): ")
    if play.lower() == "y":
        game = Game()
        game.start()
        win = game.play_round()
        if win == "player":
            print("You win!")
        elif win == "dealer":
            print("Dealer wins!")
        else:
            print("It's a stand off!")
    else:
        break


