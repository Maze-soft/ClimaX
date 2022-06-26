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



#PARA DATA#
link = "https://api.hgbrasil.com/weather?woeid=455860"

resposta = requests.get(link)
conteudo = resposta.json()


'''
IMAGES:

nublado.jpg
ensolarado.jpg
chuva.jpg
trovoada.jpg
'''

hora = conteudo["results"]["time"]
dia = conteudo["results"]["forecast"][0]["weekday"]
data = conteudo["results"]["date"] # DATA
descriçao = conteudo["results"]["forecast"][0]["description"]
condi = conteudo["results"]["condition_slug"]
temp = conteudo["results"]["temp"]  #temperatura
maxi = conteudo["results"]["forecast"][0]["max"]
mini = conteudo["results"]["forecast"][0]["min"]

#temperatura = str(temp + "C")

class Programa(BoxLayout):
    tempum = temp
    maxum = maxi
    minum = mini
    condium = condi
    horaum = hora
    diaum = dia + ","
    desc = descriçao
    dataum = data

    if condium == "cloud":
        fundo = "nublado.jpg"

    elif condium == "rain":
        fundo = "chuva.jpg"

    else:
        fundo = "ensolarado.jpg"
        
    

    

class ClimaX(App):
    def build(self):
        return Programa()


ClimaX().run()


