import PySimpleGUI as psg

app_layout = [
    [psg.Menu(['File', 'Help'])]
]

window = psg.Window('PyNotepad', layout=app_layout)
while True:
    event,values=window.read()

    if event == None:
        break
window.close()