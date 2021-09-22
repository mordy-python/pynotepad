import PySimpleGUI as psg

app_layout = [
    [
        psg.Menu(
            [
                ["File", ["New File", "Open", "Save", "Save As", "Exit"]],
                ["Help", ["About"]],
            ]
        )
    ],
    [psg.Multiline(s=(100, 100))],
]

window = psg.Window("PyNotepad", layout=app_layout, resizable=True)

while True:
    event, values = window.read()

    if event == None:
        break

window.close()
