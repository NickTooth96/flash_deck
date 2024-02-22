import os
import sys

import argparse
import random

import src.qaset as qa
import src.deck as deck
import pickle

__SAVE_PATH__ = 'save/'
TYPES = {"Multiple Choice": 1, "True/False": 2, "Short Answer": 3}

def parse_from_txt(file_path: str):
    """Parse a text file and return a list of QAsets."""
    lines = []
    cards = []
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) % 4 != 0:
            raise Exception("Invalid file format.")
        for i in range(0, len(lines), 4):
            type = TYPES[lines[i]]
            question = lines[i + 1]
            options = lines[i + 2].split(',')
            answer = lines[i + 3]
            cards.append(qa.QASet(type, question, options, answer))
        print(cards)
        return cards

def manual_entry():
    cards = []
    while True:
        os.system('clear')        
        question = input("Enter the question [Enter 'NO' to stop]: ")
        if question in ['NO', 'no', 'No']:
            break
        type = int(input("Enter the type of question [Multiple Choice: 1, True or False: 2, Short Answer: 3]: "))
        if type == 1:            
            options = input("Enter the options separated by a comma: ").split(',')
            for i in range(len(options)):
                print(f"{i+1}. {options[i]}")
            answer = options[int(input("Enter the number of the correct answer: "))-1]
        elif type == 2:
            options = ['False','True']
            answer = options[int(input("Enter 0 [False] or 1 [True]: "))]
        cards.append(qa.QASet(type, question, options, answer))
    print(cards)
    return cards

def load_deck(name):
    with open(os.path.join(__SAVE_PATH__,name), 'rb') as file:
        return pickle.load(file)