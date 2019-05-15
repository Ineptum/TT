import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
from TTUI import Ui_MainWindow
import time
import datetime
import random


class TT(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Modes = ['ALPHABET MODE', 'SHORT WORDS', 'LONG WORDS', 'KANT', 'FJ']
        self.Mode = 1
        self.rand = False

        self.letters = {
            Qt.Key_Space: [self.SpaceBar, ' '],
            Qt.Key_Q: [self.Q, 'q'],
            Qt.Key_W: [self.W, 'w'],
            Qt.Key_E: [self.E, 'e'],
            Qt.Key_R: [self.R, 'r'],
            Qt.Key_T: [self.T, 't'],
            Qt.Key_Y: [self.Y, 'y'],
            Qt.Key_U: [self.U, 'u'],
            Qt.Key_I: [self.I, 'i'],
            Qt.Key_O: [self.O, 'o'],
            Qt.Key_P: [self.P, 'p'],
            Qt.Key_BracketLeft: [self.Bracket1, '['],
            Qt.Key_BraceLeft: [self.Bracket1, '{'],
            Qt.Key_BracketRight: [self.Bracket2, ']'],
            Qt.Key_BraceRight: [self.Bracket2, '}'],
            Qt.Key_Backslash: [self.Backslash, '\\'],
            Qt.Key_Bar: [self.Backslash, '|'],
            Qt.Key_A: [self.A, 'a'],
            Qt.Key_S: [self.S, 's'],
            Qt.Key_D: [self.D, 'D'],
            Qt.Key_F: [self.F, 'f'],
            Qt.Key_G: [self.G, 'g'],
            Qt.Key_H: [self.H, 'h'],
            Qt.Key_J: [self.J, 'j'],
            Qt.Key_K: [self.K, 'k'],
            Qt.Key_L: [self.L, 'l'],
            Qt.Key_Semicolon: [self.Semicolon, ';'],
            Qt.Key_Colon: [self.Semicolon, ':'],
            Qt.Key_Apostrophe: [self.Quote, "'"],
            Qt.Key_QuoteDbl: [self.Quote, '"'],
            Qt.Key_Z: [self.Z, 'z'],
            Qt.Key_X: [self.X, 'x'],
            Qt.Key_C: [self.C, 'c'],
            Qt.Key_V: [self.V, 'v'],
            Qt.Key_B: [self.B, 'b'],
            Qt.Key_N: [self.N, 'n'],
            Qt.Key_M: [self.M, 'm'],
            Qt.Key_Comma: [self.Comma, ','],
            Qt.Key_Less: [self.Comma, '<'],
            Qt.Key_Period: [self.Dot, '.'],
            Qt.Key_Greater: [self.Dot, '>'],
            Qt.Key_Slash: [self.Slash, '/'],
            Qt.Key_Question: [self.Slash, '?'],
            Qt.Key_1: [self.One, '1'],
            Qt.Key_Exclam: [self.One, '!'],
            Qt.Key_2: [self.Two, '2'],
            Qt.Key_At: [self.One, '@'],
            Qt.Key_3: [self.Three, '3'],
            Qt.Key_NumberSign: [self.One, '#'],
            Qt.Key_4: [self.Four, '4'],
            Qt.Key_Dollar: [self.One, '$'],
            Qt.Key_5: [self.Five, '5'],
            Qt.Key_Percent: [self.One, '%'],
            Qt.Key_6: [self.Six, '6'],
            Qt.Key_Acircumflex: [self.One, '^'],
            Qt.Key_7: [self.Seven, '7'],
            Qt.Key_Ampersand: [self.One, '&'],
            Qt.Key_8: [self.Eight, '8'],
            Qt.Key_Asterisk: [self.One, '*'],
            Qt.Key_9: [self.Nine, '9', ],
            Qt.Key_ParenLeft: [self.One, '(', ],
            Qt.Key_0: [self.Zero, '0', ],
            Qt.Key_ParenRight: [self.One, ')']
        }

        self.initUi()

    def initUi(self):
        # Setting text fields

        self.LeftPattern.show()
        self.RightPattern.show()
        self.turn_keys_off()
        self.Time.setText('Your result will be shown here')
        self.Time.setStyleSheet("color: rgb(44, 56, 97);")
        self.Errors.setText('')

        kant = ['Immanuel', 'Kant', '(1724-1804)', 'is',
                'the', 'central', 'figure', 'in',
                'modern', 'philosophy.', 'He',
                'synthesized', 'early', 'modern',
                'rationalism', 'and', 'empiricism,',
                'set', 'the', 'terms',
                'for', 'much', 'of', 'nineteenth',
                'and', 'twentieth', 'century',
                'philosophy,', 'and', 'continues',
                'to', 'exercise', 'a', 'significant',
                'influence', 'today', 'in',
                'metaphysics,', 'epistemology,',
                'ethics,', 'political',
                'philosophy,', 'aesthetics,',
                'and', 'other', 'fields.', 'The',
                'fundamental', 'idea',
                'of', 'Kant’s', 'critical', 'philosophy',
                'especially', 'in', 'his',
                'three', 'Critiques:', 'the', 'Critique',
                'of', 'Pure', 'Reason', '(1781,', '1787),',
                'the', 'Critique', 'of', 'Practical', 'Reason', '(1788),',
                'and', 'the', 'Critique', 'of', 'the', 'Power', 'of', 'Judgment',
                '(1790)', 'is', 'human', 'autonomy.', 'He', 'argues', 'that', 'the',
                'human', 'understanding', 'is',
                'the', 'source', 'of', 'the', 'general', 'laws', 'of', 'nature', 'that',
                'structure', 'all', 'our', 'experience;',
                'and', 'that', 'human', 'reason', 'gives', 'itself', 'the', 'moral',
                'law,', 'which', 'is', 'our', 'basis', 'for',
                'belief', 'in', 'God,', 'freedom,', 'and', 'immortality.', 'Therefore,',
                'scientific', 'knowledge,', 'morality,',
                'and', 'religious', 'belief', 'are', 'mutually', 'consistent', 'and',
                'secure', 'because', 'they', 'all', 'rest',
                'on', 'the', 'same', 'foundation', 'of', 'human', 'autonomy,', 'which',
                'is', 'also', 'the', 'final', 'end', 'of',
                'nature', 'according', 'to', 'the', 'teleological', 'worldview', 'of',
                'reflecting', 'judgment', 'that', 'Kant',
                'introduces', 'to', 'unify', 'the', 'theoretical',
                'and', 'practical', 'parts', 'of', 'his', 'philosophical', 'system.']

        fj = ['fffjjj', 'fjfjfj', 'fjfjj', 'jjfjf', 'jfjfjf', 'ffjjf', 'f', 'f', 'f', 'fj',
              'jj', 'jf', 'jjfj', 'jfjf', 'jfjfjfjfjfjfjfjfjjjjjfjfjf', 'jfjfjf', 'fjjf',
              'jfjj', 'fjjfjfj', 'jjfjfj', 'jfjf', 'fjjfjfjfjfjjjjjfjfjjffjffffjfjfjjfjf',
              'jfj', 'jfj', 'jfj', 'fjfjfj', 'fjjf', 'jfjfjf', 'jjf', 'jfj', 'jfjf', 'ff',
              'jj', 'fff', 'jjj', 'f', 'j', 'fj']

        shortWords = ['hay', 'heir', 'harp', 'half', 'hang', 'hex', 'high', 'echo', 'earn',
                      'elan', 'eddy', 'edit',
                      'obit', 'oboe', 'obey', 'owl', 'oak', 'okie', 'dokey', 'down', 'duty',
                      'dux', 'dixy', 'doxy', 'xmas', 'xtal',
                      'nix', 'next', 'note', 'name', 'nape', 'nail', 'snap', 'spar', 'step',
                      'slow', 'shot', 'sheet', 'qua', 'quay',
                      'quad', 'quod', 'quit', 'pack', 'pray', 'pure', 'pig', 'pixy', 'push',
                      'rush', 'rue', 'rock', 'rose', 'rich',
                      'ring', 'main', 'mad', 'male', 'melt', 'milk', 'make', 'zero', 'zest',
                      'zonk', 'zoom', 'zinc', 'zing', 'year',
                      'yelp', 'ywis', 'your', 'chip', 'char', 'cut', 'chut', 'coxy', 'cow',
                      'kale', 'ken', 'knap', 'keep', 'keck',
                      'kiwi', 'with', 'wind', 'wick', 'woke', 'wont', 'void', 'volt',
                      'vole', 'vote', 'vita', 'vox', 'vug', 'very',
                      'jog', 'joke', 'jack', 'jab', 'job', 'jamb', 'jeep', 'girl', 'glue',
                      'gold', 'grow', 'good', 'luck', 'lake',
                      'lid', 'lie', 'lex', 'live', 'love']

        longWords = ['allowable', 'absolute', 'black', 'bonus', 'bicycle', 'expressive',
                     'eating', 'fortune', 'finish', 'frequency', 'fuzzy', 'imperial',
                     'include', 'kilobyte', 'obtain', 'throw', 'tutor', 'cherry', 'casino',
                     'cinema', 'cajole', 'candle', 'rubric', 'rover', 'rigor', 'unbound',
                     'unique', 'vampire', 'velvet', 'vogue', 'yearly', 'zombie', 'zippy',
                     'quack', 'quick', 'quake', 'queen', 'query', 'quorum', 'quadruple',
                     'xenon', 'xerox', 'xistor', 'xiphoid', 'xylogen', 'xanthoxylone',
                     'nixie', 'nothing', 'network', 'neighbour', 'window', 'weight',
                     'world', 'winch', 'whose', 'white', 'south', 'sounding', 'submarine',
                     'jumbo', 'justify', 'journey', 'government', 'paradox', 'penalty',
                     'paving', 'pepsi', 'guano', 'apes', 'memento', 'mori']

        alphabet = ['fall', 'jam', 'dash', 'kid', 'ska', 'lad', 'alf', 'bank',
                    'navy', 'man', 'gal', 'ham', 'talk', 'yak', 'rutty', 'urn',
                    'elf', 'is', 'wolf', 'oven', 'quasi', 'pet', 'xxl', 'cot',
                    'zone', 'abcdefghijklmnopqrstuvwxyz', 'fife', 'jojoba',
                    'doddle', 'kick', 'suss', 'label', 'aka', 'bob', 'nine',
                    'memo', 'guggle', 'hah', 'totality', 'yellowy', 'river', 'unused',
                    'eke', 'ivied', 'willow', 'oboe', 'quark', 'prep', 'xerox', 'clack',
                    'zigzag', 'zyxwvutsrqponmlkjihgfedcba']

        self.modes = [alphabet, fj, kant, shortWords, longWords]
        if self.rand:
            random.shuffle(self.modes[self.Mode])

        self.typer = ' ' + ' '.join(self.modes[self.Mode])  # Choosing mode
        self.typed = ''

        # The variable which counts correctly pressed keys to calculate the result
        self.let_counter = 0
        self.Speed = []
        self.is_stopped = False
        self.ST = 0  # Timer for counting time spent in pause
        self.STtimer = 0  # not to break the typing speed statistic

        self.errors = [0, str(eval('len(self.typer)'))]  # Error counter

        self.start = False  # A flag checking if the session has started
        self.finish = False  # A flag checking if the session has finished
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
        # Getting ready to show results in the end of key_press_event method
        self.let_counter += 1

        self.typed += self.typer[0]
        self.typer = self.typer[1:]

        speed_appender = self.Let_counter / ((time.time() - self.timer_start - self.ST) / 60)
        self.Speed.append(int(speed_appender))

        # This if statement checks whether the left box is filled with letters up to the end
        if len(self.typed) > 80:
            # Here the first letter in the box disappears so the text can fill into box
            self.typed = self.typed[1:]

        # Setting the fields to resemble changes
        self.TextTyped.setText(self.typed)
        self.TextField.setText(self.typer)

    def go(self):  # The session starts or is continued
        if self.is_stopped:
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
            self.is_stopped = False
        else:
            self.initUi()
            self.turn_keys_off()
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
        self.is_stopped = True
        # The countdown starts from the moment the session is stopped
        self.STtimer = time.time()

        # Everything written below makes STOPPED signs
        # show up and all the working signs disappear
        self.turn_keys_off()

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
        self.Switch.clicked.connect(lambda: self.switch_ui())

        # Restart the session if asked to
        self.Restart.clicked.connect(lambda: self.restart())

    def graph(self):
        self.widget.clear()
        self.widget.show()
        self.wList.show()
        self.widget.plot([i for i in range(len(self.Speed) - 1)],
                         [i for i in self.Speed[1:]], pen='w')

    def switch_ui(self):
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

        self.doSwitch.clicked.connect(lambda: self.switch(self.Mode,
                                                          self.rOrder.checkState(), 1))

    def switch(self, mode, random, restart):
        self.Mode = mode
        self.rand = random

        # Restarting the session if the GO button was pressed
        if restart == 1:
            self.restart()

    def key_press_event(self, event):

        if event.key() == Qt.Key_Space and not self.start and not self.finish:
            # This signalises either the start of the session or it's continuation
            self.go()
        try:
            # <STOP caller>
            if event.key() == Qt.Key_Escape:
                if not self.finish:
                    if not self.is_stopped:  # The session stops upon
                        self.stop()  # pressing Esc
                    elif self.is_stopped:
                        # If Esc is pressed twice the application is exited
                        QApplication.exit()
                else:
                    QApplication.exit()
            # </STOP caller>

            if self.start:

                if self.typed == '':  # If the session has started and the first butt
                    # on is being pressed
                    self.timer_start = time.time()  # start position for the timer
                    # is set

                self.turn_keys_off()  # All the keys turn off

                self.letters[event.key()][0].setStyleSheet("background-color:"
                                                           "rgb(255, 255, 255);")
                if self.letters[event.key()][1].upper() == self.typer[0].upper():
                    self.manageTyping()
                else:
                    self.letters[event.key()][0].setStyleSheet("background-colo"
                                                               "r: rgb(255, 108"
                                                               ", 54);")
                    self.errors[0] += 1

                if self.TextField.text() == '' and self.TextTyped.text() != '':
                    self.turn_keys_off()  # When there is nothing more to type all the
                    # keys turn off
                    self.finishing()
        except Exception as e:
            pass

    def finishing(self):
        if not self.finish:  # If the session is not finished
            # Outputing the results and making sure the session is finished now
            lCount = self.let_counter / ((time.time() - self.timer_start - self.ST) / 60)
            self.let_counter = int(lCount)
            if 300 < self.let_counter <= 425:
                self.Time.setStyleSheet("color: rgb(44, 56, 97)")
            elif self.let_counter >= 425:
                self.Time.setStyleSheet("color: rgb(1, 255, 1)")
            else:
                self.Time.setStyleSheet("color: rgb(255, 138, 84)")
            self.Time.setText(str(self.let_counter) + ' characters per minute')
            self.Time.show()

            # self.errors variable now resembles the percentage of errors made in int,
            # not list
            self.errors = int((self.errors[0]) / int(self.errors[1]) * 100)
            # Coloring the label depending on how much errors were made
            if 20 < self.errors >= 10:
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

            b = ''
            try:
                b = open('scoreboard.txt', 'r').read()
            except:
                pass
            a = open('scoreboard.txt', 'w')
            writer = ' '.join([self.Modes[self.Mode] + ',',
                               str(self.let_counter), 'cpm,', str(self.errors), '% errors',
                               str(datetime.datetime.today())[:-7]]) + '\n' + b
            a.write(writer)
            a.close()

            self.Switch.clicked.connect(lambda: self.switch_ui())
            self.Restart.clicked.connect(lambda: self.restart())

    def turn_keys_off(self):
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
        self.LeftPattern.setText('Space to start, ')
        self.RightPattern.setText('Esc to stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tt = TT()
    tt.show()
    sys.exit(app.exec_())
