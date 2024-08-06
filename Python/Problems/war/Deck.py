import Card
import random

class Deck():
    
    suits = {
    "spades": 1,
    "clubs": 2,
    "diamonds": 3,
    "hearts": 4
}
    
    def __init__(self):
        self.deck = []
        
        for num in range(1,14):
            for suit in Deck.suits.items():
            # for suit in [1, 2, 3, 4]:
                # 
                self.deck.append(Card.Card(int(num), suit))
    def display_cards(self):
        for i in range(0,52):
            print(f"{self.deck[i].value} and {self.deck[i].suit}")
            
    def shuffle_deck(self):
        random.shuffle(self.deck) # shuffles in place which is fine
    
    def get_deck(self):
        return self.deck
            
# deck = Deck()
# deck.display_cards()
# deck.shuffle_deck()
# deck.display_cards()