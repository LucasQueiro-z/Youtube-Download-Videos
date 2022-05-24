import PySimpleGUI as sg
from pytube import YouTube, streams

class VideoDownloader:
    def __init__(self):
        self.url = ''

    def baixou(self):
        sg.theme('Dark')

        layout = [
            [sg.Text('Download Finalizado!')],
        ]

        sg.Window('Aviso',layout, icon='youtubedl_93529.ico').read()

    def erro(self):
        sg.theme('Dark')

        layout = [
            [sg.Text('Algum erro ocorreu, Tente novamente!')],
        ]

        sg.Window('Aviso', layout, icon='youtubedl_93529.ico').read()

    def home(self):
        sg.theme('DarkBlue4')

        layout = [
            [sg.Text('Insira a URL: '), sg.InputText()],
            [sg.Text('Caminho Ex: '), sg.InputText('C:/Users/name_user/Videos')],
            [sg.Button('Download Alta Qualidade', size=(50))],
            [sg.Button('Download Baixa Qualidade', size=(50))],
            [sg.Button('Sair',size=(50))],
        ]

        janela = sg.Window('YoutubeDownloader',icon='youtubedl_93529.ico', element_justification='center', element_padding=(0,5)).Layout(layout)
        while True:
            button, values = janela.read()

            if (button == 'Download Alta Qualidade'):
                try:
                    self.url = values[0]
                    video = YouTube(f"{self.url}")
                    stream = video.streams.get_highest_resolution()
                    if(stream.download(output_path=f'{values[1]}')):
                        self.baixou()
                except Exception:
                    self.erro()
            elif(button == 'Download Baixa Qualidade'):
                try:
                    self.url = values[0]
                    video = YouTube(f"{self.url}")
                    stream = video.streams.get_lowest_resolution()
                    if(stream.download(output_path=f'{values[1]}')):
                        self.baixou()
                except Exception:
                    self.erro()
            elif (button == 'Sair'):
                break

nova_janela = VideoDownloader()
nova_janela.home()