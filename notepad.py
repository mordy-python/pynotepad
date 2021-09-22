import PySimpleGUI as psg

app_layout = [
    [psg.Menu(['File', 'Help'])]
]

window = psg.Window('PyNotepad', layout=app_layout)
