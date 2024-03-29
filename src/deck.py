import os
import random
import pickle


current_file_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file_path)
__SAVE_PATH__ = os.path.join(current_directory,'save')

CLEAR = 'cls' if os.name == 'nt' else 'clear'

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
    
    def size(self):
        """Return the size of the deck."""
        return len(self.deck) 
  
      
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
        
    def quiz(self):
        while not self.empty():
            self.shuffle()
            card = self.draw()
            os.system(CLEAR)
            result = card.ask_question()
            self.report(card, result)
        os.system(CLEAR)
        
        print("Quiz complete.")
        print(f"Score: {self.score() * 100:.2f}%")
        for card, result in self.print_report().items():
            print(f"{card.view_question()}: {'Correct' if result else 'Incorrect'}") 
