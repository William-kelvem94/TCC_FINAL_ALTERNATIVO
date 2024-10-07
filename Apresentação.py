import cv2
import pytesseract
import os
import numpy as np
from gtts import gTTS
from pygame import mixer
import mtranslate
import keras.models
import speech_recognition as sr
import threading
import time
import pyttsx3
import signal
import sys

# Configuração do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

# Dicionário de idiomas suportados pelo gTTS
idiomas = {
    'Afrikaans': 'af', 'Árabe': 'ar', 'Bengali': 'bn', 'Cantonês': 'yue', 'Catalão': 'ca',
    'Chinês': 'zh-tw', 'Croata': 'hr', 'Checo': 'cs',
    'Dinamarquês': 'da', 'Holandês': 'nl', 'Inglês': 'en', 'Filipino': 'fil', 'Finlandês': 'fi',
    'Francês': 'fr', 'Alemão': 'de', 'Grego': 'el', 'Gujarati': 'gu', 'Hebraico': 'he', 'Hindi': 'hi',
    'Húngaro': 'hu', 'Indonésio': 'id', 'Italiano': 'it', 'Japonês': 'ja', 'Javanês': 'jw', 'Coreano': 'ko',
    'Letão': 'lv', 'Lituano': 'lt', 'Malaio': 'ms', 'Marata': 'mr', 'Norueguês': 'no', 'Polonês': 'pl',
    'Português (Brasil)': 'pt-br', 'Português Portugal': 'pt-pt', 'Romeno': 'ro', 'Russo': 'ru',
    'Sérvio': 'sr', 'Eslovaco': 'sk', 'Esloveno': 'sl', 'Espanhol': 'es', 'Suaíli': 'sw',
    'Sueco': 'sv', 'Tâmil': 'ta', 'Telugu': 'te', 'Tailandês': 'th', 'Turco': 'tr', 'Ucraniano': 'uk',
    'Vietnamita': 'vi', 'Galês': 'cy'
}

# Inicializar o mixer e pyttsx3
mixer.init()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Lock para controle de execução
fala_lock = threading.Lock()

def falar(texto):
    with fala_lock:
        print(texto)  # Para debug e visualização
        engine.say(texto)
        engine.runAndWait()

def reconhecer_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        falar("Diga algo...")
        try:
            audio = recognizer.listen(source, timeout=2)
            comando = recognizer.recognize_google(audio, language='pt-BR')
            falar("Você disse: " + comando)
            return comando.lower()
        except sr.WaitTimeoutError:
            falar("Tempo de escuta excedido")
            return None
        except sr.UnknownValueError:
            falar("Não entendi o que você disse")
            return None
        except sr.RequestError as e:
            falar("Erro ao solicitar resultados")
            return None

def selecionar_idioma_por_voz():
    falar("Diga o nome do idioma que você deseja no próximo comando:")
    comando = reconhecer_comando()
    if comando:
        for nome, codigo in idiomas.items():
            if nome.lower() in comando:
                return codigo
    falar("Idioma não reconhecido, usando Português do Brasil")
    return 'pt-br'

def load_trained_model(model_path):
    try:
        model = keras.models.load_model(model_path)
        falar("Modelo carregado com sucesso.")
        return model
    except Exception as e:
        falar(f"Erro ao carregar o modelo: {str(e)}")
        return None

def preprocess_image(image):
    resized_image = cv2.resize(image, (128, 128))
    processed_image = resized_image / 255.0
    return processed_image

def convert_prediction_to_text(image):
    text = pytesseract.image_to_string(image, lang='por', config=tessdata_dir_config)
    return text

def select_frame_por_voz(cap, result):
    frame_selected = None
    while True:
        ret, frame = cap.read()
        if not ret:
            falar("Falha ao capturar a imagem da câmera")
            continue
        cv2.imshow('frame', frame)

        if result['comando']:
            comando = result['comando']
            result['comando'] = None
            if comando and ("capturar" in comando or "enter" in comando):
                frame_selected = frame
                break
            elif comando and ("sair" in comando or "f" in comando):
                result['fim'] = True
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return frame_selected

def obter_comandos_de_voz(result):
    while not result['fim']:
        comando = reconhecer_comando()
        if comando:
            result['comando'] = comando

def signal_handler(sig, frame):
    falar("Interrupção detectada. Encerrando o programa...")
    sys.exit(0)

# Configurar o tratamento de sinal para interrupção
signal.signal(signal.SIGINT, signal_handler)

# Selecionar idioma via comando de voz
idioma_selecionado = selecionar_idioma_por_voz()

# Carregar o modelo treinado
model_path = 'C:/Users/willi/Documents/FACULDADE/10º SEMESTRE/PROJETO FINAL 2/CODIGO TCC1/OFICIAL - APRESENTAÇÃO/H5/H5.h5'
model = load_trained_model(model_path)

# Inicializar a câmera
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    falar("Erro ao abrir a câmera")
    sys.exit(1)

result = {'comando': None, 'fim': False}

thread = threading.Thread(target=obter_comandos_de_voz, args=(result,))
thread.start()

falar("Bem-vindo ao SICOMUV: Sistema de Comunicação Multifuncional com Reconhecimento de Texto e Assistência por Voz para Inclusão Digital.")
falar("Você pode escolher entre as opções: Capturar imagem, Traduzir texto ou Sair.")

while True:
    selected_frame = select_frame_por_voz(cap, result)
    if result['fim']:
        break
    if selected_frame is not None:
        gray = cv2.cvtColor(selected_frame, cv2.COLOR_BGR2GRAY)
        processed_image = preprocess_image(gray)
        input_image = np.expand_dims(processed_image, axis=0)
        prediction = model.predict(input_image)

        if prediction is not None:
            text = convert_prediction_to_text(gray)
            print("Texto:", text)

            translated_text = mtranslate.translate(text, 'pt', 'en')
            print("Tradução:", translated_text)

            if translated_text:
                with fala_lock:
                    tts = gTTS(text=translated_text, lang=idioma_selecionado)
                    audio_file = 'audio.mp3'
                    tts.save(audio_file)

                    mixer.music.load(audio_file)
                    mixer.music.play()
                    while mixer.music.get_busy():
                        time.sleep(0.5)

                    mixer.music.unload()
                    os.remove(audio_file)

            cv2.imshow('frame', selected_frame)

cap.release()
cv2.destroyAllWindows()
result['fim'] = True
thread.join()
falar("Recursos limpos. Programa encerrado.")