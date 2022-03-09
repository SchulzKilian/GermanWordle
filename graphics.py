#PYTHON

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.factory import Factory
import random
from kivy.uix.floatlayout import FloatLayout

with open(file="germandict.txt", encoding = "utf-8")as fl:
    wörter = fl.readlines()
    wortliste = [wort.strip() for wort in wörter]

möglich = ['seine', 'haben', 'durch', 'hatte', 'waren', 'sagte', 'jeder', 'sagen', 'klein', 'lesen', 'seits', 'Hafen', 'Lande', 'warum', 'Licht', 'Punkt', 'bauen', 'Vater', 'jeder', 'leben', 'wenig', 'Runde', 'jeder', 'geben', 'unter', 'durch', 'sagen', 'Hilfe', 'Linie', 'Umzug', 'Recht', 'Junge', 'viele', 'würde', 'diese', 'lange', 'Sache', 'sehen', 'gehen', 'nicht', 'meine', 'Anruf', 'erste', 'unten', 'Seite', 'jetzt', 'Seite', 'Sonne', 'Stadt', 'Macht', 'links', 'Nacht', 'Leben', 'essen', 'Fisch', 'Stopp', 'Basis', 'hören', 'Pferd', 'Farbe', 'Start', 'bekam', 'gehen', 'immer', 'Musik', 'beide', 'Marke', 'Meile', 'Fluss', 'genug', 'Ebene', 'Liste', 'Vogel', 'Frage', 'Stein', 'Feuer', 'Süden', 'Stück', 'sagte', 'obere', 'ganze', 'König', 'Kraft', 'Insel', 'statt', 'Spiel', 'Wärme', 'Osten', 'malen', 'unter', 'Macht', 'Stadt', 'Stern', 'Nomen', 'fähig', 'Pfund', 'getan', 'stand', 'Front', 'Woche', 'Ozean', 'warme', 'stark', 'Geist', 'beste', 'Boden', 'hören', 'sechs', 'Reise', 'Vokal', 'Krieg', 'legen', 'gegen', 'Liebe', 'Karte', 'regen', 'Regel', 'Kälte', 'Fahrt', 'Zelle', 'Platz', 'Grund', 'Dauer', 'Kunst', 'Thema', 'Kreis', 'Kluft', 'Silbe', 'Kugel', 'Welle', 'Motor', 'breit', 'Segel', 'Übung', 'Board', 'weich', 'Gases', 'Monat', 'blume', 'Reise', 'Reihe', 'genau', 'Ärger', 'Samen', 'Pause', 'wuchs', 'Draht', 'braun', 'Messe', 'sonst', 'Mitte', 'töten', 'milch', 'Orgel', 'Alter', 'Kleid', 'Wolke', 'ruhig', 'Stein', 'Menge', 'Boden', 'Eisen', 'Stick', 'Falte', 'lösen', 'Boden', 'Hügel', 'Katze', 'Küste', 'Kopie', 'still', 'Boden', 'Rolle', 'Kampf', 'Blick', 'nicht', 'Stuhl', 'reich', 'Bitte', 'Ernte', 'deren', 'Rings', 'sanft', 'Wasch', 'Menge', 'Strom', 'Angst', 'Blick', 'Suche', 'Druck', 'Wüste', 'Anzug', 'Strom', 'Stamm', 'Blatt', 'Aktie', 'Markt', 'küken', 'liebe', 'Feind', 'Natur', 'Dampf', 'Zweig', 'Spiel', 'Feige', 'Stahl', 'apfel', 'Masse', 'Karte', 'Abend', 'Basis', 'Block', 'Firma', 'Schuh', 'Lager', 'Quart', 'Ebene', 'Glanz', 'breit',"braun", "quizz","zwölf","zöpfe","kropf","stadt","ratte","Katze","macht"]
möglich = [worz.upper() for worz in möglich]
Window.size=500,900
class HomeScreen(Screen):
		# add a function to automatically go into first text field
    def start(self):
    	liste[0][0].focus = True

class Win(MDDialog):
    pass

class Lose(MDDialog):
    def get(self):
        return "".join(word)

class Row(Widget):
    pass

class GameScreen(Screen):
    def __init__(self,**kwargs):
        super(GameScreen,self).__init__(**kwargs)
        global word
        word = list(random.choice(möglich))
        print(word)
        super().__init__()
        pass
def getmerow(Char):
    for i,zeile in enumerate(liste):
        for j, item in enumerate(zeile):
            if Char == item:
                return i,j

def getlowest(Instance):
    for zeile in liste:
        for item in zeile:
            if not item.text or item == Instance:
                return item
def submitguess(string,row):
    if len(string)!= 5:
        return False
    if string not in wortliste:
        return False
    green = []
    orange= []
    oneg = list("".join(word))
    for i,letter in enumerate(string):
        if letter == oneg[i]:
            liste[row][i].background_color = .123,.165,.109,.1
            green.append(i)
            oneg[i]="*"
    if len(green)==len(oneg):
        Win().open()
    elif row == 5:
        Lose().open()
    for i,letter in enumerate(string):
        if letter in oneg and i not in green:
            orange.append(letter)
            liste[row][i].background_color = .8,.51,0,1
            oneg[oneg.index(letter)]="#"
            #now orange should work better
    return True


def getnextone(position):
    if position[1]!= 4:
        return liste[position[0]][position[1]+1]
    else:
        return liste[position[0]][1]
class Game(GridLayout):
    def __init__(self,**kwargs):
        super(Game, self).__init__(**kwargs)
        global liste
        liste = []
        self.rows=6
        self.spacing=3
        self.padding=15
        self.cols=5
        for i in range(6):
            kleineliste = []
            for j in range(5):
                kleineliste.append(CharInput())
                self.add_widget(kleineliste[j])
                if i + j != 0:
                    kleineliste[j].is_focusable = False
            liste.append(kleineliste)


class CharInput(TextInput):
    def keyboard_on_key_down(self, window,keycode, text, modifiers):
        if keycode[0] == 8 and not self.text and getmerow(self)[1]!=0:
            previous = self.get_focus_previous()
            if previous:
                self.focus = False
                previous.focus = True
        elif keycode[0]== 8:
            self.text = ""
    def on_text(self, _, text):
        previous = self.get_focus_previous()
        position = getmerow(self)
        self.text= self.text.upper()

        if position[1]==4:
            guess = ""
            for item in liste[position[0]]:
                guess += item.text
            if submitguess(guess,position[0]):
                for item in liste[position[0]]:
                    item.disabled = True
                    if not position == (5,4):
                        liste[position[0]+1][0].is_focusable = True
                        liste[position[0]+1][0].focus = True
        getnextone(position).is_focusable = True
        if not text:
            return
        if len(text) > 1:
            self.text = self.text[-1]
        next = self.get_focus_next()

        if next and position[1]!= 4:
            self.focus = False

            next.focus = True

class Changewindow(ScreenManager):
    pass


kv = """
Changewindow:
    HomeScreen:
    GameScreen:
    """
class graphicsApp(MDApp):
    def build(self):
        root = Factory.FloatLayout()
        root.add_widget(Builder.load_string(kv))
        return root
    def reset(self, ind):
        if liste[0][0].text:
            self.root.clear_widgets()
            self.root.add_widget(Builder.load_string(kv))
        ind.dismiss()





if __name__ == '__main__':
    graphicsApp().run()
