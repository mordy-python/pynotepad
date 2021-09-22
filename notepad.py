import PySimpleGUI as psg

menu_def = [
    ["&File", ["&Open     Ctrl-O", "&Save       Ctrl-S", "E&xit"]],
# ['Help[View Help, Send Feedback, About Notepad]']
    ["Help", ["View Help", "Send Feedback", "About Notepad"]]
]

app_layout = [[psg.Menu(menu_def)], [psg.Multiline()]]

window = psg.Window("PyNotepad", layout=app_layout, resizable=True)

while True:
    event, values = window.read()

    if event == None:
        break
    elif event == 'Open':
            filename = psg.popup_get_file('file to open', no_window=True)
            print(filename)


window.close()
