#!/anaconda3/envs/dl36/bin/python3.6

import re
import argparse
import random

import anki
import genanki

from utilities import funcs
from utilities import models


def main(args):
    # Initialize new deck
    my_deck = genanki.Deck(
        deck_id=random.getrandbits(32),
        name=args.deckName)
    # Open file and read
    with open(args.inputFile, 'r') as f:
        read_input_file = f.read()
        # Parse file for notes using smart logic
        list_of_dicts = note_parse(raw_text=read_input_file)
        # Z
        print(list_of_dicts)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Turn some notes into a Anki deck.')
    parser.add_argument('--inputFile', help='File for notes to be parsed to Anki deck.')
    parser.add_argument('--deckName', help='Name for Deck.')
    args = parser.parse_args()

    main(args)
