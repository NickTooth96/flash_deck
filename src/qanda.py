TYPES = {0: None, 1: "Multiple Choice", 2: "True or False", 3: "Short Answer"}

class QASet:

    type = 0
    question = ""
    options = []
    answer = ""

    def __init__(self, type: int, question, options, answer):
        self.type = type
        self.answer = answer
        self.options = options
        self.answer = answer

