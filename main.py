import src.deck as deck
import src.parse as parse
import argparse
import os

__PATH__ = 'data/test.txt'
__SAVE_PATH__ = 'save/'

CLEAR = 'cls' if os.name == 'nt' else 'clear'

SOURCE_HELP = "The source file to parse. Default is 'data/test.txt'."


parser = argparse.ArgumentParser(
                    prog='Flash Deck',
                    description='A simple flash card program.',
                    epilog='By Nicholas Toothaker')

parser.add_argument('-p','--parse', action='store_true')
parser.add_argument('-q','--quiz', action='store_true')
parser.add_argument('-n','--new', action='store_true')

subparsers = parser.add_subparsers(dest='new', help='Specify new with file or manual')
# Subparser for 'file' option
file_parser = subparsers.add_parser('file', help='Create a new file')
file_parser.add_argument('name', help='Name of the file')

# Subparser for 'manual' option
manual_parser = subparsers.add_parser('manual', help='Create a new manual entry')
manual_parser.add_argument('name', help='Name of the entry')

parser.add_argument('--src',dest='source',default=__PATH__, help=SOURCE_HELP)
args = parser.parse_args()

## CLI Main

if args.quiz:
    deck_list = os.listdir(__SAVE_PATH__)
    for i, deck_file in enumerate(deck_list):
        print(f"{i+1}. {deck_file}: {parse.load_deck(deck_file).size()} cards.")
    user_input = int(input("Enter the number of the deck you would like to load: "))
    deck = parse.load_deck(deck_list[user_input-1])

    while not deck.empty():
        deck.shuffle()
        card = deck.draw()
        os.system(CLEAR)
        result = card.ask_question()
        deck.report(card, result)
    os.system(CLEAR)
    
    print("Quiz complete.")
    print(f"Score: {deck.score() * 100:.2f}%")
    for card, result in deck.print_report().items():
        print(f"{card.view_question()}: {'Correct' if result else 'Incorrect'}")    
    
elif args.new:
    if args.new == 'file':
        cards = parse.parse_from_txt(args.source)
        deck = deck.Deck(args.name, cards)
    elif args.new == 'manual':
        cards = parse.manual_entry()
        deck = deck.Deck(args.name, cards)
    else:
        print("Operation Failed.")
else:
    print("No Command given.")
      