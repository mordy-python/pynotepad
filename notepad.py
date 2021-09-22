import PySimpleGUI as psg

menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Toolbar', ['---', 'Command &1', 'Command &2',
                              '---', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]

app_layout = [
    [psg.Menu(menu_def)],
    [psg.Multiline()]
]

window = psg.Window("PyNotepad", layout=app_layout, resizable=True)

while True:
    event, values = window.read()

    if event == None:
        break

window.close()
