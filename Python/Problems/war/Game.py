import Deck
import Player
import time

class Game():
    def __init__(self, player_A:Player, player_B:Player):
        self.player_A = player_A
        self.player_B = player_B
        
        self.deck = Deck.Deck()
        self.deck.shuffle_deck()
        self.deck = self.deck.get_deck()
        
    def deal_cards(self):
        print(len(self.deck))
        while len(self.deck) != 0:
            self.player_A.hand.append(self.deck.pop())
            self.player_B.hand.append(self.deck.pop())
            
    def print_hands(self):
        # for card in self.player_A.hand:
        #     print(f"Player {self.player_A.name} has {card.value}, {card.suit}")
        # for card in self.player_B.hand:
        #     print(f"Player {self.player_B.name} has {card.value}, {card.suit}")
        print(f"Player A has {len(self.player_A.hand)} cards")
        print(f"Player B has {len(self.player_B.hand)} cards")
    
    def add_to_hands(self):
        pass
    
    def compare_cards(self, card_a, card_b):
        if card_a.value < card_b.value:
            return "a"
        
        if card_a.value == card_b.value:
            # check suit
            print("oh no the numbers are the same..........................................")
            if card_a.suit[1] < card_b.suit[1]: # [suitname, value]
                return "a"
            else:
                return "b"
             
        return "b"
    
    def add_to_hand(self, player, card_a, card_b):
        player.hand.append(card_a)
        player.hand.append(card_b)
    
    def check_empty_hands(self, player_A, player_B):
        if len(player_A.hand) == 0:
            return True
        elif len(player_B.hand) == 0:
            return True
        else:
            return False


player_A = Player.Player("Bob")
player_B = Player.Player("Joe")
game = Game(player_A, player_B)
game.deal_cards()
game.print_hands()

# start the game of war!
# i = 10
while True:
    
    card_a = player_A.draw_card()
    card_b = player_B.draw_card()
    
    result = game.compare_cards(card_a, card_b)
    if result == "a":
        # player A wins the hand
        print(f"{player_A.name} wins this hand of {card_a.value}/{card_a.suit} and {card_b.value}/{card_b.suit}")
        game.add_to_hand(player_A, card_a, card_b)
    else:
        # player B wins the hand\
        print(f"{player_B.name} wins this hand of {card_a.value}/{card_a.suit} and {card_b.value}/{card_b.suit}")
        game.add_to_hand(player_B, card_a, card_b)
        
    # check if hands are empty
    game.print_hands()
    is_empty = game.check_empty_hands(player_A, player_B)
    # print(f"Empty hands: {is_empty}")
    if is_empty:
        print("Someone's out of cards!")
        # declare a winner
        if len(player_A.hand) > len(player_B.hand):
            print(f"{player_A.name} wins!")
        else:
            print(f"{player_B.name} B wins!")
        break
    else:
        # continue game
        # time.sleep(0.5) # add some suspense
        pass