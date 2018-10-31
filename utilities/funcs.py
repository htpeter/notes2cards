
def note_parse(raw_text):
	"""
	WHERE THE MAGIC HAPPENS!
	Turns notes2cards formatted notes into genanki cards.
	Also stores them in a format for use later if we wanna
	get fancy.
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