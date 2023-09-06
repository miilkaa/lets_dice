import PySimpleGUI as sg
from funcs import dice

dices_img = ['./images/d20_50x50.png', './images/d12_50x50.png', './images/d10_50x50.png', 
             './images/d8.png', './images/d6.png', './images/d4.png']
dices = ['d20','d12','d10','d8','d6','d4']
result = ''
layout = [
    [sg.Button("", key=d, image_filename=img, image_size=(50, 50), button_color=('white', 'white'), border_width=0) for d, img in zip(dices, dices_img)],
    [sg.Button('-', button_color=('black', 'black')), sg.Text(result, key='-RESULT-', text_color=('black')), sg.Button('+', button_color=('black', 'black'))]
]

window = sg.Window("Let's Dice", layout, size=(300, 200), resizable=True, background_color='white')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in dices:
        result = dice(int(event[1:]))
        window['-RESULT-'].update(result)
    if event == '-':
        if isinstance(result, int):
            result -= 1
        window['-RESULT-'].update(result)
    if event == '+':
        if isinstance(result, int):
            result += 1
        window['-RESULT-'].update(result)

window.close()
