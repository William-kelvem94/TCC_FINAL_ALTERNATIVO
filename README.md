## Descrição

O SICOMUV é um sistema projetado para facilitar a comunicação e inclusão digital, utilizando reconhecimento de texto e assistência por voz. Ele captura imagens, processa texto e oferece tradução e síntese de fala em múltiplos idiomas.

## Funcionalidades

- **Captura de Imagens**: Utiliza a câmera para capturar imagens e processá-las.
- **Reconhecimento de Texto**: Extrai texto de imagens utilizando OCR (Tesseract).
- **Tradução de Texto**: Traduz texto reconhecido para diferentes idiomas.
- **Síntese de Voz**: Converte texto traduzido em fala usando gTTS e Pyttsx3.
- **Comandos de Voz**: Interage com o usuário através de comandos de voz para capturar imagens e traduzir textos.

## Requisitos

- Python 3.12
- Tesseract OCR
- Microfone e câmera conectados ao sistema

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/William-kelvem94/TCC_FINAL_ALTERNATIVO.git
   cd TCC_FINAL_ALTERNATIVO


Crie e ative um ambiente virtual:
python -m venv myenv
myenv\Scripts\activate  # No Windows
# source myenv/bin/activate  # No MacOS/Linux


Instale as dependências:
pip install -r requirements.txt


Configure o Tesseract OCR:

Certifique-se de que o Tesseract está instalado no caminho C:\Program Files\Tesseract-OCR\tesseract.exe.
Ajuste o caminho no código se necessário.



Uso

Execute o programa:
python Apresentação.py


Comandos de Voz:

Capturar Imagem: Diga "capturar" para tirar uma foto.
Traduzir Texto: Diga "traduzir" para iniciar o processo de tradução.
Sair: Diga "sair" para encerrar o programa.



Estrutura do Projeto

H5/: Contém o modelo treinado para reconhecimento de imagem.
myenv/: Ambiente virtual com pacotes instalados.
Apresentação.py: Script principal do sistema.
requirements.txt: Lista de dependências do projeto.

Contribuição
Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório e envie suas pull requests.
Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

