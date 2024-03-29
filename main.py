import src.deck as deck
import src.parse as parse
import argparse
import os

__PATH__ = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data','test.txt')
__SAVE_PATH__ = os.path.join(os.path.dirname(os.path.realpath(__file__)),'save')

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
        print(f"{i+1}. {deck_file.ljust(20)} {parse.load_deck(deck_file).size()} cards.")
    user_input = parse.evaluate_user_answer(input("Enter the number of the deck you would like to load: "))
    deck = parse.load_deck(deck_list[user_input-1])
    deck.quiz()
    # deck.repeat_wrong()
        
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
    
    print(__PATH__)
    print(__SAVE_PATH__)
 
    print("No Command given.")
      