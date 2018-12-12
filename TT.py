import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
from TTUI import Ui_MainWindow
import time
import random


class TT(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.Mode = 1
		self.rand = False

		self.initUi()

	def initUi(self):
		# Setting text fields

		self.LeftPattern.show()
		self.RightPattern.show()
		self.offKey()
		self.Time.setText('Your result will be shown here')
		self.Time.setStyleSheet("color: rgb(44, 56, 97);")
		self.Errors.setText('')

		kant = ['Immanuel', 'Kant', '(1724-1804)', 'is', 'the', 'central', 'figure', 'in', 'modern', 'philosophy.',
		        'He', 'synthesized', 'early', 'modern', 'rationalism', 'and','empiricism,', 'set', 'the', 'terms',
		        'for', 'much', 'of', 'nineteenth', 'and', 'twentieth', 'century', 'philosophy,', 'and', 'continues',
		        'to', 'exercise', 'a', 'significant', 'influence', 'today', 'in', 'metaphysics,', 'epistemology,',
		        'ethics,', 'political', 'philosophy,', 'aesthetics,', 'and', 'other', 'fields.', 'The',
		        'fundamental', 'idea', 'of', 'Kant’s', 'critical', 'philosophy', 'especially', 'in', 'his',
		        'three', 'Critiques:', 'the', 'Critique', 'of', 'Pure', 'Reason', '(1781,', '1787),', 'the', 'Critique',
		        'of', 'Practical', 'Reason', '(1788),', 'and', 'the', 'Critique', 'of', 'the', 'Power', 'of', 'Judgment',
		        '(1790)', 'is', 'human', 'autonomy.', 'He', 'argues', 'that', 'the', 'human', 'understanding', 'is',
		        'the', 'source', 'of', 'the', 'general', 'laws', 'of', 'nature', 'that', 'structure', 'all', 'our', 'experience;',
		        'and', 'that', 'human', 'reason', 'gives', 'itself', 'the', 'moral', 'law,', 'which', 'is', 'our', 'basis', 'for',
		        'belief', 'in', 'God,', 'freedom,', 'and', 'immortality.', 'Therefore,', 'scientific', 'knowledge,', 'morality,',
		        'and', 'religious', 'belief', 'are', 'mutually', 'consistent', 'and', 'secure', 'because', 'they', 'all', 'rest',
		        'on', 'the', 'same', 'foundation', 'of', 'human', 'autonomy,', 'which', 'is', 'also', 'the', 'final', 'end', 'of',
		        'nature', 'according', 'to', 'the', 'teleological', 'worldview', 'of', 'reflecting', 'judgment', 'that', 'Kant',
		        'introduces', 'to', 'unify', 'the', 'theoretical', 'and', 'practical', 'parts', 'of', 'his', 'philosophical', 'system.']
 
		fj = ['fffjjj', 'fjfjfj', 'fjfjj', 'jjfjf', 'jfjfjf', 'ffjjf', 'f', 'f', 'f', 'fj', 'jj', 'jf',
		      'jjfj', 'jfjf', 'jfjfjfjfjfjfjfjfjjjjjfjfjf', 'jfjfjf', 'fjjf', 'jfjj', 'fjjfjfj', 'jjfjfj',
		      'jfjf', 'fjjfjfjfjfjjjjjfjfjjffjffffjfjfjjfjf', 'jfj', 'jfj', 'jfj', 'fjfjfj', 'fjjf', 'jfjfjf',
		      'jjf', 'jfj', 'jfjf', 'ff', 'jj', 'fff', 'jjj', 'f', 'j', 'fj']

		shortWords = ['hay', 'heir', 'harp', 'half', 'hang', 'hex', 'high', 'echo', 'earn', 'elan', 'eddy', 'edit',
		 			  'obit', 'oboe', 'obey', 'owl', 'oak', 'okie', 'dokey', 'down', 'duty', 'dux', 'dixy', 'doxy', 'xmas', 'xtal',
		  			  'nix', 'next', 'note', 'name', 'nape', 'nail', 'snap', 'spar', 'step', 'slow', 'shot', 'sheet', 'qua', 'quay',
		   			  'quad', 'quod', 'quit', 'pack', 'pray', 'pure', 'pig', 'pixy', 'push', 'rush', 'rue', 'rock', 'rose', 'rich',
		    		  'ring', 'main', 'mad', 'male', 'melt', 'milk', 'make', 'zero', 'zest', 'zonk', 'zoom', 'zinc', 'zing', 'year',
		    		  'yelp', 'ywis', 'your', 'chip', 'char', 'cut', 'chut', 'coxy', 'cow', 'kale', 'ken', 'knap', 'keep', 'keck',
		      		  'kiwi', 'with', 'wind', 'wick', 'woke', 'wont', 'void', 'volt', 'vole', 'vote', 'vita', 'vox', 'vug', 'very',
		       		  'jog', 'joke', 'jack', 'jab', 'job', 'jamb', 'jeep', 'girl', 'glue', 'gold', 'grow', 'good', 'luck', 'lake',
		        	  'lid', 'lie', 'lex', 'live', 'love']

		longWords = ['allowable', 'absolute', 'black', 'bonus', 'bicycle', 'expressive', 'eating', 'fortune', 'finish', 'frequency',
					 'fuzzy', 'imperial', 'include', 'kilobyte', 'obtain', 'throw', 'tutor', 'cherry', 'casino', 'cinema', 'cajole',
					 'candle', 'rubric', 'rover', 'rigor', 'unbound', 'unique', 'vampire', 'velvet', 'vogue', 'yearly', 'zombie', 'zippy',
					 'quack', 'quick', 'quake', 'queen', 'query', 'quorum', 'quadruple', 'xenon', 'xerox', 'xistor', 'xiphoid', 'xylogen',
					 'xanthoxylone', 'nixie', 'nothing', 'network', 'neighbour', 'window', 'weight', 'world', 'winch', 'whose', 'white',
					 'south', 'sounding', 'submarine', 'jumbo', 'justify', 'journey', 'government', 'paradox', 'penalty', 'paving', 'pepsi',
					 'guano', 'apes', 'memento', 'mori']
					 
		alphabet = ['fall', 'jam', 'dash', 'kid', 'ska', 'lad', 'alf', 'bank',
			 'navy', 'man', 'gal', 'ham', 'talk', 'yak', 'rutty', 'urn',
			 'elf', 'is', 'wolf', 'oven', 'quasi', 'pet', 'xxl', 'cot',
			 'zone', 'abcdefghijklmnopqrstuvwxyz', 'fife', 'jojoba',
			 'doddle', 'kick', 'suss', 'label', 'aka', 'bob', 'nine',
			 'memo', 'guggle', 'hah', 'totality', 'yellowy', 'river', 'unused',
			 'eke', 'ivied', 'willow', 'oboe', 'quark', 'prep', 'xerox','clack',
			 'zigzag', 'zyxwvutsrqponmlkjihgfedcba']

		self.modes = [alphabet, fj, kant, shortWords, longWords]
		if self.rand:
			random.shuffle(self.modes[self.Mode])

		self.typer = ' ' + ' '.join(self.modes[self.Mode]) # Choosing mode
		self.typed = ''

		# The variable which counts correctly pressed keys to calculate the result
		self.LetterCounter = 0
		self.Speed = []
		self.isStopped = False
		self.ST = 0 	 # Timer for counting time spent in pause
		self.STtimer = 0 # not to break the typing speed statistic

		self.errors = [0, str(eval('len(self.typer)'))] # Error counter

		self.start = False  # A flag checking if the session has started
		self.finish = False # A flag checking if the session has finished
		self.setWindowTitle('Learn Typing!')

		# Setting text boxes
		self.TextTyped.setText(self.typed)
		self.TextField.setText(self.typer)

		self.wList.hide()
		self.widget.hide()
		self.switcher.hide()
		self.aMode.hide()
		self.fjMode.hide()
		self.KMode.hide()
		self.sMode.hide()
		self.lMode.hide()
		self.doSwitch.hide()
		self.rOrder.hide()

		# Hiding the STOPPED pop-up
		self.stopped.hide()
		self.lstopped.hide()

		# Hiding restarter and mode switcher
		self.Restart.hide()
		self.Switch.hide()

	def manageTyping(self):
		# Getting ready to show results in the end of keyPressEvent method
		self.LetterCounter += 1

		self.typed += self.typer[0]
		self.typer = self.typer[1:]

		self.Speed.append(int(self.LetterCounter/ ((time.time() - self.timerStart - self.ST) / 60)))
		
		# This if statement checks whehter the left box is filled with letters up to the end
		if len(self.typed) > 50:
			# Here the first letter in the box disappears so the text can fill into the box
			self.typed = self.typed[1:]

		# Setting the fields to resemble changes
		self.TextTyped.setText(self.typed)
		self.TextField.setText(self.typer)

	def go(self): # The session starts or is continued
		if self.isStopped:
			# Setting text boxes
			self.TextTyped.setText(self.typed)
			self.TextField.setText(self.typer)

			# Hiding the STOPPED pop-up
			self.stopped.hide()
			self.lstopped.hide()

			# Hiding restarter and mode switcher
			self.Restart.hide()
			self.Switch.hide()
			self.widget.hide()
			self.wList.hide()

			# Timer counts how much time the session was being paused
			self.ST += time.time() - self.STtimer
			# The session now goes on
			self.isStopped = False
		else:
			self.initUi()
			self.offKey()
			# Hiding results
			self.Time.hide()
			self.Errors.hide()
		
		# Hiding short instructions
		self.LeftPattern.hide()
		self.RightPattern.hide()

		# Getting TextField ready to start the session
		self.TextField.show()

		# Making sure the session started
		self.start = True

	def restart(self):
		self.initUi()

	def stop(self):
		self.isStopped = True
		# The countdown starts from the moment the session is stopped
		self.STtimer = time.time()

		# Everything written below makes STOPPED signs 
		# show up and all the working signs disappear
		self.offKey()

		self.LeftPattern.setText('Space to continue, ')
		self.LeftPattern.show()
		self.RightPattern.setText('Esc to exit')
		self.RightPattern.show()

		self.Switch.show()
		self.Restart.show()

		self.stopped.show()
		self.lstopped.show()

		# Now the session isn't continuing
		if self.start:
			self.start = False

		# Building a graph to show how average typing
		# speed was changing during the session
		self.graph()

		# Switch the mode if asked to
		self.Switch.clicked.connect(lambda: self.switchUi())

		# Restart the session if asked to
		self.Restart.clicked.connect(lambda: self.restart())

	def graph(self):
		self.widget.clear()
		self.widget.show()
		self.wList.show()
		self.widget.plot([i for i in range(len(self.Speed) - 1)],
						 [i for i in self.Speed[1:]], pen='w')

	def switchUi(self):
		mode = self.Mode
		# Showing all hidden widgets
		self.switcher.show()
		self.aMode.show()
		self.fjMode.show()
		self.KMode.show()
		self.sMode.show()
		self.lMode.show()
		self.doSwitch.show()
		self.rOrder.show()

		# Connecting to switch function
		self.aMode.clicked.connect(lambda: self.switch(0, self.rOrder.checkState(), 0))
		self.fjMode.clicked.connect(lambda: self.switch(1, self.rOrder.checkState(), 0))
		self.KMode.clicked.connect(lambda: self.switch(2, self.rOrder.checkState(), 0))
		self.sMode.clicked.connect(lambda: self.switch(3, self.rOrder.checkState(), 0))
		self.lMode.clicked.connect(lambda: self.switch(4, self.rOrder.checkState(), 0))

		self.doSwitch.clicked.connect(lambda: self.switch(self.Mode, self.rOrder.checkState(), 1))

	def switch(self, mode, random, restart):
		self.Mode = mode
		self.rand = random

		# Restarting the session if the GO button was pressed
		if restart == 1:
			self.restart()

	def keyPressEvent(self, event):

		if event.key() == Qt.Key_Space and not self.start and not self.finish:
			self.go() # This signalises either the start of the session or it's continuation

		try:
			################################ <STOP caller>
			if event.key() == Qt.Key_Escape:
				if not self.finish:
					if not self.isStopped: # The session stops upon 
						self.stop()        # pressing Esc
					elif self.isStopped:
						# If Esc is pressed twice in a row the application is exited
						QApplication.exit()
				else:
					QApplication.exit()
			############################### </STOP caller>

			if self.start:

				if self.typed == '':              # If the session has started and the first button is being pressed
					self.timerStart = time.time() # start position for the timer is set

				self.offKey()					  # All the keys turn off

				if event.key() == Qt.Key_Q:                                       # If Q key is pressed
					self.Q.setStyleSheet("background-color: rgb(255, 255, 255);") # Q key switches on
					if 'Q' == self.typer[0].upper():                              # If Q is the right key to press it
						self.manageTyping()                                       # manages text on the screen with manageTyping method
					else:
						self.errors[0] += 1                                          # If Q isn't the right key to press it is remembered
						self.Q.setStyleSheet("background-color: rgb(255, 108, 54);") # there was a mistake and Q is now painted red

				# Same for every key down there:

				elif event.key() == Qt.Key_Space:
					self.SpaceBar.setStyleSheet("background-color: rgb(255, 255, 255);")
					if ' ' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.SpaceBar.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_W:
					self.W.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'W' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.W.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_E:
					self.E.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'E' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.E.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_R:
					self.R.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'R' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.R.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_T:
					self.T.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'T' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.T.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Y:
					self.Y.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'Y' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Y.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_U:
					self.U.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'U' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.U.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_I:
					self.I.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'I' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.I.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_O:
					self.O.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'O' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.O.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_P:
					self.P.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'P' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.P.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_A:
					self.A.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'A' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.A.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_S:
					self.S.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'S' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.S.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_D:
					self.D.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'D' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.D.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_F:
					self.F.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'F' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.F.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_G:
					self.G.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'G' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.G.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_H:
					self.H.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'H' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.H.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_J:
					self.J.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'J' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.J.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_K:
					self.K.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'K' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.K.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_L:
					self.L.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'L' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.L.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Z:
					self.Z.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'Z' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Z.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_X:
					self.X.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'X' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.X.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_C:
					self.C.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'C' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.C.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_V:
					self.V.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'V' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.V.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_B:
					self.B.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'B' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.B.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_N:
					self.N.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'N' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.N.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_M:
					self.M.setStyleSheet("background-color: rgb(255, 255, 255);")
					if 'M' == self.typer[0].upper():
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.M.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_1:
					self.One.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '1' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.One.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Exclam:
					self.One.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '!' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Two.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_2:
					self.Two.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '2' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Two.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_At:
					self.Two.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '@' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Two.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_3:
					self.Three.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '3' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Three.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_NumberSign:
					if '#' == self.typer[0]:
						self.Three.setStyleSheet("background-color: rgb(255, 255, 255);")
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Three.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_4:
					self.Four.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '4' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Four.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Dollar:
					self.Zero.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '$' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Zero.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_5:
					self.Five.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '5' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Five.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Percent:
					self.Five.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '%' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Five.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_6:
					self.Six.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '6' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Six.setStyleSheet("background-color: rgb(255, 108, 54);")
						
				elif event.key() == Qt.Key_Up:
					self.Six.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '^' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Six.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_7:
					self.Seven.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '7' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Seven.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Ampersand:
					self.Seven.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '&' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Seven.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_8:
					self.Eight.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '8' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Eight.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Asterisk:
					self.Eight.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '*' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Eight.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_9:
					self.Nine.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '9' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Nine.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_ParenLeft:
					self.Nine.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '(' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Nine.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_0:
					self.Zero.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '0' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Zero.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_ParenRight:
					self.Zero.setStyleSheet("background-color: rgb(255, 255, 255);")
					if ')' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Zero.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Minus:
					self.Minus.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '-' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Minus.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Underscore:
					self.Minus.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '_' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Minus.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Equal:
					self.Equality.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '=' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Equality.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Plus:
					self.Equality.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '+' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Equality.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_BracketLeft:
					self.Bracket1.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '[' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Bracket1.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_BraceLeft:
					self.Bracket1.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '{' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Bracket1.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_BracketRight:
					self.Bracket2.setStyleSheet("background-color: rgb(255, 255, 255);")
					if ']' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Bracket2.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_BraceRight:
					self.Bracket2.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '}' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Bracket2.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Semicolon:
					self.Semicolon.setStyleSheet("background-color: rgb(255, 255, 255);")
					if ';' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Semicolon.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Colon:
					self.Semicolon.setStyleSheet("background-color: rgb(255, 255, 255);")
					if ':' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Semicolon.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Apostrophe:
					self.Quote.setStyleSheet("background-color: rgb(255, 255, 255);")
					if "'" == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Quote.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_QuoteDbl:
					self.Quote.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '"' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Quote.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Comma:
					self.Comma.setStyleSheet("background-color: rgb(255, 255, 255);")
					if ',' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Comma.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Left:
					self.Comma.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '<' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Comma.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Period:
					self.Dot.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '.' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Dot.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Slash:
					self.Slash.setStyleSheet("background-color: rgb(255, 255, 255)")
					if '/' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Slash.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Question:
					self.Slash.setStyleSheet("background-color: rgb(255, 255, 255)")
					if '?' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Slash.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Right:
					self.Dot.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '>' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Dot.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Backslash:
					self.Backslash.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '\\'== self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Backslash.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_Bar:
					self.Backslash.setStyleSheet("background-color: rgb(255, 255, 255)")
					if '|'== self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Backslash.setStyleSheet("background-color: rgb(255, 108, 54);")

				elif event.key() == Qt.Key_AsciiTilde:
					self.Grave.setStyleSheet("background-color: rgb(255, 255, 255);")
					if '~' == self.typer[0] or '`' == self.typer[0]:
						self.manageTyping()
					else:
						self.errors[0] += 1
						self.Grave.setStyleSheet("background-color: rgb(255, 108, 54);")

				if self.TextField.text() == '' and self.TextTyped.text() != '':
					self.offKey() # When there is nothing more to type all the keys turn off

					if not self.finish: # If the session is not finished
						# Outputing the results and making sure the session is finished now
						self.LetterCounter = int(self.LetterCounter / ((time.time() - self.timerStart - self.ST) / 60))
						if self.LetterCounter <= 425 and self.LetterCounter > 300:
							self.Time.setStyleSheet("color: rgb(44, 56, 97)")
						elif self.LetterCounter >= 425:
							self.Time.setStyleSheet("color: rgb(1, 255, 1)")
						else:
							self.Time.setStyleSheet("color: rgb(255, 138, 84)")
						self.Time.setText(str(self.LetterCounter) + ' characters per minute')
						self.Time.show()
						

						# self.errors variable now resembles the percentage of errors made in int, not list
						self.errors = int((self.errors[0]) / int(self.errors[1]) * 100)
						# Coloring the label depending on how much errors were made
						if self.errors >= 10 and self.errors < 20:
							self.Errors.setStyleSheet("color: rgb(44, 56, 97)")
						elif self.errors < 10:
							self.Errors.setStyleSheet("color: rgb(1, 255, 1)")
						else:
							self.Errors.setStyleSheet("color: rgb(255, 138, 84)")
						self.Errors.setText(str(self.errors) + '% errors')
						self.Errors.show()

						self.finish = True
						self.Restart.show()
						self.Switch.show()
						self.graph()

						self.Switch.clicked.connect(lambda: self.switchUi())
						self.Restart.clicked.connect(lambda: self.restart())

		except Exception:
			pass

	def offKey(self):
		# All the code below switches off the keys and sets their StyleSheets to default
		self.SpaceBar.setStyleSheet("background-color: rgb(201, 225, 255);")
		self.TextField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(94, 110, 184);")
		self.TextTyped.setStyleSheet("background-color: rgb(201, 225, 255);\n"
"color: rgb(149, 160, 255);")
		self.Two.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);\n")
		self.One.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Grave.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.Backspace.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.Tab.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.Backslash.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.CAPS.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.Enter.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.LShift.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.RShift.setStyleSheet("background-color: rgb(201, 225, 255);\n"
	"color: rgb(155, 164, 172);")
		self.Three.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.Four.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.Five.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.Six.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.Seven.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.Eight.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.Nine.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.Zero.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Minus.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Equality.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Bracket2.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Bracket1.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.P.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.O.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.I.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.U.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.Y.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.T.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.R.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.E.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.W.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.Q.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.A.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.D.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.S.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.G.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.F.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.H.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.J.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.K.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.L.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.Semicolon.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Quote.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.Z.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.V.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.X.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.C.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.B.setStyleSheet("background-color: rgb(255, 202, 78);\n"
	"color: rgb(209, 145, 41);")
		self.N.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.M.setStyleSheet("background-color: rgb(244, 244, 47);\n"
	"color: rgb(230, 195, 51);")
		self.Comma.setStyleSheet("background-color: rgb(203, 255, 58);\n"
	"color: rgb(141, 176, 64);")
		self.Dot.setStyleSheet("background-color: rgb(46, 245, 255);\n"
	"color: rgb(37, 171, 208);")
		self.Slash.setStyleSheet("background-color: rgb(33, 217, 147);\n"
	"color: rgb(61, 175, 103);")
		self.vertical.setStyleSheet("color: rgb(155, 164, 172);")
		self.question.setStyleSheet("color: rgb(61, 175, 103);")
		self.colon.setStyleSheet("color: rgb(61, 175, 103);")
		self.doublequote.setStyleSheet("color: rgb(61, 175, 103);")
		self.brace2.setStyleSheet("color: rgb(61, 175, 103);")
		self.brace1.setStyleSheet("color: rgb(37, 171, 208);")
		self.cage.setStyleSheet("color: rgb(37, 171, 208);")
		self.dollar.setStyleSheet("color: rgb(141, 176, 64);")
		self.cat.setStyleSheet("color: rgb(61, 175, 103);")
		self.exclamation.setStyleSheet("color: rgb(61, 175, 103);")
		self.curly1.setStyleSheet("color: rgb(61, 175, 103);")
		self.curly2.setStyleSheet("color: rgb(61, 175, 103);")
		self.star.setStyleSheet("color: rgb(141, 176, 64);")
		self.And.setStyleSheet("color: rgb(230, 195, 51);")
		self.upward.setStyleSheet("color: rgb(209, 145, 41);")
		self.percent.setStyleSheet("color: rgb(209, 145, 41);")
		self.underline.setStyleSheet("color: rgb(61, 175, 103);")
		self.plus.setStyleSheet("color: rgb(61, 175, 103);")
		self.right.setStyleSheet("color: rgb(37, 171, 208);")
		self.left.setStyleSheet("color: rgb(141, 176, 64);")
		self.LeftPattern.setText('Space to start, ')
		self.RightPattern.setText('Esc to stop')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	tt = TT()
	tt.show()
	sys.exit(app.exec_())
