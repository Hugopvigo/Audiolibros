from gtts import gTTS

def create_audiolibro_gtts(text_file, output_file):
    try:
        with open(text_file, "r", encoding="utf-8") as file:
            text = file.read()

        tts = gTTS(text=text, lang="es")
        tts.save(output_file)

        print(f"OK: Audiolibro guardado como {output_file}")

    except FileNotFoundError:
        print(f"KO: Error: El archivo {text_file} no se encontró.")
    except Exception as e:
        print(f"KO: Ocurrió un error: {e}")

text_file = "test.txt"
output_file = "test.mp3"

create_audiolibro_gtts(text_file, output_file)