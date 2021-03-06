from __future__ import print_function
from flask import Flask, render_template, request
import requests
import random
import os

app = Flask(__name__)
app.config["DEBUG"] = True

dict = {}

@app.route("/", methods=["GET", "POST"])
def site():
	if request.method == "POST":
		return render_template("index.html")
	else: # request.method == "GET"
		return render_template("index.html")

@app.route('/swagger')
def swagger():
	global dict
	dict = {}
	p1 = request.args.get('p1')
	p2 = request.args.get('p2')
	loadSelectors(p1, p2)
	text = getNumLines(2) + getNumLines(3)
	print(text)
	return text


def readInFile(filename, charset='utf-8'):
	with open("lyrics/" + filename, 'r') as f:
		words = f.read().decode(charset).rsplit()
		for i in range(len(words)-1):
			pair = words[i]+' '+words[i+1]
			if i < len(words)-2:
				value = words[i+2]
				if pair not in dict:
					dict[pair] = [value]
				else:
					dict[pair].append(value)

def getNumLines(numLines):
	lineCount = 0
	while lineCount < numLines:
		current_pair = random.choice(dict.keys())
		result = current_pair.capitalize()
		count = 0
		while current_pair in dict and lineCount < numLines:
			next_word = random.choice(dict[current_pair])
			result = result+ ' '+ next_word
			comp = current_pair.split()
			current_pair = comp[1]+ ' '+ next_word
			count += 1
			if count >= 6:
				lineCount += 1
				count = 0
				result = result + "\n"
		lineCount += 1
	return result

def loadSeuss():
	readInFile('fox-in-socks.txt')
	readInFile('cat-in-the-hat.txt')
	readInFile('green-eggs-and-ham.txt')
	readInFile('one-fish-two-fish.txt')
	readInFile('mullberry-street.txt')
	readInFile('if-i-ran-a-zoo.txt')

def loadGambino():
	readInFile('freaks-and-geeks.txt')
	readInFile('bonfire.txt')

def loadHemingway():
	readInFile('captives.txt')
	readInFile('advice-to-son.txt')
	readInFile('i-like-canadians.txt')
	readInFile('youth.txt')

def loadJayZ():
	readInFile('empire-state-of-mind.txt')
	readInFile('holy-grail.txt')

def load2Chainz():
	readInFile('we-own-it.txt')
	readInFile('birthday-song.txt')
	readInFile('im-different.txt')
	readInFile('bandz-dance.txt')

def loadBey():
	readInFile('single-ladies.txt')
	readInFile('seven-eleven.txt')
	readInFile('drunk-in-love.txt')
	readInFile('flawless.txt')

def loadPoe():
	readInFile('a-dream.txt')
	readInFile('alone.txt')
	readInFile('evening-star.txt')
	readInFile('a-valentine.txt')

def loadShakespeare():
	readInFile('the-world-stage.txt')
	readInFile('lover-complaint.txt')
	readInFile('winter-wind.txt')

def loadSelectors(p1, p2):
	if (p1 == "seuss") or (p2 == "seuss"):
		loadSeuss()
	if (p1 == "jay-z") or (p2 == "jay-z"):
		loadJayZ()
	if (p1 == "ernest") or (p2 == "ernest"):
		loadHemingway()
	if (p1 == "gambino") or (p2 == "gambino"):
		loadGambino()
	if (p1 == "beyonce") or (p2 == "beyonce"):
		loadBey()
	if (p1 == "2chainz") or (p2 == "2chainz"):
		load2Chainz()
	if (p1 == "poe") or (p2 == "poe"):
		loadPoe()
	if (p1 == "shakespeare") or (p2 == "shakespeare"):
		loadShakespeare()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run()
    # p1_dict = {}
    # p2_dict = {}
