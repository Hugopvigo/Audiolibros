# Generador de Audiolibros con Python (Texto a MP3) 

Este proyecto proporciona un script en Python simple y fácil de usar para convertir archivos de texto (`.txt`) en audiolibros (`.mp3`). Ideal para escuchar tus libros, artículos o cualquier otro texto mientras estás en movimiento.

## Características ✨

* **Conversión Rápida:** Transforma texto a audio MP3 en segundos.
* **Fácil de Usar:** Simplemente coloca tu texto en `test.txt` y ejecuta el script.
* **Configurable:** El nombre del archivo de salida (`test.mp3`) se puede personalizar.
* **Multiplataforma:** Funciona en Windows, macOS y Linux.
* **gTTS:** Utiliza la API de Google Text-to-Speech para una voz natural.

## Requisitos 

* Python 3.6 o superior.
* Librería `gTTS`:
    ```bash
    pip install gTTS
    ```

## Instrucciones de Uso 

1.  **Descarga el script:**
    * Descarga el archivo `audiolibro.py` y guárdalo en tu ordenador.
2.  **Prepara el texto:**
    * Crea un archivo llamado `test.txt` en el mismo directorio que el script.
    * Copia y pega el texto que deseas convertir en audio dentro de `test.txt`.
3.  **Ejecuta el script:**
    * Abre una terminal o línea de comandos.
    * Navega hasta el directorio donde guardaste el script.
    * Ejecuta el siguiente comando:
        ```bash
        python audiolibro.py
        ```
4.  **Obtén el audiolibro:**
    * El script generará un archivo llamado `test.mp3` en el mismo directorio.
    * ¡Disfruta de tu audiolibro!

## Configuración Avanzada ⚙️

* **Nombre del archivo de salida:**
    * Puedes cambiar el nombre del archivo de salida modificando la variable `output_file` en el script.
    * Ejemplo: `output_file = "mi_audiolibro.mp3"`
* **Idioma:**
    * Puedes cambiar el idioma del audio modificando el parámetro `lang` en la llamada a `gTTS()`.
    * Ejemplo: `tts = gTTS(text=text, lang="en")` (para inglés).

## Notas Adicionales ℹ️

* Asegúrate de que tu sistema tenga una conexión a internet activa, ya que `gTTS` requiere acceso a la API de Google.
* Para textos largos, la generación del audiolibro puede tardar unos minutos.

## Contribuciones 

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el script, no dudes en crear un pull request.

## Licencia 

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.