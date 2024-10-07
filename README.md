Aqui está o conteúdo atualizado do README.md com a adição de um tópico explicando como o sistema funciona:
# SICOMUV

## Descrição

O SICOMUV é um sistema projetado para facilitar a comunicação e inclusão digital, utilizando reconhecimento de texto e assistência por voz. Ele captura imagens, processa texto e oferece tradução e síntese de fala em múltiplos idiomas.

## Funcionalidades

- **Captura de Imagens**: Utiliza a câmera para capturar imagens e processá-las.
- **Reconhecimento de Texto**: Extrai texto de imagens utilizando OCR (Tesseract).
- **Tradução de Texto**: Traduz texto reconhecido para diferentes idiomas.
- **Síntese de Voz**: Converte texto traduzido em fala usando gTTS e Pyttsx3.
- **Comandos de Voz**: Interage com o usuário através de comandos de voz para capturar imagens e traduzir textos.

## Como Funciona

1. **Inicialização**: Ao iniciar o programa, o usuário é saudado com uma mensagem de boas-vindas e instruções sobre as opções disponíveis: capturar imagem, traduzir texto ou sair.

2. **Seleção de Idioma**: O usuário é solicitado a falar o idioma desejado para a tradução. O sistema reconhece o idioma a partir do comando de voz e confirma a seleção. Se o idioma não for reconhecido, o Português do Brasil é usado como padrão.

3. **Interação com o Usuário**: 
   - **Captura de Imagem**: O sistema ativa a câmera e permite que o usuário capture uma imagem dizendo "capturar".
   - **Processamento de Texto**: O texto extraído da imagem é traduzido e convertido em fala. O sistema fornece feedback auditivo durante todo o processo.

4. **Comandos de Voz**: O usuário pode continuar capturando imagens, traduzindo textos ou optar por sair do programa dizendo "sair".

5. **Encerramento**: O sistema libera os recursos utilizados e encerra o programa, informando que os recursos foram limpos.

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
source myenv/bin/activate  # No MacOS/Linux


Instale as dependências:
pip install -r requirements.txt


Configure o Tesseract OCR:
Certifique-se de que o Tesseract está instalado no caminho C:\Program Files\Tesseract-OCR\tesseract.exe. Ajuste o caminho no código se necessário.


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

Este conteúdo fornece uma visão detalhada de como o sistema funciona, desde a inicialização até o encerramento, além de instruções claras sobre como instalar e usar o sistema. Se precisar de mais ajustes ou informações adicionais, estou à disposição para ajudar!

