import random
class Player():
    
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        print(f"Player {name} has joined")
        
    def draw_card(self):
        # randomly select a card from hand and return
        card_num = random.randint(0,len(self.hand)-1)
        return self.hand.pop(card_num)