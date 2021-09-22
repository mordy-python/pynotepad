import PySimpleGUI as psg

while True:
    event,values=window.read()

    if event == None:
        break

window.close
app_layout = [
    [psg.Menu(['File', 'Help'])]
]

window = psg.Window('PyNotepad', layout=app_layout)
