import PySimpleGUI as psg

app_layout = [
    [psg.Menu([['File'], ['Help']])],
    [psg.Multiline(s=(100, 100))]
]

window = psg.Window('PyNotepad', layout=app_layout, resizable=True)

while True:
    event,values=window.read()

    if event == None:
        break

window.close()