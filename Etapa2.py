import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os

# Iniciando as configurações
audio = sr.Recognizer()
maquina = pyttsx3.init()


# Mensagem de início do assistente virtual
maquina.say('Olá, eu sou a Luma, como posso te ajudar?')
maquina.runAndWait()

# Função para executar reconhecimento de microfone e Luma
def executar_comando():
    # Bloco de teste e exceção para microfone com falha
    try:
        # Reconhecendo microfone\
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language = "pt-BR")
            comando = comando.lower()

            # Teste de reconhecimento da Luma
            if 'luma' in comando:
                comando = comando.replace('luma', '')
                maquina.say(comando)
                maquina.runAndWait()
    
    except:
        print("Microfone não está funcionando!")
    return comando


# Função para executar as condições após reconhecimento de voz
def comando_voz_usuario():
    comando = executar_comando()

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        print(f'Agora são {hora}.')
        maquina.runAndWait()
    elif 'youtube' in comando:
        webbrowser.open("youtube.com")
        exit(0)
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'calculadora' in comando:
        loc = "C:\\Windows\\System32\\calc.exe"
        os.startfile(loc)
    elif 'tchau' in comando:
        maquina.say("Bye, bye!")
        maquina.runAndWait()

comando_voz_usuario()

# while True:
#     comando_voz_usuario()




