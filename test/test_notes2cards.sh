#!/bin/bash

# executed by travis from ../
python3.6 notes2cards.py --inputFile test_file.md \
						--deckName Test_Deck --outputFile test_deck.apkg
