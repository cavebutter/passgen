import json
import string
import random
import PySimpleGUIQt as sg
import pyperclip

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation
characters = letters + numbers + punctuation

with open('words.json', 'r') as read_file:
    wordlist = json.load(read_file)


def pwd_word_recipe(num):
    pwd = ''
    for i in range(num-1):
        pwd += random.choice(list(wordlist))
        pwd += '-'
    pwd += random.choice(list(wordlist))
    return pwd


def pwd_random(num):
    pwd = ''
    for i in range(num):
        pwd += random.choice(characters)
    return pwd


sg.theme('DarkTeal12')

col1_layout = [[sg.Text("Number of words in your password (2-5)")],
        [sg.Slider(range=(2, 5), default_value=3, tick_interval=1, orientation='h',
                   key='-NUMWORDS-')]]

col2_layout = [sg.Text("Number of characters in your password (8-20)")], [sg.Slider(
    range=(8, 20), default_value=3, tick_interval=2, orientation='h',
                   key='-NUMCHARS-')]

layout = [
    [sg.Text("Select your password recipe: ")],
    [sg.Radio("Words", "Recipe", key='WORDS', default=True), sg.Radio(
        "Characters", "Recipe", key='CHARS')],
    [sg.Column(col1_layout)],

    [sg.Column(col2_layout)],
    [sg.Button('Submit'), sg.Text('      '), sg.Exit(), sg.Text('      '),  sg.Button('Copy Password')],
    [sg.Text("Your New Password Will Display Here", key='-OUTPUT-', font=('Courier',18),
             text_color='white')]
]

window = sg.Window("Jay's Password Generator", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Submit":
        if values['WORDS']:
            pwd = pwd_word_recipe(values['-NUMWORDS-'])
            window['-OUTPUT-'].update(pwd)
        elif values["CHARS"]:
            pwd = pwd_random(values['-NUMCHARS-'])
            window['-OUTPUT-'].update(pwd)
        else:
            sg.Popup("Rats")
    if event == "Copy Password":
        pyperclip.copy(pwd)
        sg.Popup("Password Copied To Clipboard!", title="Copied")
window.close()
