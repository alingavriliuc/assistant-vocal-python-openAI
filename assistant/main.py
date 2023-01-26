import speech_recognition as sr
from gtts import gTTS
import openai
import os

# Initialisation de l'API OpenAI
openai.api_key = ""

# Initialisation du recognizer
r = sr.Recognizer()
opentChat = True

def say(text):
    tts = gTTS(text=text, lang='fr')
    tts.save("command.mp3")
    os.system("mpg321 command.mp3")

def requestGPT(user_request): 
    # Utilisation de l'API de OpenAI pour comprendre la demande
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{user_request}"),
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.5
    )

    # Affiche la réponse de l'API
    print(response["choices"][0]["text"])
    say(response["choices"][0]["text"])

say("Bonjour, je suis votre assistant personnel, comment puis-je vous aider ?")
print("Bonjour, je suis votre assistant personnel, comment puis-je vous aider ?")

with sr.Microphone() as source:
    print("En attente de votre commande...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio, language='fr-FR')
    requestGPT(command)
except:
    say("Désolé, je n'ai pas compris ce que vous avez dit.")
    print("Désolé, je n'ai pas compris ce que vous avez dit.")


