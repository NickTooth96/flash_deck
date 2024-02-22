import os
import random
import pickle

__SAVE_PATH__ = 'save/'

class Deck():
    name = ""
    deck = []
    discard_pile = []
    report_card = {}
    def __init__(self, name, deck: list) -> None:
        self.deck = deck
        self.discard_pile = []
        self.report_card = {}
        self.name = name        
        self.save()
        
    def save(self):
        with open(os.path.join(__SAVE_PATH__,self.name), 'wb') as file:
            pickle.dump(self, file)


## Accessor Functions


    def score(self):
        """Return the score."""
        total_correct = 0
        for result in self.report_card.values():
            if result:
                total_correct += 1
        return total_correct / len(self.report_card)
        
    def draw(self):
        """Draw a card from the deck."""
        card = self.deck.pop()
        self.discard_pile.append(card)
        return card  
    
    def empty(self):
        """Return True if the deck is empty."""
        return len(self.deck) == 0  
    
    def print_report(self):
        """Return the report card."""
        return self.report_card    
  
      
## Manipulator Functions


    def add(self, card):
        """Add a card to the deck."""
        self.deck.append(card)

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)
        
    def report(self, card, result):
        """Add a card to the report card."""
        self.report_card[card] = result
