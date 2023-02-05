from PySimpleGUI import PySimpleGUI as sg
import qrcode
from PIL import Image

sg.theme('DarkBlue2')
layout=[

    [sg.Text("link"),sg.Input(key='linkey')],
    [sg.Text("Nome do Arquivo"),sg.Input(key='arquivo')],
    [sg.Button("Salvar")],
    [sg.Image("",key="imagem")]

]

janela=sg.Window('Qr code gerador',layout)
while True:
    eventos,valores=janela.read()

    if eventos==sg.WINDOW_CLOSED:
        break
    if eventos=="Salvar":
        link=valores["linkey"]
        arquivo=valores['arquivo']
        print(arquivo)
        imageQr=qrcode.make(link)
        imageQr.save(arquivo+".png")

        janela['imagem'].update(arquivo+".png")

