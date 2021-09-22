import PySimpleGUI as psg

menu_def = [
    ["&File", ["&Open     Ctrl-O", "&Save       Ctrl-S", "E&xit"]],
]

app_layout = [[psg.Menu(menu_def)], [psg.Multiline()]]

window = psg.Window("PyNotepad", layout=app_layout, resizable=True)

while True:
    event, values = window.read()

    if event == None:
        break

window.close()
