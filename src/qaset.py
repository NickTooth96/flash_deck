import random


TYPES = {0: None, 1: "Multiple Choice", 2: "True or False", 3: "Short Answer"}

class QASet:

    type = 0
    question = ""
    options = []
    answer = ""

    def __init__(self, type: int, question, options, answer):
        self.type = type
        self.question = question
        self.options = options
        self.answer = answer


## Accessor Functions

  
    def view_question(self):
        """Return the question."""
        return self.question

    def view_options(self):
        """Return the options."""
        return self.options
    
    def ask_question(self):
        print(self.question)
        self.shuffle_options()
        if self.type == 1 or self.type == 2:
            for i in range(len(self.options)):
                print(f"{i+1}. {self.options[i]}")
            user_answer = input("Enter the number of your answer: ")
            return self.options[int(user_answer) - 1] == self.answer       
        elif self.type == 3 or self.type == 0: 
            user_answer = input("Enter your answer: ")
            return user_answer == self.answer
        else:
            return False


## Manipulator Functions
 
  
    def shuffle_options(self):
        """Shuffle the options."""
        if self.type == 1 or self.type == 2:
            random.shuffle(self.options)