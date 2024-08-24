import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import os

# Iniciando as configurações
audio = sr.Recognizer()
maquina = pyttsx3.init()


# Mensagem de início do assistente virtual
maquina.say('Olá, eu sou a Luma, como posso te ajudar?')
maquina.runAndWait()

# Reconhecendo microfone\
with sr.Microphone() as source:
    print('Ouvindo...')
    voz = audio.listen(source)
    comando = audio.recognize_google(voz, language = "pt-BR")
    comando = comando.lower()
    print(comando)

    if 'luma' in comando:
        comando = comando.replace('luma', '')
        maquina.say(comando)
        maquina.runAndWait()


