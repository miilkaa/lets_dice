import PySimpleGUI as sg
from funcs import dice

dices_img = ['./images/d20_50x50.png', './images/d12_50x50.png', './images/d10_50x50.png', 
             './images/d8.png', './images/d6.png', './images/d4.png']
dices = ['d20', 'd12', 'd10', 'd8', 'd6', 'd4']
result = "Let's Dice!"
adjustment = 0  # Для хранения изменений
symbol = ""
layout = [
    [sg.Button("", key=d, image_filename=img, image_size=(50, 50), button_color=('white', 'white'), border_width=0) for d, img in zip(dices, dices_img)],
    [sg.Button('-', font=("Arial", 16, "bold"), button_color=('white', 'black'), size=(2)), sg.Text(symbol, key='-SYMBOL-', text_color=('black'), font=("Arial", 16), background_color="white", size=(1,1)), sg.Text(adjustment, key='-ADJUSTMENT-', text_color=('black'), font=("Arial", 16), background_color="white", size=(4,1)), sg.Text(result, key='-RESULT-', text_color=('black'), font=("Arial", 16), background_color="white"), sg.Button('+', font=("Arial", 16, "bold"), button_color=('white', 'black'), size=(2))],
    [sg.Button('Clear', button_color=('black'))]
]

window = sg.Window("Let's Dice", layout, size=(550, 200), resizable=True, background_color='white')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in dices:
        result = dice(int(event[1:]))
        adjustment = 0
        symbol = ''
        window['-RESULT-'].update(result)
        window['-ADJUSTMENT-'].update(adjustment)
        window['-SYMBOL-'].update(symbol)
    if event == '-':
        if isinstance(result, int):
            adjustment -= 1
            result -= 1
            if adjustment <= 0:
                symbol = ''
        window['-RESULT-'].update(result)
        window['-ADJUSTMENT-'].update(adjustment)
        window['-SYMBOL-'].update(symbol)
    if event == '+':
        if isinstance(result, int):
            symbol = "+"
            adjustment += 1
            result += 1
            if adjustment <= 0:
                symbol = ''
        window['-RESULT-'].update(result)
        window['-ADJUSTMENT-'].update(adjustment)
        window['-SYMBOL-'].update(symbol)
    if event == "Clear":
        result = "Let's Dice!"
        adjustment = 0
        symbol = ""
        window['-RESULT-'].update(result)
        window['-ADJUSTMENT-'].update(adjustment)
        window['-SYMBOL-'].update(symbol)

window.close()
