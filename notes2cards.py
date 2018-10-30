#!/anaconda3/envs/dl36/bin/python3.6

import re
import argparse
import random

import anki
import genanki

def main(args):
	# Initialize new deck
	my_deck = genanki.Deck(
  			deck_id = random.getrandbits(32),
  			name = args.deckName)
	# Open file and read
	with open(args.inputFile, 'r') as f:
		read_input_file = f.read()
		# Parse file for notes using smart logic
		list_of_dicts = note_parse(raw_text = read_input_file)
		# Z
		print(list_of_dicts)

def note_parse(raw_text):
	"""
	Turns notes2cards formatted notes into genanki cards.
	"""
	list_of_dicts = raw_text
	return list_of_sections

def notify(dictionary, model_type):
	"""
	Turn a dictionary to a note based on a style
	"""
	# types of models for note
	types = {
		# Simple card with Question and Answer
		'standard_model' : genanki.Model(
				model_id = random.getrandbits(32),
				name = 'standard_model',
				fields=[
				    {'name': 'Question'},
				    {'name': 'Answer'},
				  ],
				templates=[
				    {
				      'name': 'Card 1',
				      'qfmt': '{{Question}}',
				      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
				    },
				  ]),
		# Placeholder for more robust methods.
		'fancy_model' : genanki.Model(
				model_id = random.getrandbits(32),
				name = 'fancy_model',
			  fields=[
				    {'name': 'Question'},
				    {'name': 'Answer'},
				  ],
			  templates=[
				    {
				      'name': 'Card 1',
				      'qfmt': '{{Question}}',
				      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
				    },
				  ]),
			}
	# Generate note
	note = genanki.Note( 
		model = types[model_type],
 		fields=['Capital of Argentina', 'Buenos Aires'])
	return note


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Turn some notes into a Anki deck.')
	parser.add_argument('--inputFile', help='File for notes to be parsed to Anki deck.')
	parser.add_argument('--deckName', help='Name for Deck.')
	args = parser.parse_args()

	main(args)