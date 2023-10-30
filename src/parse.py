import src.qanda as qa


TYPES = {"Multiple Choice": 1, "True or False": 2, "Short Answer": 3}

def parse_from_txt(file_path: str):
    """Parse a text file and return a list of strings."""
    lines = []
    questions = []
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) % 4 != 0:
            raise Exception("Invalid file format.")
        for i in range(0, len(lines), 4):
            type = TYPES[lines[i]]
            question = lines[i + 1]
            options = lines[i + 2].split(',')
            answer = lines[i + 3]
            questions.append(qa.QASet(type, question, options, answer))
        return questions
