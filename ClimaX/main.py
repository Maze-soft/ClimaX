'''
**ANOTAÇOES**

No app vai ter dia(5 dias e 5 datas), data, descriçao, temperatura(min e max)

date , temp, forecast, weekday, description


'''







from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import requests






link = "https://api.hgbrasil.com/weather?woeid=455860"

resposta = requests.get(link)
conteudo = resposta.json()

'''
1 dia
'''

data = conteudo["results"]["date"] # DATA
temp = conteudo["results"]["temp"] #temperatura
dia = conteudo["results"]["forecast"][0]["weekday"]
descriçao = conteudo["results"]["forecast"][0]["description"]


dia2 = conteudo["results"]["forecast"][0]["date"]["date"]

print(dia2)



class Programa(BoxLayout):
    tempum = temp
    diaum = dia
    dataum = data
    descum = descriçao


class ClimaX(App):
    def build(self):
        return Programa()


ClimaX().run()

