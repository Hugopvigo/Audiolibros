# 🎧 Generador de Audiolibros con Python

Convierte tus archivos de texto (`.txt`) en audiolibros (`.mp3`) de forma sencilla utilizando Python y la potencia de Google Text-to-Speech (gTTS).

## ✨ Características

*   **🚀 Conversión Rápida:** Genera audiolibros en segundos.
*   **💻 Interfaz de Línea de Comandos (CLI):** Flexible y fácil de usar con argumentos.
*   **🌍 Soporte Multilingüe:** Elige el idioma que prefieras (español por defecto).
*   **🎙️ Calidad Natural:** Utiliza la API de gTTS para una voz clara y natural.
*   **🛠️ Alternativa Offline:** Incluye scripts de ejemplo para usar `pyttsx3` (motor offline).

## 📋 Requisitos

*   Python 3.6 o superior.
*   Conexión a internet (para gTTS).
*   Librería `gTTS`:
    ```bash
    pip install gTTS
    ```

## 🚀 Uso Rápido

1.  Prepara tu archivo `test.txt` con el contenido.
2.  Ejecuta el script:
    ```bash
    python3 audiolibro.py
    ```
3.  Busca tu archivo `test.mp3`.

## ⚙️ Configuración Avanzada (CLI)

El script ahora soporta argumentos para mayor flexibilidad:

```bash
python3 audiolibro.py [input_file] [output_file] --lang [código_idioma]
```

### Ejemplos:

*   **Especificar archivos:**
    ```bash
    python3 audiolibro.py mi_libro.txt mi_audio.mp3
    ```
*   **Cambiar el idioma (ej. Inglés):**
    ```bash
    python3 audiolibro.py libro_en.txt audio_en.mp3 --lang en
    ```

## 🎙️ Motores Alternativos (Offline)

Si prefieres no depender de internet o buscas una voz más robótica/local, el archivo `idiomas.py` muestra cómo listar las voces disponibles en tu sistema usando `pyttsx3`.

Para usarlo, instala:
```bash
pip install pyttsx3
```

## 📂 Estructura del Proyecto

*   `audiolibro.py`: Script principal de conversión (gTTS).
*   `idiomas.py`: Utilidad para explorar voces locales (pyttsx3).
*   `test.txt`: Archivo de ejemplo para pruebas.
*   `LICENSE`: Licencia MIT.

## 🤝 Contribuciones

¿Tienes alguna idea para mejorarlo? ¡Los Pull Requests son bienvenidos!

## 📄 Licencia

Este proyecto está bajo **CC BY-NC-SA 4.0** — Consulta [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**Desarrollado por [Hugo Perez-Vigo](https://hugopvigo.es)** · [@hugopvigo](https://x.com/hugopvigo)

[![GitHub](https://img.shields.io/badge/GitHub-Hugopvigo-181717?style=for-the-badge&logo=github)](https://github.com/Hugopvigo)

</div>