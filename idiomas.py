# Si quieres usar pyttsx3 y verificas los idiomas instalados en tu OS. Voz mas robotica.

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
    print(voice.name)
    print(voice.languages)