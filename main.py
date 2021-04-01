import musicalbeeps
import time
import random
import PySimpleGUI as sg

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def gen_note():
    random.seed()
    note = random.choice(notes)
    octave = str(random.randint(3, 6))
    accidental = random.randint(0, 2)
    random.seed()
    if accidental == 0:
        accidental = "#"
    elif accidental == 1:
        accidental = "b"
    else:
        accidental = ""

    return note + octave + accidental


# Define the window's contents
layout = [[sg.Text('Note duration (milliseconds):')],
          [sg.Slider(range=(69, 2000),
                     default_value=1000,
                     size=(20, 15),
                     orientation='horizontal',
                     font=('Helvetica', 12))],
          [sg.Button('Play'), sg.Button('Stop')]
          ]

# Create the window
window = sg.Window('Note Generator', layout)
playing = False
delay = 1000
timer = 0
player = musicalbeeps.Player(volume=1.0, mute_output=False)
while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Play':
        playing = True
    if event == 'Stop':
        playing = False
    if playing and time.time_ns() // 1_000_000 - timer >= delay:
        timer = time.time_ns() // 1_000_000
        player.play_note(gen_note(), delay / 1000)
    delay = values[0]

window.close()
