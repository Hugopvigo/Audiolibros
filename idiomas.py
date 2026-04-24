# Script para listar las voces disponibles en el sistema usando pyttsx3
# Útil si prefieres una síntesis de voz offline (más robótica)

import pyttsx3

def listar_voces():
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        print(f"--- Voces detectadas: {len(voices)} ---")
        for index, voice in enumerate(voices):
            print(f"ID: {voice.id}")
            print(f"Nombre: {voice.name}")
            print(f"Idiomas: {voice.languages}")
            print("-" * 30)
            
    except Exception as e:
        print(f"Error al inicializar el motor offline: {e}")
        print("Asegúrate de tener instalada la librería: pip install pyttsx3")

if __name__ == "__main__":
    listar_voces()
