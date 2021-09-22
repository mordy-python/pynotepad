import PySimpleGUI as psg

menu_layout = [
    ['Help',['View Help', 'Send Feedack', 'About Notepad']]
]

app_layout = [
    [
        psg.Menu(
            [
                [menu_layout],
                ["Help", ["About"]],
            ]
        )
    ],
    [psg.Multiline(size=(125, 35))],
]

window = psg.Window("PyNotepad", layout=app_layout, resizable=True)

while True:
    event, values = window.read()

    if event == None:
        break

window.close()
