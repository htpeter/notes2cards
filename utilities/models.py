import genanki
import random

class SimpleVocabCard(object):
	"""
	For a simple header, text section format
	"""
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

	def to_note(self, model_type = 'standard_model'):
		note = genanki.Note( 
			model = types[model_type],
 			fields=[self.question, self.answer])
		return note

	def __repr__(self):
		return "|| Card - {0} || \n\t {1}".\
					format(self.question, self.answer)

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