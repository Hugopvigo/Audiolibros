import argparse
from gtts import gTTS
import os

def create_audiolibro_gtts(text_file, output_file, lang="es"):
    try:
        if not os.path.exists(text_file):
            print(f"KO: Error: El archivo {text_file} no se encontró.")
            return

        with open(text_file, "r", encoding="utf-8") as file:
            text = file.read()

        if not text.strip():
            print(f"KO: Error: El archivo {text_file} está vacío.")
            return

        tts = gTTS(text=text, lang=lang)
        tts.save(output_file)

        print(f"OK: Audiolibro guardado como {output_file} (idioma: {lang})")

    except Exception as e:
        print(f"KO: Ocurrió un error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte un archivo de texto en un audiolibro MP3.")
    parser.add_argument("input", nargs="?", default="test.txt", help="Archivo de texto de entrada (default: test.txt)")
    parser.add_argument("output", nargs="?", default="test.mp3", help="Archivo MP3 de salida (default: test.mp3)")
    parser.add_argument("--lang", default="es", help="Idioma del audio (default: es)")

    args = parser.parse_args()
    create_audiolibro_gtts(args.input, args.output, args.lang)
