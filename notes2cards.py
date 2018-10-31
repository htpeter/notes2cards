import re
import argparse
import random

import anki
import genanki

from utilities import models

def main(args):
    # Initialize new deck
    my_deck = genanki.Deck(
        deck_id=random.getrandbits(32),
        name=args.deckName)
    # my_deck.add_model()
    # Open file and read
    with open(args.inputFile, 'r') as f:
        read_input_file = f.read()
        # Parse file for notes using smart logic
        list_of_notes = note_parse(raw_text=read_input_file)
        # add em to our deck
        for item in list_of_notes:
        	note = item.to_note()
        	my_deck.add_note(note)
    # Write to output    	
    genanki.Package(my_deck).write_to_file(args.outputFile)


def note_parse(raw_text):
	"""
	WHERE THE MAGIC HAPPENS!
	Turns notes2cards formatted notes into genanki cards.
	Also stores them in a format for use later if we wanna
	get fancy.
	"""
	cards = []
	list_of_lines = raw_text.split('\n')
	for idx, val in enumerate(list_of_lines):
		if val[0] == '#':
			card = models.SimpleVocabCard(val, list_of_lines[idx + 1])
			cards.append(card)
	return cards

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Turn some notes into a Anki deck.')
    parser.add_argument('--inputFile', help='File for notes to be parsed to Anki deck.')
    parser.add_argument('--deckName', help='Name for Deck.')
    parser.add_argument('--outputFile', help='Output name for created Anki deck.')
    args = parser.parse_args()

    main(args)
